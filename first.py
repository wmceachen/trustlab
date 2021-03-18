# AN EARLY ATTEMPT, CAN IGNORE
import requests
import re
from warcio.archiveiterator import ArchiveIterator
from warcio.recordloader import ArcWarcRecord
from itertools import chain
from multiprocessing.dummy import Pool as ThreadPool


HTTP_BASE_PATH = 'https://commoncrawl.s3.amazonaws.com/'
paths = []
for i in range(1, 11):
    with open(f'paths/warc-{i}.paths') as f:
        paths.extend(map(lambda p: HTTP_BASE_PATH + p, f.read().splitlines()))

path_chain = chain(paths)


# def paths(http_path: str):
e = next(path_chain)
stream = requests.get(e, stream=True).raw


def valid_record2(record: ArcWarcRecord) -> bool:

    if record.rec_type != 'response':
        return False
    if record.http_headers.get_header('Content-Type') != 'text/html':
        return False
    return True


def valid_record(record):
    """Filter the Archive Iterator

    Args:
        record (ArcWarcRecord): [any record]

    Returns:
        bool: [if the record is an actual HTML webpage]
    """
    return not record.rec_type == "warcinfo" and ".com/" in record.rec_headers.get_header("WARC-Target-URI")


def has_covid(record):
    return valid_record(record) and 'covid' in record.rec_headers.get_header("WARC-Target-URI")


for record in filter(valid_record, ArchiveIterator(stream)):
#     # if record.rec_type == "warcinfo":
#     #     continue

#     # if not ".com/" in record.rec_headers.get_header(
#     #     "WARC-Target-URI"
#     # ):
#     #     continue
    url = record.rec_headers.get_header(
        "WARC-Target-URI"
    )
    print(url)
    # contents = (
    #     record.content_stream()
    #     .read()
    #     .decode("utf-8", "replace")
    # )
    # print(contents)

# https://stackoverflow.com/questions/57838041/how-to-use-parallel-processing-filter-in-python
tp = ThreadPool()


# def pool_filter(pool, func, candidates):
#     return [c for c, keep in zip(candidates, pool.map(func, candidates)) if keep]


# print(pool_filter(tp, has_covid, ArchiveIterator(stream)))
