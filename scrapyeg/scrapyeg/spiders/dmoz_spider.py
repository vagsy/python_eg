# -*- coding: utf-8 -*
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz" #该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.windline.info/archives/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print '=========================='
            print title
            print link
            print desc

#启动爬虫
#scrapy crawl dmoz
