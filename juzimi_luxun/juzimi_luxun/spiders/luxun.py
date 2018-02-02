# -*- coding: utf-8 -*-
import scrapy
from juzimi_luxun.items import JuzimiLuxunItem

class LuxunSpider(scrapy.Spider):
    name = 'luxun'
    allowed_domains = ['www.juzimi.com']
    baseURL = "http://www.juzimi.com/writer/%E9%B2%81%E8%BF%85?page="
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//a[@class='xlistju']")

        for node in node_list:
            item = JuzimiLuxunItem()
            # 提取信息，并且将提取出的Unicode字符串编码为UTF-8编码
            item['section'] = node.xpath("./text()").extract()[0].encode("utf-8")

            yield item

        if len(response.xpath("//li[@class='pager-next']")):
            url = response.xpath("//li[@class='pager-next']/a/@href").extract()[0]

            yield scrapy.Request("http://www.juzimi.com/" + url, callback=self.parse)
