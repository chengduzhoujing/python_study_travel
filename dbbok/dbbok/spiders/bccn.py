# -*- coding: utf-8 -*-
from urllib import parse
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from ..items import BccnItem

class BccnSpider(CrawlSpider):
    name = 'bccn'
    allowed_domains = ['bccn.net']
    start_urls = ['https://www.bccn.net/']
    custom_settings = {
        'filename':'bccndownload.json'
    }

    rules = (
        Rule(LinkExtractor(allow=r'tag'), callback='parse_item', follow=True),
    )

    def parse_item(self, response:HtmlResponse):
        tag = ''.join(map(lambda x: x.strip(), response.xpath('//div[@class="nav"]//text()').extract()))
        if not tag:
            return {}
        item =BccnItem()
        item['tag'] = tag
        base_url = parse.urlparse(response.url).netloc
        contents = response.xpath('//table//tr')
        flag = True
        if contents:
            for content in contents:
                if flag:
                    flag=False
                    continue
                target = content.xpath('.//td[@class="td_1"]')
                item['link'] = base_url + target.xpath('./a/@href').extract()[0].strip()
                item['name'] = target.xpath('.//text()').extract()[0].strip()
                yield item



