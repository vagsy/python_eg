# -*- coding: utf-8 -*-
import scrapy
from stack.items import StackItem

class StackSpiderSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    def parse(self, response):
        # 第一页
        questions = response.xpath('//div[@class="summary"]/h3')
        for question in questions:
            url = "http://stackoverflow.com" + question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_inside)

        # 其他页
        if len(response.xpath("//a[@rel='next']")):
            url = response.xpath("//a[@rel='next']/@href").extract()[0]

            yield scrapy.Request("http://stackoverflow.com" + url, callback=self.parse)

    def parse_inside(self, response):

        item = StackItem()
        item['title'] = response.xpath('//a[@class="question-hyperlink"]/text()').extract()[0]
        item['url'] = response.url
        item['question'] = response.xpath('//div[@class="question"]/table/tbody/tr/td[@class="postcell"]/node()')
        item['answer'] = response.xpath('//div[@class="answer"]/table/tbody/tr/td[@class="answercell"]/node()')

        yield item

