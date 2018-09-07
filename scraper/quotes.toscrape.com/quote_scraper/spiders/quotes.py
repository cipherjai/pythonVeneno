# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

# its a callback method that scrapy will call when the responses to the start url are received
    def parse(self, response):
        self.log('Visited quotes spider' + response.url)

        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text':  quote.css('span.text::text').extract_first(),
                'tag': quote.css('a.tag::text').extract(),
                }
            yield item

        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin (next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        # yield{
        #     'author-name':response.css('small.author::text').extract(),
        #     'text':response.css('span.text::text').extract(),
        #     'tages':response.css('a.tag::text').extract(),
        # }
