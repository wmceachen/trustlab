# trustlab
Trust Lab CommonCrawl coding challenge

To create a results.txt with the desired sites, run `python results.py`.  

In this version, I assume that any site in which content meets certain vocabulary thresholds is valid. For example, if a site mentions COVID, and news, and economic terms more than 8 times, it is probably a news site about the economic effects of COVID.

In the past 6 hours, I spent undue amount of time trying to work with WARC, rather than WET, files. Upon realizing my error (WARC files are larger, unnecessary, and slower), I switched to WET. From there, I built a basic identification program that parsed the large text tiles, splitting at individual URLS. I found that the largest computational limitations were in requesting and filtering. Requesting each WARC file takes between 10 and 20 seconds, and filtering through the WARC files takes upwards of a minute.

