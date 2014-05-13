#!/usr/bin/env python
#
#   Title:  	Hit Bot
#   Author: 	Chris Shenkan
#   Date:   	5/7/2014
#   Version 	0.3.2
#

import sys
import requests
import os
import bot_base as base 
import fileinput
import re
import argparse
from bs4 import BeautifulSoup


def main(): # TODO: implement conditions to check for cmdline arguments before asking for input
	parser, args = base.parse_arguments() # debug - semi-permanent
	known, unknown = parser.parse_known_args() # debug semi-permanent
	print known # debug
	print unknown # debug
	print known.url * 10 # debug
	if known.url == '':
		url = base.get_url()
	else:
		url = known.url
	while base.test_url(url) is False:
		url = base.get_url()
	

if __name__ == '__main__':
	main()