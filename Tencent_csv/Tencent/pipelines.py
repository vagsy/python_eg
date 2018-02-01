# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# class TencentPipeline(object):
#     def process_item(self, item, spider):
#         return item


import csv

class TencentPipeline(object):
    # 此处字段名与items.py中设置保持一致
    colname = ['positionName', 'positionLink', 'positionType', 'peopleNumber', 'workLocation', 'publishTime']

    def open_spider(self, spider):
        # 在爬虫启动时，创建csv，并设置newline=''来避免空行出现
        self.file = open("tencent.csv", "w")
        # 启动csv的字典写入方法
        self.writer = csv.DictWriter(self.file, self.colname)
        # 写入字段名称作为首行
        self.writer.writeheader()

    def close_spider(self, spider):
        # 在爬虫结束时，关闭文件节省资源
        self.file.close()

    def process_item(self, item, spider):
        # 把每次输出的item，写入csv中
        self.writer.writerow(item)
        return item
