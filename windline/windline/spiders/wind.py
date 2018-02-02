# -*- coding: utf-8 -*-
import scrapy
from windline.items import WindlineItem

class WindSpider(scrapy.Spider):
    name = 'wind'
    allowed_domains = ["www.windline.info"]
    baseURL = "http://www.windline.info/page/"
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//h2[@class='kratos-entry-title']/a")

        for node in node_list:
            item = WindlineItem()
            # 提取信息，并且将提取出的Unicode字符串编码为UTF-8编码
            item['title'] = node.xpath("./text()").extract()[0].encode("utf-8")

            yield item


        if len(response.xpath("//a[@class='next']")):
            url = response.xpath("//a[@class='next']/@href").extract()[0]

            yield scrapy.Request(url, callback = self.parse)