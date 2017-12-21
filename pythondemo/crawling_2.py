import urllib2
def download(url, num_retries=2):
	print 'Downloading:', url
	try:
		html = urllib2.urlopen(url).read();
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries-1)
	return html
# print download('http://www.windline.info');
# print download('http://www.windline.info/500');
print download('http://httpstat.us/500')
