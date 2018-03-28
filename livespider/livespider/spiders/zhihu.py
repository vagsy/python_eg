# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from livespider.items import LivespiderItem
import json


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def start_requests(self):
        starturl = 'https://api.zhihu.com/lives/homefeed?limit=10&offset=10&includes=live'
        yield Request(url=starturl, callback=self.parse)

    def parse(self, response):
        item = LivespiderItem()
        result = json.loads(response.text)
        records = result['data']
        for record in records:
            item['title'] = record['live']['subject']
            item['speaker'] = record['live']['speaker']['member']['name']
            # 将item传给pipelines.py保存到数据库
            yield item

        next_page_url = result['paging']['next'] + '&includes=live'
        yield Request(url=next_page_url, callback=self.parse)
