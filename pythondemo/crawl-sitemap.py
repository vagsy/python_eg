# -*- coding: utf-8 -*
import urllib2
import re

def download(url, user_agent='wswp', num_retries=2):
	# print 'Downloading:', url
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

def crawl_sitemap(url):
	# download the sitemap file
	sitemap = download(url)
	# extract the sitemap links  |extract 提取
	try:
		links = re.findall('<loc>(.*?)</loc>', sitemap)
	except re.error as e:
		print 'Download error:', e.reason
		links = None
	# download each links
	for link in links:
		print link
		html = download(link)
		# print html

# crawl_sitemap('http://example.webscraping.com/sitemap.xml')
crawl_sitemap('http://www.windline.info/sitemap.xml')
# crawl_sitemap('http://bbit.top/sitemap.xml')

