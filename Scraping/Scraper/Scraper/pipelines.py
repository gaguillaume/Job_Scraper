# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class ScraperPipeline(object):
    def process_item(self, item, spider):
        item['job_title'] = self.clean_spaces(item['job_title'])
        if item['company']:
            item['company'] = self.clean_spaces(item['company'])
        item['location'] = self.clean_spaces(item['location'])
        item['salary'] = self.clean_spaces(item['salary'])
        item['summary'] = self.clean_spaces(item['summary'])
        
        return item

    def clean_spaces(self, string):
        if string: 
            return " ".join(string.split())


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
