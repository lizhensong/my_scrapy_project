# -*- coding: utf-8 -*-
import scrapy
from my_scrapy_project.items import MyScrapyProjectItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        items = MyScrapyProjectItem()
        items['title'] = response.xpath('//*[@id="u1"]/a[1]/text()').extract_first()
        items['url'] = response.xpath('//*[@id="u1"]/a[1]/@href').extract()[0]
        print(i for i in items)
        return items
