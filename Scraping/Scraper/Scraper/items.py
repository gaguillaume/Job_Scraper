# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ScraperItem(Item):
    job_title = Field()
    company = Field()
    location = Field()
    salary = Field()
    summary = Field()
    link_url = Field()
    crawl_url = Field()
