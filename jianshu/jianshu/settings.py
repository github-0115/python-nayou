# Scrapy settings for jianshu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'jianshu'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['jianshu.spiders']
NEWSPIDER_MODULE = 'jianshu.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
# FEED_URI=u'/Users/apple/Documents/jianshu-hot.csv'
# FEED_FORMAT='CSV'
