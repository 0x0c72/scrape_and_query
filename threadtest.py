#!/usr/bin/python

import threading
import time
import requests
from bs4 import BeautifulSoup

class getterThread(threading.Thread):
	def __init__(self, threadID, url):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.url = url
	def run(self):
		print "Starting " + self.name + " ID: " + str(self.threadID)
		check_url(self.url)
		print "URL is %s - Thread ID: %d" % (self.url, self.threadID)
		print "Exiting " + self.name + " ID: " + str(self.threadID)

def check_url(url):
	res = requests.get(url)
	page = str(BeautifulSoup(res.content))
	print str(res.status_code)
	

def main():
	urlList = ['http://bostonfanfavorites.com', 'http://google.com', 'http://google.com']
	i = 1
	ta = []
	name = "Thread"
	for url in urlList:
		tName = name + str(i)
		print "Initializing thread %s" % tName
		tName = getterThread(i, url)
		ta.append(tName)
		i += 1
	for thread in ta:
		thread.start()

if __name__ == '__main__':
	main()