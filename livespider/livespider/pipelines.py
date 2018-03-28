# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class LivespiderPipeline(object):

    def open_spider(self, spider):
        # 初始化爬虫，开启数据库或者新建一个csv文件
        self.con = sqlite3.connect('zhihulive.db')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        # 写入数据库或数据文件
        title = item['title']
        speaker = item['speaker']
        sql_command = "INSERT INTO LiveTable (title,speaker) VALUES ('{title}','{speaker}')".format(title=title,
                                                                                                    speaker=speaker)
        self.cur.execute(sql_command)
        self.con.commit()
        return item

    def close_spider(self, spider):  # 关闭数据库或者数据文件
        self.con.close()
