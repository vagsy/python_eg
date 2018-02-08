# -*- coding: utf-8 -*-
import scrapy
from stack.items import StackItem

class StackSpiderSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    def parse(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = "http://stackoverflow.com" + question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item

        if len(response.xpath("//a[@rel='next']")):
            url = response.xpath("//a[@rel='next']/@href").extract()[0]

            yield scrapy.Request("http://stackoverflow.com" + url, callback=self.parse)
