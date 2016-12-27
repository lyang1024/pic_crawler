from urllib.request import urlopen
from urllib.error import URLError
import os
import re

#open url
#timeout set to 5

def load_url(url):
	try:
		conn = urlopen(url,timeout=5)
		html = conn.read().decode('utf-8')
		return html
	except URLError:
		return ''
	except Exception:
		print('unknown exception in conn.read()')
		return ''

#download image from a url to a specified file name

def download_pic(url,filename):
	try:
		conn = urlopen(url, timeout=5)
		f = open(filename,'wb')
		f.write(conn.read())
		f.close()
		return True
	except URLError:
		print('load'+url+'error')
		return False
	except Exception:
		print('unknown exception in conn.read()')
		return ''

#save image from a url to a path
def save_pic(url,path):
	searchname = '.*/(.*?.jpg)'
	name = re.findall(searchname,url)
	filename = path + '/' + name[0]

	#print filename + ':start'

	tryTimes = 3

	while tryTimes != 0:
		tryTimes -= 1
		if os.path.exists(filename):
			print(filename+' exists, skip')
			return True
		else:
			os.mknod(filename)
			if download_pic(url, filename):
				break

	if tryTimes >= 0:
		print(filename + ': over')
	else:
		print(url + ' : Failed to download')

#loop through all pics and store
def save_pic_list(picList,path):
	picurl = ''
	for picture in picList:
		save_pic(picture,path)

#parse source of web page and get pic url list
def get_pic_list(url,path):
	if os.path.exists(path):
		print(path+'exist')
	else:
		os.makedirs(path)
	html = ''
	while True:
		html = loadurl(url)
		if html == '':
			print('load'+url+'error')
			continue
		else:
			break

	rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
	rePicContent2 = '<div.*?class="postContent.*?>.*?<p>'
	rePicList = '<img.*?src="(.*?)".*?>'
	picContent = re.findall(rePicContent1, html, re.S)
	if len(picContent) <= 0:
		picContent = re.findall(rePicContent2, html, re.S)
	if len(picContent) <= 0:
		print('load false, over download this page and return')
		return False
	else:
		picList = re.findall(rePicList,picContent[0],re.S)
		pic_list(picList,path)

