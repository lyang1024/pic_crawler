import re
from urllib.request import urlopen
from urllib.error import URLError
import getSinglePage

def loadurl(url):
	try:
		conn = urlopen(url,timeout=5)
		html = conn.read().decode('utf-8')
		return html
	except URLError:
		return ''
	except Exception:
		print('unknown exception in conn.read()')
		return ''

#set path and call getPageImgs module
def save_to_path(urllist,path):
	searchname = '.*/(.*?).html'
	current_path = ''
	for url in urllist:
		try:
			name = re.findall(searchname,url,re.S)
			current_path = path + '/' + name[0]
			getPageImgs.get_pic_list(url,current_path)
		except URLError:
			pass

#iterate through tags
def getTagImgs(url, path):
	tagList = '<div .*?class="pic".*?>.*?<a.*?href="(.*?)".*?target.*?>'
	html = ''
	while True:
		html = loadurl(url)
		if html == '':
			print ('load ' + url + ' error')
			continue
		else:
			break
	seriesList = re.findall(tagList,html,re.S)
	if len(seriesList) == 0:
		pass
	else:
		save_to_path(tagList,path)
