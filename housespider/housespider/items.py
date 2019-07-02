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
    direction = Field()
    floor = Field()
    fitment = Field()
    broker = Field()
    broker_url = Field()
    broker_star = Field()
    broker_company = Field()
    broker_tel = Field()

    url = Field()

    # House info
    build_year = Field()
    lift = Field()
    property_right = Field()
    house_catalog = Field()
    house_structure = Field()
    house_material = Field()
    add_time = Field()


class House5i5jItem(Item):
    title = Field()  # 标题
    tag = Field()  # 标签
    id = Field()  # 编号
    price = Field()  # 总价
    unit_price = Field()  # 单价
    house_type = Field()  # 户型
    area = Field()  # 面积
    # loc = Field()  # 小区
    floor = Field()  # 楼层
    direction = Field()  # 朝向
    fitment = Field()  # 装修
    usage = Field()  # 规划用途
    year = Field()  # 年代
    structure = Field()  # 建筑类型
    visit_time = Field()  # 看房时间
    metro = Field()  # 地铁
    property_right = Field()  # 产权
    list_time = Field()  # 挂牌时间

    # 小区信息
    community = Field()  # 小区
    mean_price = Field()  # 均价
    build_year = Field()  # 建筑年代
    total_houses = Field()  # 总户数
    district = Field()  # 商圈
    wuye = Field()  # 物业
    on_sale = Field()  # 在售房源
    on_rent = Field()  # 在租房源

    url = Field()
