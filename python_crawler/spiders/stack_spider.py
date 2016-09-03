# -*- coding: utf-8 -*-

# here we define the spider used for the Stack Overflow website

import logging

from scrapy import Spider 
from scrapy.selector import Selector
from python_crawler.items import StackItem

# Stack Spider Class
class StackSpider(Spider):
    # an unique name
    name = "stack"

    # initializer
    def __init__(self, tag='', pages=''):
        if tag:
            # checks if user sent a tag argument
            self.tag = tag
        else:
            # if not, use 'javascript' as default
            self.tag = 'javascript'

        if pages:
            # checks if user sent a pages argument (and it's lower than 16)
            self.pages = pages
        else:
            # if not, use 1 as start and 9 as end for default
            self.pages = '9'

        # the domains the spider is allowed to visit
        self.allowed_domains = ["stackoverflow.com"]
        # the urls the spider is starting at
        self.start_urls = []

        # appending the urls to the spider
        urlStart = "http://stackoverflow.com/questions/tagged/" + self.tag + "?sort=newest&pageSize=50&"
        for page in range(int(self.pages)):
            newUrl = urlStart + "page=" + str(page + 1)
            self.start_urls.append(newUrl)

        logging.info('Starting spider at: ' + self.start_urls[0])

    # parsing the response html files
    def parse(self, response):
        # a dictionary containing all the latest questions (inside any <h3>)
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # loops the question dictionary
        for question in questions:
            item = StackItem()
            # each question's title
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            # each question's url (from the <a>)
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            # returns the items one by one
            yield item

        logging.info('Spider success!')
