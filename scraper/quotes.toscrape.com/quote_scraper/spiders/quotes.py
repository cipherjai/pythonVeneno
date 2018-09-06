# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

# its a callback method that scrapy will call when the responses to the start url are received
    def parse(self, response):
        self.log('Visited quotes spider' + response.url)
        yield{
            'author-name':response.css('small.author::text').extract(),
            'text':response.css('span.text::text').extract(),
            'tages':response.css('a.tag::text').extract(),
        }
