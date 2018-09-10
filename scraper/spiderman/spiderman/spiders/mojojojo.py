# -*- coding: utf-8 -*-
import scrapy


class MojojojoSpider(scrapy.Spider):
    name = 'mojojojo'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.{}/gp/bestsellers/electronics/6459737011/ref=sr_bs_0_6459737011_1'.format(allowed_domains[0])]
    # print('https://www.{}/gp/bestsellers/electronics/6459737011/ref=sr_bs_0_6459737011_1'.format(allowed_domains[0]))

    # sketch the dictionary inside tis method to fetch the data in the yield
    def parse(self, response):
        print("-----------------------------------------------------------------------")
        print(products)
        print("_________________________________________________________________________")
        for product_item in response.xpath('//span[contains(@class, "a-list-item")]').extract():
            item = {
                'product_name':product_item.xpath('//span[contains(@class, "zg-text-center-align")]/text()').extract(),
                'product_sale_price': product_item.xpath('//span[contains(@class, "p13n-sc-price")]/text()').extract_first(),
                'product_rating': product_item.xpath('//span[contains(@class, "a-icon-alt")]/text()').extract_first(),
                'product_link_endpoint': product_item.xpath('//a[contains(@class, "a-link-normal")]/text()').extract_first(),
                'product_bestseller_rank':product_item.xpath('//span[contains(@class, "zg-badge-text")]/text()').extract_first(),
                }
            yield item
