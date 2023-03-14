# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GbRuItem(scrapy.Item):
    user_id = scrapy.Field()
    username = scrapy.Field()
    course_name = scrapy.Field()
    _id = scrapy.Field()
