#!/usr/bin/env python
"""
Created on 27/02/2018

@author: 'Jiezhi.G@gmail.com'

Source code: https://github.com/Jiezhi/HouseSpider

Reference: 
"""
import scrapy
from housespider.housespider.items import HousespiderItem


class FangSpider(scrapy.Spider):
    name = 'FangTX'
    allowed_domains = ['esf.nanjing.fang.com']

    start_urls = ['http://esf.nanjing.fang.com/house/h316/']

    # def start_requests(self):
    #     all_url = ['https://nj.lianjia.com/ershoufang/pg{}/'.format(i) for i in range(1, 100)]
    #     for url in all_url:
    #         print(url)
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info('start parse %s!', response.url)
        self.logger.info('*' * 40)

        houses = response.css('dl.list')
        for fang in houses:
            # print(house)
            item = HousespiderItem()
            item.title = fang.css('p.title a::text').extract_first()
            item.url = fang.css('p.title a::attr(href)').extract_first()
            item['info'] = fang.css('p.mt12::text').extract()
            item['loc'] = fang.css('p.mt10 span::text').extract_first()
            item['loc_url'] = fang.css('p.mt10 a::attr(href)').extract_first()
            item['loc_detail'] = fang.css('p.mt10 span.iconAdress::text').extract_first()
            item['pub_time'] = fang.css('p.gray6 span::text').extract_first()
            item['area'] = fang.css('div.area p::text').extract_first()
            item['price'] = fang.css('span.price::text').extract_first()
            item['unit_price'] = fang.css('p.danjia::text').extract_first()
            item['tags'] = fang.css('span.colorPink::text').extract()

            yield item

        next_page = 'http://esf.nanjing.fang.com/' + response.css('a#PageControl1_hlk_next::attr(href)').extract_first()
        yield scrapy.Request(next_page, callback=self.parse)
