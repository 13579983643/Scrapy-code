#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author      :
# @File        : test.py
# @Software    : PyCharm
# @description : XXX


import scrapy
import os
import requests
from lxml import etree


class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]
    dont_proxy = True

    # 自定义配置。自定义配置会覆盖项目级别(即setting.py)配置
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.xiaohuar.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        },

        # 'ITEM_PIPELINES': {
        #     'maoyan.pipelines.pipelines.MainPipelineKafka': 300,
        #     # 'maoyan.pipelines.pipelines.MainPipelineSQLServer': 300,
        # },

        # 'DOWNLOADER_MIDDLEWARES': {
        #     # 'maoyan.middlewares.useragent.RandomUserAgentMiddleware': 90,
        #     # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 100,
        #     # 'maoyan.middlewares.middlewares.ZhiMaIPMiddleware': 125,
        #     'maoyan.middlewares.proxy_middlewares.ProxyMiddleware': 125,
        # },

        # 'CONCURRENT_REQUESTS': 100,
        # 'DOWNLOAD_DELAY': 0.5,
        # 'RETRY_ENABLED': False,
        # 'RETRY_TIMES': 1,
        # 'RETRY_HTTP_CODES': [500, 503, 504, 400, 403, 404, 408],

        # 'REDIRECT_ENABLED': False,  # 关掉重定向,不会重定向到新的地址
        # 'HTTPERROR_ALLOWED_CODES': [301, 302, 403],  # 返回301, 302时,按正常返回对待,可以正常写入cookie
    }

    def parse(self, response):
        current_url = response.url
        print(current_url)
        # 创建查询的 xpath 对象 (也可以使用 scrapy 中 response 中 xpath)
        # selector = etree.HTML(response.text)

        div_xpath = '//div[@class="item_t"]'
        items = response.xpath(div_xpath)

        for item in items:
            # 图片 地址
            # /d/file/20190117/07a7e6bc4639ded4972d0dc00bfc331b.jpg
            img_src = item.xpath('.//img/@src').extract_first()
            img_url = 'http://www.xiaohuar.com{0}'.format(img_src) if 'https://' not in img_src else img_src
            # 校花 名字
            mm_name = item.xpath('.//span[@class="price"]/text()').extract_first()
            # 校花 学校
            mm_school = item.xpath('.//a[@class="img_album_btn"]/text()').extract_first()
            if not os.path.exists('./img/'):
                os.mkdir('./img')
            file_name = "%s_%s.jpg" % (mm_school, mm_name)
            file_path = os.path.join("./img", file_name)
            r = requests.get(img_url)
            if r.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(r.content)
            else:
                print('status code : {0}'.format(r.status_code))

        next_page_xpath = '//div[@class="page_num"]//a[contains(text(), "下一页")]/@href'
        next_page_url = response.xpath(next_page_xpath).extract_first()
        if next_page_url:
            r_headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Host': 'www.xiaohuar.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
            }
            yield scrapy.Request(next_page_url, headers=r_headers, callback=self.parse)


def test_1():
    from scrapy import cmdline
    cmdline.execute('scrapy crawl xiaohuar'.split())


def test_2():
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    process = CrawlerProcess(get_project_settings())
    process.crawl('xiaohuar')
    process.start()


if __name__ == '__main__':
    test_1()
    #test_2()
    pass
