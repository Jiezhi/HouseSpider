#!/usr/bin/env python
"""
Created on 27/02/2018

@author: 'Jiezhi.G@gmail.com'

Source code: https://github.com/Jiezhi/HouseSpider

Reference: 
"""
import scrapy


class FangtxSpider(scrapy.Spider):
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
            yield {
                'title': fang.css('p.title a::text').extract_first(),
                # '仁恒G53精装三房出售 新城区 全新未住过'
                'url': fang.css('p.title a::attr(href)').extract_first(),
                # '/chushou/3_165865397.htm'
                'info': fang.css('p.mt12::text').extract(),
                # '<p class="mt12">\r\n
                # 3室2厅\r\n                            \r\n
                # <span class="line">|</span>中层(共18层)\r\n
                # <span class="line">|</span>南北向\r\n
                # <span class="line">|</span>建筑年代：2011\r\n </p>'
                'loc': fang.css('p.mt10 span::text').extract_first(),
                # '仁恒G53公寓'
                'loc_url': fang.css('p.mt10 a::attr(href)').extract_first(),
                # '/house-xm1810860322/'
                'loc_detail': fang.css('p.mt10 span.iconAdress::text').extract_first(),
                # '奥体-建邺区嵩山路136号'
                'pub_time': fang.css('p.gray6 span::text').extract_first(),
                # '49秒前发布'
                'area': fang.css('div.area p::text').extract_first(),
                # '100㎡'
                'price': fang.css('span.price::text').extract_first(),
                # '550'
                'unit_price': fang.css('p.danjia::text').extract_first(),
                # '55000元'
                'tags': fang.css('span.colorPink::text').extract(),
                # ['优质教育']
            }

        next_page = 'http://esf.nanjing.fang.com/' + response.css('a#PageControl1_hlk_next::attr(href)').extract_first()
        yield scrapy.Request(next_page, callback=self.parse)
