# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstScrapyItem(scrapy.Item):
    date = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    pass
