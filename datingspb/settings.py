# Scrapy settings for datingspb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'datingspb'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['datingspb.spiders']
NEWSPIDER_MODULE = 'datingspb.spiders'
DEFAULT_ITEM_CLASS = 'datingspb.items.DatingspbItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOAD_DELAY = 0.5
