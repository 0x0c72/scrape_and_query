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
	args, known_args, unknown_args = base.parse_arguments() 

	if known_args.url == '':
		url = base.get_url()
	else:
		url = known_args.url
	while base.test_url(url) is False:
		url = base.get_url()

	if known_args.outfile is not None:
		outfile = known_args.outfile
	else:
		outfile = base.create_log_filename(url)
	if known_args.infile is not None:
		infile = known_args.infile
	else:
		infile = None



if __name__ == '__main__':
	main()