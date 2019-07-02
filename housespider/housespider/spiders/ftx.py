#!/usr/bin/env python
"""
Created on 27/02/2018

@author: 'Jiezhi.G@gmail.com'

Source code: https://github.com/Jiezhi/HouseSpider

Reference: 
"""
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from housespider.items import HousespiderItem, HouseDetailItem


class FangSpider(scrapy.Spider):
    name = 'ftx'
    allowed_domains = ['esf.nanjing.fang.com']

    # start_urls = ['http://esf.nanjing.fang.com/house/kw%cf%c9%c1%d6%d0%c2%b4%e5/']

    start_urls = ['http://esf.nanjing.fang.com/house/h316/']

    # def start_requests(self):
    #     all_url = ['https://nj.lianjia.com/ershoufang/pg{}/'.format(i) for i in range(1, 100)]
    #     for url in all_url:
    #         print(url)
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """
        This function parses page information.
        @url http://esf.nanjing.fang.com/house/h316/
        @returns items 1
        @scrapes title
        """
        self.logger.info('start parse %s!', response.url)
        self.logger.info('*' * 40)

        houses = response.css('dl.list')
        for fang in houses:
            item = HousespiderItem()
            item['title'] = fang.css('p.title a::text').extract_first()
            item['url'] = fang.css('p.title a::attr(href)').extract_first()
            item['info'] = fang.css('p.mt12::text').extract()
            item['loc'] = fang.css('p.mt10 span::text').extract_first()
            item['loc_url'] = fang.css('p.mt10 a::attr(href)').extract_first()
            item['loc_detail'] = fang.css('p.mt10 span.iconAdress::text').extract_first()
            item['pub_time'] = fang.css('p.gray6 span::text').extract_first()
            item['area'] = fang.css('div.area p::text').extract_first()
            item['price'] = fang.css('span.price::text').extract_first()
            item['unit_price'] = fang.css('p.danjia::text').extract_first()
            item['tags'] = fang.css('span.colorPink::text').extract()

            if item['url']:
                yield scrapy.Request('http://esf.nanjing.fang.com' + item['url'], callback=self.parse_item)
            # return

        next_page = 'http://esf.nanjing.fang.com/' + response.css('a#PageControl1_hlk_next::attr(href)').extract_first()
        yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        """
        解析房子细节
        :param response:
        :return:
        """
        l = ItemLoader(item=HouseDetailItem(), response=response)

        l.add_xpath('title', '//div[@class="floatl"]/text()', MapCompose(str.strip))
        l.add_xpath('price', '//div[@class="trl-item price_esf  sty1"]/i/text()', MapCompose(str.strip))
        l.add_xpath('room', '//div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w146"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))

        l.add_xpath('direction',
                    '//div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w146"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))

        l.add_xpath('area',
                    '//div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w182"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))
        l.add_xpath('floor',
                    '//div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w182"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))

        l.add_xpath('price',
                    '//div[@class="tr-line clearfix"][1]/div[@class="trl-item1 w132"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))
        l.add_xpath('fitment',
                    '//div[@class="tr-line clearfix"][2]/div[@class="trl-item1 w132"]/div[@class="tt"]/text()',
                    MapCompose(str.strip))

        l.add_xpath('broker', '//span[@class="zf_jjname"]/a/text()', MapCompose(str.strip))
        l.add_xpath('broker_url', '//span[@class="zf_jjname"]/a/@href', MapCompose(str.strip))
        l.add_xpath('broker_star', '//span[@class="starOrg"]/@style', MapCompose(str.strip))
        l.add_xpath('broker_company', '//div[@class="tjcont-list-cline2"]/span[2]/text()', MapCompose(str.strip))
        l.add_xpath('broker_tel', '//div[contains(@class, "tjcont-list-cline3")]/span/text()', MapCompose(str.strip))

        l.add_xpath('build_year', '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][1]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('lift', '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][2]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('property_right',
                    '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][3]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('house_catalog', '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][4]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('house_structure',
                    '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][5]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('house_material',
                    '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][6]/span[2]/text()',
                    MapCompose(str.strip))
        l.add_xpath('add_time', '//div[@class="cont clearfix"]/div[@class="text-item clearfix"][7]/span[2]/text()',
                    MapCompose(str.strip))

        l.add_value('url', response.url)
        # 暂时不考虑图片这块
        # >> > response.xpath('//div[@class="cont-sty1 clearfix"]/div/div/img/@data-src').extract()
        # ['http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/16/6e606af50b8a4141a34be41c9756e9da/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/17/b328f8795d4847fe8b1b8e50244aaf1f/452x340.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/16/793d9c77cb7e4832b60b64f89f71fb5a/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/17/73824c76a5b144af9aa922f9f088c475/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/17/c4f8ce2ca20947d6be9093e41649dba3/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/16/20ab2122fa4147358559452da2c40427/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/16/aeaa6a1f91b64e49b978464d6c62715e/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/17/06f58da67cd240cf880a730206c504d3/452x340c.jpg',
        #  'http://cdnsfb.soufunimg.com/viewimage/1/2018_2/24/M9/17/8cf96e0adcae4fb0b8afedeff6a390cc/452x340c.jpg']

        yield l.load_item()


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute('scarpy crawl 5i5j'.split())
