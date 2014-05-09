#!/usr/bin/env python
#
#	Title: 		Bot Base Library Functions
#	Author:		Chris Shenkan
#	Date:		5/8/2014
#	Version:	1.0.3
#

from os import system
from requests import get
import sys
import time
import argparse

def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via raw_input() and return their answer.

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is one of "yes" or "no".
	"""
	valid = {"yes":True,   "y":True,  "ye":True,
			 "no":False,     "n":False}
	if default == None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "\
							 "(or 'y' or 'n').\n")
def print_version_info():
	print "Hit Bot\t0.3.1\nBy Chris Shenkan\t5/8/2014\n"

def clear_screen():
	system('clear')

def make_request(url):
	response = get(url)
	return response

def get_current_date():
	now = datetime.datetime.now()
	currentDate = [str(now.month), str(now.day), str(now.year)]
	return currentDate

def clean_url(url):
	host = url.replace("http://", "")
	host = host.replace("https://", "")
	host = host.replace("www.", "")
	host = host.replace(".com", "")
	host = host.replace(".net", "")
	host = host.replace(".org", "")
	return host

def create_log_filename(url): # TODO: implement into get_url
	host = clean_url(url)
	currentDate = get_current_date()
	textfile = host + "_scrape_" + "-".join(currentDate) + ".txt"

def create_logfile(filename): # TODO: implement logfile creation 
	sys.exit(1)

def get_url():
	try:
		print "Enter a url to be scraped..."
		print 'Usage  - "http://google.com/" <-- With the double quotes'
		print "'Q' or 'q' to quit"
		url = raw_input("URL: ")

		if url.lower() == "q":
			sys.exit(1)
	except NameError, n1:
		print "Error\nDescription: %s" % n1
		get_url()
	except SyntaxError, s1:
		print "Error\nDescription %s" % s1
		get_url()

	try:
		url = eval(url) 
	except SyntaxError, s2:
		print "You can't enter nothing for the URL!\n"
		get_url()
	return url

def test_url(url):
	res = make_request(url)

	if 300 <= int(res.status_code) > 400:
		print "Request failed: Response code: %d" % int(res.status_code)
		get_url()
	elif int(res.status_code) >= 400:
		print "Request failed: Response code: %d" % int(res.status_code)
		get_url()
	elif 200 <= int(res.status_code) < 300:
		print "Success!\nURL %s, returned Status Code: %d" % (str(url), int(res.status_code))
	else:
		print "Request failed: Reason Unknown"
		get_url()

def parse_arguments():
	parser = argparse.ArgumentParser(description='')
	parser.add_argument("--version", help="Display version information.", action='version', version='HitBot  -  version: 0.3.1  -  By Chris Shenkan 5/8/2014')
	parser.add_argument("-u", "--url", help="Specify URL to parse.", nargs='?', default="")
	parser.add_argument('-i', '--infile', nargs='?', type=argparse.FileType('r'), default=None)
	parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'), default=None)
	args = parser.parse_args()
	return parser, args