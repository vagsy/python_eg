# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):#类 ItcastItem  继承父类scrapy.Item
    # define the fields for your item here like:
    # 老师姓名
    name = scrapy.Field() #创建一个item字段  提取的字段存储到字段里面去
    # 老师职称
    title = scrapy.Field()
    # 老师信息
    info = scrapy.Field()
    # pass
