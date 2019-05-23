# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import BookItem

class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']
    custom_settings = {
        'filename':'d:/dbbooktest1.json'
    }

    def parse(self, response:HtmlResponse):

        subjects = response.xpath("//li[@class='subject-item']")
        for subject in subjects:
            item = BookItem()
            titles = subject.xpath(".//h2//a//text()").extract()
            item['title'] = ''.join(map(lambda x: x.strip(), titles))
            pub = subject.xpath(".//div[@class='pub']/text()").extract()[0].strip()
            item['pub'] = pub
            rate = subject.xpath(".//span[@class='rating_nums']/text()").extract()[0].strip()

            item['rate'] = rate
            # items.append(item)

            yield item


