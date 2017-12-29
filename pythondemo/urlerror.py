# -*- coding: utf-8 -*

# 通常，URLError在没有网络连接(没有路由到特定服务器)，或者服务器不存在的情况下产生。
# 这种情况下，异常同样会带有"reason"属性，它是一个tuple（可以理解为不可变的数组），
# 包含了一个错误号和一个错误信息。


import urllib2

req = urllib2.Request('http://www.baibai.com')

try:
    urllib2.urlopen(req)

except urllib2.URLError, e:
    print e.reason