# -*- coding: utf-8 -*-
import scrapy


class AmzproductsSpider(scrapy.Spider):
    name = 'Amzproducts'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Electronics-LED-LCD-TVs/zgbs/electronics/6459737011/ref=zg_bs_pg_2?_encoding=UTF8&pg={}'.format(i) for i in range(1,3)]

    def parse(self, response):
        urls= response.css('li.zg-item-immersion>span>div>span>a::attr(href)').extract()
        for url in urls:
            url= response.urljoin(url)
            yield scrapy.Request(url=url, callback= self.parse_prod_details)

    def parse_prod_details(self,response):
        yield {
            'Product': response.xpath('normalize-space(//h1[contains(@id,"title")]/span/text())').extract_first(),
            'Price': response.xpath('//span[contains(@id, "priceblock_ourprice")]/text()').extract_first(),
            'Type/Size': response.xpath('normalize-space(//span[contains(@class, "selection")]/text())').extract_first(),
            'Avg_rating': response.xpath('//i[contains(@data-hook,"average-star-rating")]/span[contains(@class, "a-icon-alt")]/text()').extract_first(),
            'Total_rating_no': response.xpath('//span[contains(@data-hook, "total-review-count")]/text()').extract_first(),
            'revw_link': response.xpath('(//a[contains(@data-hook, "see-all-reviews-link-foot")]/@href)').extract()

        }
