# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):#类 ItcastItem  继承父类scrapy.Item
    # define the fields for your item here like:
    name = scrapy.Field() #创建一个item字段  提取的字段存储到字段里面去
    # pass
