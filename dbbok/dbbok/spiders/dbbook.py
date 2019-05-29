# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from ..items import DbbokItem


class DbbookSpider(CrawlSpider):
    name = 'dbbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91?start=0&type=T']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )
    custom_settings = {
        'filename':'doubantushu.json'
    }
    def parse_item(self, response:HtmlResponse):
        item = DbbokItem()
        subjects = response.xpath("//li[@class='subject-item']")
        for subject in subjects:
            title = ''.join(map(lambda x:x.strip(), subject.xpath('.//h2//text()').extract()))
            pub = subject.xpath('.//div[@class="pub"]').extract()
            rate = subject.xpath('.//span[@class="rating_nums"]').extract()
            item['name'] = title
            item['pub'] = pub[0].strip() if len(pub) > 0 else '无'
            item['rate'] = rate[0].strip() if len(rate) > 0  else '0'
            yield item

