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


class HouseDetailItem(Item):
    # Basic
    title = Field()
    price = Field()
    room = Field()
    area = Field()
    price = Field()
    direction = Field()
    floor = Field()
    fitment = Field()
    broker = Field()
    broker_url = Field()
    broker_star = Field()
    broker_company = Field()
    broker_tel = Field()

    # House info
    build_year = Field()
    lift = Field()
    property_right = Field()
    house_catalog = Field()
    house_structure = Field()
    house_material = Field()
    add_time = Field()
