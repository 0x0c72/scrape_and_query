#!/usr/bin/env python
#
#   Title:  	Hit Bot
#   Author: 	Chris Shenkan
#   Date:   	5/7/2014
#   Version 	0.3.1
#

import sys
import requests
import os
#from bot_base import *
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
	url = base.get_url()
	base.test_url(url)

if __name__ == '__main__':
	main()