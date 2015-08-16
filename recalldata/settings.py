# -*- coding: utf-8 -*-

# Scrapy settings for recalldata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'recalldata'

SPIDER_MODULES = ['recalldata.spiders']
NEWSPIDER_MODULE = 'recalldata.spiders'
ITEM_PIPELINES = {'recalldata.pipelines.RecalldataPipeline'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'recalldata (+http://www.yourdomain.com)'
