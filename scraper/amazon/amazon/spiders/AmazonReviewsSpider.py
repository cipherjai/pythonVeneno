# -*- coding: utf-8 -*-
import scrapy

class AmazonReviewsSpider(scrapy.Spider):
    name = 'AmazonReviews'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/Amazon-Echo-Dot-Portable-Bluetooth-Speaker-with-Alexa-Black/dp/B01DFKC2SO?pd_rd_wg=jbHva&pd_rd_r=f997ef98-0614-42a3-acb5-bcb0d6eb7ecb&pd_rd_w=rZyMm&ref_=pd_gw_simh&pf_rd_r=TSMY899X7TSAPEE034AP&pf_rd_p=b841581f-e864-5164-afa6-4c18a8348879".format(i) for i in range(1,11)
     ]

    def parse(self, response):
        prod_name =  response.xpath('//a[contains(@data-hook, "product-link")]/text()').extract()
        prod_price = response.xpath('//span[contains(@class, "a-color-price arp-price")]/text()').extract()
        Revw_author = response.xpath('//a[contains(@data-hook, "review-author")]/text()').extract()
        Revw_title = response.xpath('//a[contains(@data-hook, "review-title")]/text()').extract()
        Revw_rating = response.xpath('//i[contains(@data-hook, "review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract()
        Revw_date = response.xpath('//span[contains(@data-hook, "review-date")]/text()').extract()
        Revw_content = response.xpath('//span[contains(@data-hook, "review-body")]/text()').extract()
        Revw_helpful = response.xpath('//span[contains(@data-hook, "helpful-vote-statement")]/text()').extract()


        yield {
            'prod_name' : prod_name,
            'prod_price' : prod_price,
            'Review_author': Revw_author,
            'Review_title': Revw_title,
            'Review_rating': Revw_rating,
            'Review_date': Revw_date,
            'Review_content': Revw_content,
            'Review_helpfulness': Revw_helpful
        }
