#!/usr/bin/env python
#
#   Title:  	Hit Bot 3
#   Author: 	Chris Shenkan
#   Date:   	5/7/2014
#   Version 	3.0.1
#

import sys
import requests
import os
from bot_base import *
import fileinput
import re
import argparse
from bs4 import BeautifulSoup



def main():
	parser, args = parse_arguments()
	known, unknown = parser.parse_known_args()
	print known
	print unknown
	print known.url * 10
	url = get_url()
	test_url(url)

if __name__ == '__main__':
	main()