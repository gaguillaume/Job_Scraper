# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from scrapy.utils import log

from scrapy.exceptions import DropItem

#client =  MongoClient("mongodb://mongodb:27017/mongodb")

#db = client["mongodb"]

#proposals = db["Proposal"]
#
class ScraperPipeline(object):
    #on overwrite ces 2 fonctions
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://mongodb:27017/mongodb")
        db = connection["mongodb"]
        self.collection = db["Indeed"]

    def process_item(self, item, spider):

        item['job_title'] = self.clean_spaces(item['job_title'])
        if item['company']:
            item['company'] = self.clean_spaces(item['company'])
        item['location'] = self.clean_spaces(item['location'])
        item['salary'] = self.clean_spaces(item['salary'])
        item['summary'] = self.clean_spaces(item['summary'])
        valid = True
        for data in item:
            if not data:
                valid = False
        if valid:
            self.collection.insert(dict(item))

        return item

    def clean_spaces(self, string):
        if string:
            return " ".join(string.split())
"""
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Proposal added to MongoDB database!",level=log.DEBUG, spider=spider)"""
        #return item




class DuplicatesPipeline(object):
    '''
    Classe pour enlever les annonces en double.
    Ne fonctionne pas en l'état donc bien vérifier qu'elle n'est
    pas ajoutée dans le fichier settings.py, champ ITEM_PYPELINES
    '''
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['job_title'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['job_title'])
            return item
