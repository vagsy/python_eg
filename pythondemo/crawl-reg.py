# -*- coding: utf-8 -*
# 正则爬虫
import re
import urllib2

def download(url, user_agent='wswp', num_retries=2):
	print 'Downloading:', url
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, user_agent, num_retries-1)
	return html

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url)
print re.findall('<td class="w2p_fw">(.*?)</td>', html)

