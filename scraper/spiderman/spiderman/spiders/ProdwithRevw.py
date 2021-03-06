# -*- coding: utf-8 -*-
import scrapy


class ProdwithrevwSpider(scrapy.Spider):
     name = 'ProdwithRevw'
     allowed_domains = ['amazon.com']

     start_urls = [
         'https://www.amazon.com/Best-Sellers-Electronics-LED-LCD-TVs/zgbs/electronics/
6459737011/ref=zg_bs_pg_2?_encoding=UTF8&pg={}'.format(i) for i in range(1, 3)]


     def parse(self, response):

         urls = response.xpath('(//li[contains(@class,"zg-item-immersion")]/span/div/sp
an/a[contains(@class,"a-link-normal")]/@href)').extract()
         for url in urls:
             url = response.urljoin(url)
             yield scrapy.Request(url=url, callback=self.prod_details)


     def prod_details(self, response):
         item = {
             'Product': response.xpath('normalize-space(//h1[contains(@id,"title")]/spa
n/text())').extract_first(),
             'Price': response.xpath('//span[contains(@id, "priceblock_ourprice")]/text
()').extract_first(),
             'Type/Size': response.xpath('normalize-space(//span[contains(@class, "sele
ction")]/text())').extract_first(),
             'Avg_rating': response.xpath('//i[contains(@data-hook,"average-star-rating
")]/span[contains(@class, "a-icon-alt")]/text()').extract_first(),
             'Total_rating_no': response.xpath('//span[contains(@data-hook, "total-revi
ew-count")]/text()').extract_first(),
revw_link = response.xpath('(//a[contains(@data-hook, "see-all-reviews-link-fo
ot")]/@href)').extract()

         yield scrapy.Request(
             response.urljoin(revw_link),
             dont_filter=True,
             meta = {'item' : item },
             callback= self.revw_details
             )



     def revw_details(self, response):
         item = response.meta.get('item', {})
         for revw in response.xpath('//div[contains(@data-hook,"review")]'):

             item['review_detail']= {
                 'author':revw.xpath('.//a[contains(@data-hook, "review-author")]/text(
)').extract_first(),
                 'title':revw.xpath('.//a[contains(@data-hook, "review-title")]/text()'
).extract_first(),
                 'rating':revw.xpath('.//i[contains(@data-hook, "review-star-rating")]/
span[contains(@class,"a-icon-alt")]/text()').extract_first(),
                 'date':revw.xpath('.//span[contains(@data-hook, "review-date")]/text()
').extract_first(),
                 'helpful_to':revw.xpath('.//span[contains(@data-hook, "helpful-vote-st
atement")]/text()').extract_first(),
                 'content':revw.xpath('.//span[contains(@data-hook, "review-body")]/tex
t()').extract_first(),
                 'verification':revw.xpath('.//span[contains(@data-hook, "avp-badge")]/
text()').extract_first(),
                 'product_type':revw.xpath('.//span[contains(@data-hook, "cr-widget-Asi
nVariation")]/text()').extract_first(),
 }
             yield item
