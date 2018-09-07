# -*- coding: utf-8 -*-
import scrapy


class AmazonWebCrawlSpider(scrapy.Spider):
    name = 'amazon_web_crawl'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
