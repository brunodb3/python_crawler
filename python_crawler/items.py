# -*- coding: utf-8 -*-

# here we define the main classes for each item
# each item is used as a dict

# see documentation at:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field

# Stack Item
class StackItem(Item):
    url = Field()
    title = Field()
