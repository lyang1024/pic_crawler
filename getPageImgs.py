import re
from urllib.request import urlopen
from urllib.error import URLError

import getTagImgs

def loadurl(url):
	try:
		conn = urlopen(url,timeout=5)
		html = conn.read().decode('utf-8')
		return html
	except URLError:
		return ""
	except Exception:
		print('unknown exception in conn.read()')
		return ""

#iterate through pages
def nextpage(url, path):
	reNextLink = "<a.*?href='(.*?)'>.*?</a>"
	reNextPage = '<div.*?id="wp_page_number.*?>.*?<ul>(.*?)</ul>'
	searchPathTail = '.*/([a-z]+).*?.html'
	searchurltail = '.*/(.*?.html)'
	searchhead = '(.*)/.?.html'
	pathTail = re.findall(searchPathTail,url,re.S)
	urlTail = re.findall(searchurltail,url,re.S)
	urlhead = re.findall(searchhead,url,re.S)
	path = path + '/' + pathTail[0]
	print(path)

	nextpageurl = []
	html = ''
	while True:
		html = loadurl(url)
		if html == '':
			print('load'+url+'error')
			continue
		else:
			break
	nextPage = re.findall(reNextPage,html,re.S)
	nextLink = re.findall(reNextLink,nextPage[0],re.S)
	nextLink.append(urlTrail[0])

	nextLink = sorted(list(list(set(nextLink))))
	for i in nextLink:
		nextpageurl.append(urlhead[0]+"/"+i)
	for i in nextpageurl:
		print(i)
		getTagImgs.getTagImgs(i,path)
