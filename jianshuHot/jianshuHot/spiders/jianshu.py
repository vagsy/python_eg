# -*- coding: utf-8 -*-
import scrapy
from jianshuHot.items import JianshuhotItem
import urllib

class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['www.jianshu.com']
    baseURL = 'https://www.jianshu.com/trending/monthly?page='
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        item = JianshuhotItem()
        articles = response.xpath("//ul[@class='note-list']/li")
        ids = []
        for article in articles:
            ids.append(articles.xpath("./@data-note-id").extract()[0])
            title = article.xpath("./div[@class='content']/a[@class='title']/text()").extract()[0]
            url = article.xpath("./div[@class='content']/a[@class='title']/@href").extract()[0]
            author = article.xpath("./div[@class='content']/div/div/a[@class='nickname']/text()").extract()[0]

            # 下载所有热门文章的缩略图, 注意有些文章没有图片
            try:
                image = article.xpath("./a[@class='wrap-img']/img/@src").extract()
                urllib.urlretrieve(image[0], 'D:/PycharmProjects/python_eg/jianshuHot/images/%s-%s.jpg' % (author[0], title[0]))
            except:
                print '--no---image--'

            likeNum = article.xpath("./div[@class='content']/div[@class='meta']/span[1]/text()").extract()[0].strip()
            readNum = article.xpath("./div[@class='content']/div[@class='meta']/a[1]/text()")[1].extract().replace("\n", "").strip()
            commentNum = article.xpath("./div[@class='content']/div[@class='meta']/a[2]/text()")[1].extract().replace("\n", "").strip()

            item['title'] = title
            item['url'] = 'http://www.jianshu.com' + url
            item['author'] = author

            item['readNum'] = readNum
            # 有的文章是禁用了评论的
            try:
                item['commentNum'] = commentNum
            except:
                item['commentNum'] = ''
            item['likeNum'] = likeNum
            yield item

        if self.offset < 10:
            self.offset += 1
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)