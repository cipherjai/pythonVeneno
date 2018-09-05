# -*- coding: utf-8 -*-
import scrapy


class AmazonproductcrawlerSpider(scrapy.Spider):
    name = 'AmazonProductCrawler'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
