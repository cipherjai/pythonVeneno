# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonproductsItem(scrapy.Item):
        # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_size_type = scrapy.Field()
    product_avgrating = scrapy.Field()
    product_rating_no = scrapy.Field()
    revw_author = scrapy.Field()
    revw_title = scrapy.Field()
    revw_rating = scrapy.Field()
    revw_date = scrapy.Field()
    revw_helpfullness = scrapy.Field()
    revw_varification = scrapy.Field()
    revw_content = scrapy.Field()
    revw_product_type = scrapy.Field()

