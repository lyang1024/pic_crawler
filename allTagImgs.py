import re
import urllib.request
import urllib.error
import getTagImgs

def loadurl(url):
	try:
		conn = urllib.request.urlopen(url,timeout=5)
		html = conn.read().decode('utf-8')
		print(html)
		return html
	except urllib.error.HTTPError as e:
		print('Error code:',e.code)
		return ''
	except urllib.error.URLError as e:
		print('Reason:',e.reason)
		return ''

def main(url,path):
	reTagContent = '<div.*?class="tags">.*?<span>(.*?)</span>'
	reTagUrl = '<a.*?href="(.*?)".*?>'
	print('start open the url')
	html = ''
	while True:
		html = loadurl(url)
		if html == '':
			print('load', url, 'error')
			continue
		else:
			break
	tagContent = re.findall(reTagContent, html, re.S)
	taglists = re.findall(reTagUrl, tagContent[0], re.S)
	taglists = sorted(list(set(taglists)))
	for url in taglists:
		getTagImgs.getTagImgs(url,path)


main('http://www.netbian.com','~/testImgs')
