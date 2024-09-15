# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nameWeb = scrapy.Field()
    url = scrapy.Field()
    modification_date = scrapy.Field()
    size = scrapy.Field()

