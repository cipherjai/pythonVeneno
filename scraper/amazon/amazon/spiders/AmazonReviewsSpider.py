# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    name = 'AmazonReviews'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/TCL-32S305-32-Inch-Smart-Model/product-reviews/B01MU1GBLL/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber={}&sortBy=recent".format(i) for i in range(1,11)
     ]

    def parse(self, response):
        Revw_author = response.xpath('//a[contains(@data-hook, "review-author")]/text()').extract()
        Revw_title = response.xpath('//a[contains(@data-hook, "review-title")]/text()').extract()
        Revw_rating = response.xpath('//i[contains(@data-hook, "review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract()
        Revw_date = response.xpath('//span[contains(@data-hook, "review-date")]/text()').extract()
        Revw_content = response.xpath('//span[contains(@data-hook, "review-body")]/text()').extract()
        Revw_helpful = response.xpath('//span[contains(@data-hook, "helpful-vote-statement")]/text()').extract()

        yield {
            'Review_author': Revw_author,
            'Review_title': Revw_title,
            'Review_rating': Revw_rating,
            'Review_date': Revw_date,
            'Review_content': Revw_content,
            'Review_helpfulness': Revw_helpful

        }