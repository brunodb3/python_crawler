# -*- coding: utf-8 -*-

# Here we define the item pipelines

from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter

# export to json
class JsonExportPipeline(object):

    # here we initialize the class
    def __init__(self):
        self.files = {}

    @classmethod
    # we connect to the crawler items
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    # when the spider opens
    def spider_opened(self, spider):
        # we create the file in the outputs folder
        file = open('outputs/' + spider.name + '/' + spider.tag + '_items.json', 'w+b')
        self.files[spider] = file
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()

    # when the spider closes
    def spider_closed(self, spider):
        # we close the file and save it
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    # processing each item 
    def process_item(self, item, spider):
        # here we export each item (spider)
        self.exporter.export_item(item)
        return item