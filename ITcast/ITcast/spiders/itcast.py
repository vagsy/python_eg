# -*- coding: utf-8 -*-
import scrapy
# 从...路径,引入...类
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数*必需
    name = "itcast"
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ["http://www.itcast.cn"] #爬虫允许域的范围
    # 起始url列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"] #爬虫第一次启动时会从这个列表里开始抓取

    # 处理响应文件
    def parse(self, response):
        # 节点列表
        node_list = response.xpath("//div[@class='li_txt']")

        #用来存储所有的item字段的
        items = []
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = ItcastItem()
            # .extract() 将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
            items.append(item)

        return items
        # pass
