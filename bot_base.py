#!/usr/bin/env python
#
#	Title: 		Bot Base Library Functions
#	Author:		Chris Shenkan
#	Date:		5/8/2014
#	Version:	0.1.4
#

from os import system
import requests
import sys
import time
import argparse

def query_yes_no(question, default="yes"):
	"""
	Ask a yes/no question via raw_input() and return their answer.

	@param string question a string that is presented to the user.
	@param string default the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).
	@return boolean valid True or False
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

def get_current_date():
	"""
	Returns the date as an array of month, day, and year using
		datetime.now()

	@return currentDate array of strings containg the date [month, day, year]
	"""
	now = datetime.datetime.now()
	currentDate = [str(now.month), str(now.day), str(now.year)]
	return currentDate

def clean_url(url): # ^(http|https)://
	"""
	Takes a string and returns the string 'cleaned' for use as the log filename.

	@param string url from input() or argparse, unmodified
	@return host string modified for use as log filename, 
		removed protocol, www, and frequently used TLDs
	"""
	host = url.replace("http://", "")
	host = host.replace("https://", "")
	host = host.replace("www.", "")
	host = host.replace(".com", "")
	host = host.replace(".net", "")
	host = host.replace(".org", "")
	if host.startswith('"'):
		host = host[1:]
	if host.endswith('"'):
		host = host[:-1]
	return host

def create_log_filename(url): 
	"""
	Function to return the full filename for the log file.

	@param url string the url in raw form from input or argparse
	@return textfile string the log filename as a string for use in creating the file
	"""
	host = clean_url(url)
	currentDate = get_current_date()
	textfile = host + "_scrape_" + "-".join(currentDate) + ".txt"
	return textfile

def create_log_file(filename): # TODO: implement logfile creation 
	sys.exit(1)


def get_url():
	"""
	Prompts the user for url input.  Adds double-quotes and checks if it's
	empty.  Then returns the input.  Exits the program when the input is Q or q.

	@return url string the users url input
	"""
	try:
		print "Enter a url to be scraped..."
		print 'Usage  -  http://google.com/'
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
	if url.endswith('"') is False and url.startswith('"') is False and url is not '':
		url = url + '"'
	if url.startswith('"') is False and url.endswith('"') is True and url is not '':
		url = '"' + url
	try:
		url = eval(url) 
	except SyntaxError, s2:
		if url is '':
			print "You can't enter nothing for the URL!\n"
		else:
			print "%s" % s2
		get_url()
	return url
 
def test_url(url):
	"""
	Tests the url given for a response. Returns false for all response codes
	at or over 300 and under 200.  Returns true for 200.

	@param url string url from input, double quoted
	@return True or False based on return code
	"""
	try:
		response = requests.get(url)
		responseCode = int(response.status_code)
	except (requests.exceptions.MissingSchema), re1:
		print re1
		print "Missing Schema, tryin entering the url with http://"
		return False
	except requests.HTTPError, re2:
		print "HTTP Error %s occured!" % re2.code
		return False

	if 300 <= responseCode > 400:
		print "Request Failed\nURL: %s, returned Status Code: %d" % (str(url), int(res.status_code))
		return False
	elif responseCode >= 400:
		print "Request Failed\nURL: %s, returned Status Code: %d" % (str(url), int(res.status_code))
		return False
	elif 200 <= responseCode < 300:
		print "Success!\nURL: %s, returned Status Code: %d" % (str(url), int(res.status_code))
		return True
	else:
		print "Request Failed\nURL: %s, returned invalid status code." % str(url)
		return False

def parse_arguments():
	"""
	Function to parse the arguments passed on command line with argparse module

	@return args, known_args, unknown_args dicts from parser's namespace
	"""
	parser = argparse.ArgumentParser(prog='HitBot', description='Scrapes a given website for links and then sends repeated requests to them.')
	parser.add_argument("--version", help="Display version information.", action='version', version='HitBot  -  version: 0.3.1  -  By Chris Shenkan 5/8/2014')
	parser.add_argument("-u", "--url", help="Specify URL to parse.", nargs='?', const="", default="")
	parser.add_argument('-i', '--infile', nargs='?', type=argparse.FileType('r'), default=None) # const defaults to None
	parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'), default=None)
	args = parser.parse_args()
	known_args, unknown_args = parser.parse_known_args()
	return args, known_args, unknown_args