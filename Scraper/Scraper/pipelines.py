# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy

from scrapy.exceptions import DropItem
from elasticsearch import Elasticsearch




#client =  MongoClient("mongodb://mongodb:27017/mongodb")

#db = client["mongodb"]

#proposals = db["Proposal"]

class ScraperPipeline(object):
    #on overwrite ces 2 fonctions
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://mongodb:27017/mongodb")
        db = connection["mongodb"]
        self.collection = db["Indeed"]
        connection2 = Elasticsearch([{'host':'elasticsearch','port':9200}])
        self.collection2 = connection2

    def process_item(self, item, spider):
        if 'job_title' in item and item['job_title']:
            item['job_title'] = self.clean_spaces(item['job_title'])
        if 'company' in item and item['company']:
            item['company'] = self.clean_spaces(item['company'])
        if 'location' in item and item['location']:
            item['location'] = self.clean_spaces(item['location'])
        if 'salary' in item and item['salary']:
            item['salary'] = self.clean_spaces(item['salary'])
        if 'summary' in item and item['summary']:
            item['summary'] = self.clean_spaces(item['summary'])
        valid = True
        for data in item:
            if not data or item['summary'] in self.collection.find({},{"site":0,"job_title":0,"company":0,"location":0,"salary":0,"link_url":0,"crawl_url":0}):
                valid = False
        if valid:
            self.collection.insert(dict(item))
            self.collection2.index(index='annonces',doc_type='ann',body=dict(item))

        return item

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())
