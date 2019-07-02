#!/usr/bin/env python
"""
Created on 27/02/2018

@author: 'Jiezhi.G@gmail.com'

Source code: https://github.com/Jiezhi/HouseSpider

Reference: 
"""
import scrapy
import re


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'

    allowed_domains = ['lianjia.com']

    start_urls = ['https://nj.lianjia.com/ershoufang/pg1co32/']

    # def start_requests(self):
    #     all_url = ['https://nj.lianjia.com/ershoufang/pg{}/'.format(i) for i in range(1, 100)]
    #     for url in all_url:
    #         print(url)
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info('start parse %s!', response.url)
        self.logger.info('*' * 40)
        houses = response.css('li.clear')
        for house in houses:
            # print(house)
            yield {
                'title': house.css('div.title a::text').extract_first(),
                'houseLoc': house.css('div.houseInfo a::text').extract_first(),
                'houseInfo': house.css('div.houseInfo::text').extract_first(),
                'housePosition': house.css('div.positionInfo::text').extract_first(),
                'housePositionInfo': house.css('div.positionInfo a::text').extract_first(),
                'houseFollowInfo': house.css('div.followInfo::text').extract_first(),
                'houseSubway': house.css('div.tag span.subway::text').extract_first(),
                # '距离3号线柳洲东路站1138米'
                'houseTaxfree': house.css('div.tag span.taxfree::text').extract_first(),
                # '房本满五年'
                'houseHaskey': house.css('div.tag span.haskey::text').extract_first(),
                # '随时看房'
                'houseTotalPrice': house.css('div.totalPrice span::text').extract_first(),
                # '192'
                'housePriceUnit': house.css('div.totalPrice::text').extract_first(),
                # '万'
                'houseUnitPrice': house.css('div.unitPrice span::text').extract_first(),
                # '单价21896元/平米'
                'houseUrl': house.css('div.title a::attr(href)').extract_first(),
                # 'https://nj.lianjia.com/ershoufang/103102037187.html'
            }

        # for url in response.xpath('//a/@href').extract():
        #     print(url)
        #     yield scrapy.Request(url, callback=self.parse)

        next_page_info = response.css('div[class="page-box fr"]').css('div::attr(page-data)').extract_first()
        next_page_info = re.findall('\d+', next_page_info)
        next_page = 'https://nj.lianjia.com/ershoufang/pg{page}co32'.format(page=str(int(next_page_info[1]) + 1))
        yield scrapy.Request(next_page, callback=self.parse)
