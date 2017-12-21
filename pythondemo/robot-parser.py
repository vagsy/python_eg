# -*- coding: utf-8 -*
import robotparser
rp = robotparser.RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
url = 'http://www.baidu.com'
user_agent = 'Baiduspider'
print rp.can_fetch(user_agent, url) #True
