# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
# from housespider.items import House5i5jItem
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule


class A5i5jSpider(CrawlSpider):
    name = '5i5j'
    allowed_domains = ['nj.5i5j.com']
    start_urls = ['https://nj.5i5j.com/ershoufang/_%E6%97%AD%E6%97%A5%E4%B8%8A%E5%9F%8E%E4%B8%89%E6%9C%9F/']

    def parse(self, response):
        self.logger.info('start parse %s!', response.url)
        self.logger.info('*' * 40)
        print(response.xpath('//h3[@class="listTit"]'))

        items = response.xpath('//h3[@class="listTit"]')
        for item in items:
            url = item.xpath('a/@href').extract_first()
            yield scrapy.Request(urljoin(response.url, url), callback=self.parse_item)

        next_page = response.xpath('//a[@class="cPage"]/@href/text()')
        yield scrapy.Request(urljoin(response.url, next_page), callback=self.parse)

    def parse_item(self, response):
        """
        :param response:
        :return:
        """
        print(response.url)
        from housespider.housespider.items import House5i5jItem
        loader = ItemLoader(item=House5i5jItem(), response=response)
        loader.add_xpath('title', '//h1[@class="house-tit"]/text()')
        loader.add_xpath('tag', '///div[@class="rent-top fl"]/p/text()')
        loader.add_xpath('id', '///div[@class="rent-top fl"]/p/text()', re='[0-9]+')
        loader.add_xpath('price', '//div[@class="jlquannei fontbaise"]//p[@class="jlinfo"]/text()')
        loader.add_xpath('unit_price', '//div[@class="jlyoubai fl"][1]/div/p[1]/text()')
        # loader.add_xpath('house_type', '//div[@class="jlyoubai fl"][2]/div/p[1]/text()')
        loader.add_xpath('area', '//div[@class="jlyoubai fl"][3]/div/p[1]/text()')
        # loader.add_xpath('community', '//div[@class="zushous"]/ul/li/a/text()')
        loader.add_xpath('floor', '//div[@class="zushous"]/ul/li[2]/text()')
        loader.add_xpath('direction', '//div[@class="zushous"]/ul/li[3]/text()')
        loader.add_xpath('fitment', '//div[@class="zushous"]/ul/li[4]/text()')
        loader.add_xpath('usage', '//div[@class="zushous"]/ul/li[5]/text()')
        loader.add_xpath('year', '//div[@class="zushous"]/ul/li[6]/text()')
        loader.add_xpath('structure', '//div[@class="zushous"]/ul/li[7]/text()')
        # loader.add_xpath('district', '//div[@class="zushous"]/ul/li/text()'[7])
        loader.add_xpath('visit_time', '//div[@class="zushous"]/ul/li[9]/text()')
        loader.add_xpath('metro', '//div[@class="zushous"]/ul/li[10]/text()')
        loader.add_xpath('house_type', '//div[@class="infocon fl"]/ul/li[1]/span/text()')
        loader.add_xpath('property_right', '//div[@class="infocon fl"]/ul/li[4]/span/text()')
        loader.add_xpath('list_time', '//div[@class="infocon fl"]/ul/li[5]/span/text()')

        loader.add_xpath('community', '//a[@class="infotit"]/text()')
        loader.add_xpath('mean_price', '//div[@class="infomain fl"]/ul/li/label/text()', re='[0-9]+')
        loader.add_xpath('build_year', '//div[@class="infomain fl"]/ul/li[2]/text()')
        loader.add_xpath('total_houses', '//div[@class="infomain fl"]/ul/li[3]/text()')
        loader.add_xpath('district', '//div[@class="infomain fl"]/ul/li[4]/text()')
        loader.add_xpath('wuye', '//div[@class="infomain fl"]/ul/li[5]/text()')
        loader.add_xpath('on_sale', '//div[@class="infomain fl"]/ul/li[6]/a/text()', re='[0-9]+')
        loader.add_xpath('on_rent', '//div[@class="infomain fl"]/ul/li[7]/a/text()', re='[0-9]+')

        loader.add_value('url', response.url)

        yield loader.load_item()


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute('scarpy crawl 5i5j'.split(), settings='../settings.py')
