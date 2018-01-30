# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名称
    allowed_domains = ['http://www.itcast.cn'] #爬虫允许域的范围
    start_urls = ['http://www.itcast.cn/'] #爬虫第一次启动时会从这个列表里开始抓取

    # 处理响应文件
    def parse(self, response):
        print (response.body)
        # pass
