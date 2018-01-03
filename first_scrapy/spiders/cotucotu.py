# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("/Users/m-tominaga/Python/first_scrapy")
from first_scrapy.items import FirstScrapyItem

class CotucotuSpider(scrapy.Spider):
    name = 'cotucotu'
    allowed_domains = ['b.hatena.ne.jp']
    start_urls = ['http://b.hatena.ne.jp/ctop/it']

    def parse(self, response):
        for sel in response.css('div.entry-contents'):
            if sel.css('li.date::text').extract_first() is None :
                continue

            item = FirstScrapyItem()
            item['date'] = sel.css('li.date::text').extract_first()
            item['name'] = sel.css('a.entry-link::text').extract_first()
            item['link'] = sel.css('a::attr(href)').extract_first()
            yield(item)
