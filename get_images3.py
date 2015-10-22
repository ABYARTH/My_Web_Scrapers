#!/usr/bin/env python
import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

def search(term):
	print"finding you"
	img_list = getPic(term)
	for im in img_list:
		print 'abc'
		savePic(im)
		print"done...."

def getPic(search):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent','Mozilla')]
	for z in range(13,16):
		htmltext = browser.open("PAGE_URLS_HERE")		
		print htmltext
		img_urls = []
		formatted_images = []
		soup = BeautifulSoup(htmltext)
		results = soup.findAll("img")
		#print results
		for k in results:
			image_f = k["*******"]
			if "******" in image_f: 
				#print image_f
				return formatted_images
				formatted_images.append(image_f)
	print formatted_images 
	

def savePic(url):
	hs = hashlib.sha224(url).hexdigest()
	file_extension = url.split(".")[-1]
	#print url
	folder = "~/****/new folder/pics.jpg"
	#fp = open(uri, 'wb')
	#if url !="":
	urllib.urlretrieve(url, folder)
	destination = folder+hs+"."+file_extension
	#print dest
	urllib.urlretrieve(url, destination)
search('cars')

#execfile('C:\Users\Abyarth\Desktop\web scraping\get_images3.py')
