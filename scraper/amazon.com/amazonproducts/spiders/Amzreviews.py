# -*- coding: utf-8 -*-
import scrapy


class AmzreviewsSpider(scrapy.Spider):
    name = 'Amzreviews'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/TCL-32S305-32-Inch-Smart-Model/product-reviews/B01MU1GBLL/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        for revw in response.xpath('//div[contains(@data-hook,"review")]'):
            yield {
                'author': revw.xpath('.//a[contains(@data-hook, "review-author")]/text()').extract_first(),
                'title': revw.xpath('.//a[contains(@data-hook, "review-title")]/text()').extract_first(),
                'rating': revw.xpath('.//i[contains(@data-hook, "review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract_first(),
                'date': revw.xpath('.//span[contains(@data-hook, "review-date")]/text()').extract_first(),
                'helpful_to': revw.xpath('.//span[contains(@data-hook, "helpful-vote-statement")]/text()').extract_first(),
                'content': revw.xpath('.//span[contains(@data-hook, "review-body")]/text()').extract_first(),
                'verification': revw.xpath('.//span[contains(@data-hook, "avp-badge")]/text()').extract_first(),
                'product_type': revw.xpath('.//span[contains(@data-hook, "cr-widget-AsinVariation")]/text()').extract_first()
            }
