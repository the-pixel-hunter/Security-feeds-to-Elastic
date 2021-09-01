#!/usr/bin/python3
import os
import re
import time
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from markdownify import markdownify as md

SLEEP_TIME = 180
FILE_PATH = "/opt/google_news_rss/json"
# FeedURL | Feed title
FEEDS = [
    "https://news.google.com/rss/topics/CAAqBwgKMJmeiQswi7mIAw?hl=en-GB&gl=GB&ceid=GB%3Aen | Malware - Malware - Google News",
    "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE4zYUcwU0FtVnVLQUFQAQ/sections/CAQqEAgAKgcICjDLvoILML3C_wIwvrD0BQ?hl=en-GB&gl=GB&ceid=GB:en | Information Security - Threats - Google News",
    "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE4zYUcwU0FtVnVLQUFQAQ?hl=en-GB&gl=GB&ceid=GB%3Aen | Information Security - Protection - Google News",
    "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE4zYUcwU0FtVnVLQUFQAQ/sections/CAQqEAgAKgcICjDLvoILML3C_wIw3rD0BQ?hl=en-GB&gl=GB&ceid=GB%3Aen | Information Security - Data Privacy - Google News",
    "https://news.google.com/rss/topics/CAAqLAgKIiZDQkFTRmdvTkwyY3ZNVEZvTUY4MmRESTRjeElGWlc0dFIwSW9BQVAB?hl=en-GB&gl=GB&ceid=GB%3Aen | Elastic NV - Latest - Google News",
    "https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSFFpZ0FQAQ/sections/CAQiSkNCQVNNUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pIUWlJT0NBUWFDZ29JTDIwdk1ERnNjSE1xQ2hJSUwyMHZNREZzY0hNb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pIUWlnQVABUAE?hl=en-GB&gl=GB&ceid=GB%3Aen | Technology - Computing - Google News",
    "https://news.google.com/rss/search?q=vulnerability%20when%3A1d&hl=en-GB&gl=GB&ceid=GB%3Aen | Search - Vulnerability - Google News",
    "https://news.google.com/rss/search?q=cve%20when%3A1d&hl=en-GB&gl=GB&ceid=GB%3Aen | Search - CVE - Google News",
    "https://news.google.com/rss/search?q=Data%20Breach%20when%3A1d&hl=en-GB&gl=GB&ceid=GB%3Aen | Search - Data Breach - Google News"
]


def date_to_iso(pubDate):
    gmt_date = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S GMT')
    return gmt_date.isoformat()

def strip_title_source(title):
    striped_title = re.sub('([^-]+)$', "", title)
    return striped_title[:-2]

def get_rss_feed(feed):
    vars = feed.split(" | ")
    print("INFO:Collecting rss feeed - rss_group="+vars[1]+"|url="+vars[0])
    response = requests.get(vars[0])
    bs_data = BeautifulSoup(response.text, "xml")
    news = bs_data.find_all('item')
    return news, vars[0], vars[1]

def dump_json(data, location):
    with open(location, 'w') as f:
        json.dump(data, f)
        
def collect_feeds():
    for feed in FEEDS:
        news, url, rss_group = get_rss_feed(feed)
        for item in news:
            NEWS_JSON.append(transform_item(item, url, rss_group)) 
    return 

def transform_item(item, url, rss_group):
        title = item.find('title').text
        link = item.find('link').text
        guid = item.find('guid').text
        pubDate = item.find('pubDate').text
        description = item.find('description').text
        source = item.find('source').text
        
        return {
            'title' : strip_title_source(title),
            'link' : link,
            'published' : date_to_iso(pubDate),
            'message' : md(description),
            'source_full' : rss_group,
            'type' : "Google News",
            'source' : source,
            'Feed' : url
        }

if __name__ == "__main__":
    
    while True: 
        NEWS_JSON = []

        now = datetime.now()
        current_time = now.strftime("%d-%m-%yT%H:%M:%S")
        file_name = "news-"+current_time+".json"
        location = os.path.join(FILE_PATH, file_name)

        print("INFO: Starting Collection at "+current_time)
        collect_feeds()
        dump_json(NEWS_JSON, location)

        print("INFO:Sleeping For",SLEEP_TIME)
        time.sleep(SLEEP_TIME)