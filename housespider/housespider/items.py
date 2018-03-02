# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class HousespiderItem(Item):
    title = Field()
    url = Field()
    info = Field()
    loc = Field()
    loc_url = Field()
    loc_detail = Field()
    pub_time = Field()
    area = Field()
    price = Field()
    unit_price = Field()
    tags = Field()
