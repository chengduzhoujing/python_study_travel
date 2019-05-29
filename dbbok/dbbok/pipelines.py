# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DbbokPipeline(object):
    def __init__(self):
        print('-------init--------------')

    def open_spider(self, spider):
        self.file = open(spider.settings['filename'], 'w')
        self.file.write('[\n')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item)) + ',\n')
        return item

    def close(self, spider):
        pass

    def __del__(self):
        self.file.write(']')
        self.file.close()

class BccnPipeline(object):

    def open_spider(self, spider):
        self.file = open(spider.settings['filename'], 'w')
        self.file.write('[\n')

    def process_item(self, item, spider):
        target = dict(item)
        if not target.get('tag', None):
            return
        self.file.write(json.dumps(dict(target)) + ',\n')
        return item

    def __del__(self):
        self.file.write(']')
        self.file.close()
