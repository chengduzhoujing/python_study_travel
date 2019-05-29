# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbbokItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    pub = scrapy.Field()
    rate = scrapy.Field()



class BccnItem(scrapy.Item):

    tag = scrapy.Field()
    link = scrapy.Field()
    name = scrapy.Field()


