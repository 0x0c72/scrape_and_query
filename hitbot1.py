#!/usr/bin/env python
#
#	Title:	Hit Bot 1
#	Author:	Chris Shenkan
#	Date:	5/7/2014
#	Version	0.3
#

import re, urllib
import sys
import time
import fileinput

file_array = []

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

def scrape_url():
	print "Enter the URL you wish to crawl.."
	print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
	myurl = input("@> ")
	try:
		textfile = file(raw_input("Enter a filename to store URL's (no quotes): "), 'wt')
	except IOError, x0:
		print "Cannot open %s" % textfile.name
		textfile = file(raw_input("Enter a filename to store URL's (no quotes): "), 'wt')

	file_array.append(textfile.name)

	try:
		for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
			print i
			try: 
				textfile.write(i+'\n')
			except IOError as io1:
				print "Error %s" % io1
	except urllib.error.URLError as x1:
		print "Error %s" % x1
		print "\nContinuing...\n"
		try:
			for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
				print ee
				try:
					textfile.write(ee+'\n')
				except IOError as io2:
					print "Error %s" % io2
		except urllib.error.URLError as x2:
			print "Error: %s" % x2
			print "\nContinuing...\n"			
	textfile.close()

def query_urls(files):
	url_list = []
	cleaned_files = clean_logfiles(files)
	for files in cleaned_files:
		with open(files) as f:
			url_list = f.read().splitlines()

def clean_logfiles(to_clean):
	time.sleep(1)



scrape_url()
q = query_yes_no("Would you like to begin querying the scraped URL's from the text file?")
if (q == True):
	query_urls(file_array)
else:
	q2 = query_yes_no("Would you like to exit?")
	if (q2 == True):
		sys.exit
	else:
		q3 = query_yes_no("Would you like to scrape again then?")
		if (q3 == True):
			scrape_url()
		else:
			q4 = query_yes_no("Make your goddamn mind up, so you want to exit?")
			if (q4 == True):
				sys.exit
			else:
				print "Too bad.."
				time.sleep(2)
				sys.exit

