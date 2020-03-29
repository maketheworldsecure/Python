#! usr/bin/env python
import bs4
from bs4 import BeautifulSoup as soup
import urllib2

url = "https://news.google.com/rss"

content = urllib2.urlopen(url).read()

Typeoffile =soup(content,'xml')

fullfiledata = Typeoffile.findAll("item")
print ("=" * 60)
print("\n")
print ("*" * 60)
print ("Day 2 Top News from Google News")
print ("*" * 60)
print("\n")
print ("=" * 60)
for Newsfeed in fullfiledata:
	print ('\033[93m' + Newsfeed.title.text + '\033[m')
	print ("============================================================================")
