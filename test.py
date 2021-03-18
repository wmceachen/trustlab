import gzip
import re
import requests
from collections import Counter
from utils import *
#https://economictimes.indiatimes.com/definition/category/Economy
# URL_MATCH = '(?<=WARC-Target-URI: ).*'
# # URL_MATCH = 'WARC-Target-URI:'

def is_any(string:str, options:[str]):
    return any(o.lower() in string for o in options)

def has_some(string:str, options:[str], req=5):
    count = Counter(string.split())
    return sum(count[o.lower()] for o in options) > req
def text_thing(page_text):
    url, _, text = page_text.partition('\r')
    text = text.lower()
    if has_some(text, COVID_WORDS) and has_some(text, ECON_WORDS) and has_some(text, NEWS_WORDS):
        # print([o.lower() for o in ECON_WORDS if o.lower() in text])
        return True
    return False

# for url in get_paths()
#     stream = requests.get(url).content
#     print()
s = requests.get('https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2020-50/segments/1606141753148.92/wet/CC-MAIN-20201206002041-20201206032041-00719.warc.wet.gz', stream=True)
print(s.content, file=open('text.txt', 'w+'))
# with gzip.open('CC-MAIN-20201206002041-20201206032041-00719.warc.wet.gz', 'rb') as f:
#     file_content = f.read().decode("utf-8")
#     # print(file_content)
#     # print(type(file_content))
#     # m = re.findall(URL_MATCH, file_content)
#     # print(m)
#     print(len(list(filter(text_thing, file_content.split('WARC-Target-URI: ')))))
    
#iterate through, every time we find a URI reset bools about covid and economy, then look for next