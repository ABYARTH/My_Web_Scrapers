import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

def search(item):
	print"finding you"
	img_list = getpicture(item)
	for im in img_list[4:-5]:
		savepicture(im)
		print"done...."

def getpicture(search):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent','Mozilla')]
	formatted_images = []
	for z in range(1,30):
		htmltext = browser.open("")
		img_urls = []
		soup = BeautifulSoup(htmltext)
		results = [i.get('src') for i in soup.findAll("img")] 
		#print results

		#pics = soup.findAll("img")
			#print pics
		for k in results:
			image_f = k
			#print image_f
			formatted_images.append(image_f)
	#print formatted_images 
	return formatted_images
def savepicture(url):
	hs = hashlib.sha224(url).hexdigest()
	#file_extension = url.split(".")[-1]
	#print url
	folder = "LOcation to store images"
	#fp = open(uri, 'wb')
	#if url !="":
	urllib.urlretrieve(url, folder)
	for i in range (1, 100):
		destination = folder+hs+"."+"jpg"
		#print dest
		urllib.urlretrieve(url, destination)
search('***')

