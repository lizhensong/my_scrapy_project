# usr\bin\python3
# -*-coding:utf-8-*-

__author__ = 'wolf li'

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    # 爬虫名称
    process.crawl('baidu')
    process.start()
