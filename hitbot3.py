#!/usr/bin/env python
#
#   Title:  	Hit Bot 3
#   Author: 	Chris Shenkan
#   Date:   	5/7/2014
#   Version 	3.0.1
#

import sys
import requests
import time
import os
from bot_base import *
import fileinput
import re
import argparse
from bs4 import BeautifulSoup

def make_request(url):
	sys.exit(1)

def get_test_url():
	try:
		print "Enter a url to be scraped..."
		print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
		print "'Q' or 'q' to quit"
		url = raw_input("@> ")
		if url.lower() == "q":
			sys.exit(1)
	except NameError, n1:
		print "Error\nDescription: %s" % n1
		get_test_url()
	except SyntaxError, s1:
		print "Error\nDescription %s" % s1
		get_test_url()
	url = eval(url)
	res = requests.get(url)
	print res.status_code
	if 300 <= int(res.status_code) > 400:
		print "Request failed: Response code: %d" % int(res.status_code)
		get_test_url()
	elif int(res.status_code) >= 400:
		print "Request failed: Response code: %d" % int(res.status_code)
		get_test_url()
	elif 200 <= int(res.status_code) < 300:
		print "Success!\nStatus Code: %d" % int(res.status_code)
	else:
		print "Request failed: Reason Unknown"
		get_test_url()
def main():
	print_version_info()
	get_test_url()


if __name__ == '__main__':
	main()