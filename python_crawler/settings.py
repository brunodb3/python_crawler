# -*- coding: utf-8 -*-

# Scrapy settings for python_crawler project

# common settings, consult the documentation if you want to know more:
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
BOT_NAME = 'python_crawler'
DOWNLOAD_DELAY = 1 # delay for any downloads/requests (seconds)
ROBOTSTXT_OBEY = True # obey robots.txt rules
CONCURRENT_REQUESTS = 4 # maximum concurrent requests performed (default: 16)
SPIDER_MODULES = ['python_crawler.spiders']
NEWSPIDER_MODULE = 'python_crawler.spiders'
# USER_AGENT is how the crawler is going to 'disguise' itself to the website
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'
# pipelines to use
ITEM_PIPELINES = {
    'python_crawler.pipelines.JsonExportPipeline': 300
}