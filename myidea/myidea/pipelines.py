# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class MyideaPipeline(object):
#     def process_item(self, item, spider):
#         return item
class FirstPipeline(object):
    def __init__(self):
        print('-----------------init---------------------')

    def open_spider(self, spider):
        print('------------open---------------')
        print(spider.settings.get('filename'))
        self.file = open(spider.settings['filename'], 'w', encoding='utf8')
        self.file.write('[\n')

    def process_item(self, item, spider):
        print(type(item))
        self.file.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider):
        print('--------------close-----------------')
        self.file.write(']')
        self.file.close()

