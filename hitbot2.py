#!/usr/bin/env python
#
#   Title:  Hit Bot 2
#   Author: Chris Shenkan
#   Date:   5/7/2014
#   Version 0.3
#

import requests
import datetime
from BeautifulSoup import BeautifulSoup
import time
import sys

now = datetime.datetime.now()
currentDate = [str(now.month), str(now.day), str(now.year)]

url = "http://www.bostonfanfavorites.com"
host = url.replace("http://", "")
host = url.replace("https://", "")
host = url.replace("www.", "")
host = url.replace(".com", "")
host = url.replace(".net", "")
host = url.replace(".org", "")
#textfile = host + "_" + "-".join(currentDate) + ".txt"
#textfile = host + ""

response = requests.get(url)

# parse html
page = str(BeautifulSoup(response.content))
textfile = "1.txt"
f = open(textfile, 'w')
goodurllist = []

def processURL(urlfile):
    with open(urlfile, 'r') as uf:
        for line in uf:
            r = requests.get(line)
            if (r.status_code == requests.codes.ok):
                line.append(goodurllist)
    for ab in goodurllist:
        print ab

def getURL(page):
    """
    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        print url
        f.write(url)
        f.write("\n")
    else:
        print "Finished writing file."
        sys.exit(1)
