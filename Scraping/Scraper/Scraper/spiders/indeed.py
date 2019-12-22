# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy import Request

from Scraper.items import ScraperItem

what = "Informatique"
where = "Paris"

class IndeedSpider(CrawlSpider):
    name = 'indeed'
    allowed_domains = ['indeed.fr']
    start_urls = [
        f"http://www.indeed.fr/jobs?q={what}&l={where}&sort=date&start=00",
    ]

    def parse(self, response):
        self.log('\n\n Crawling  %s\n' % response.url)
        for annonce in response.css('.row '):
            job_title = self.clean_spaces( annonce.css('.jobtitle::attr(title)').get() )
            location = self.clean_spaces( annonce.css('.location::text').get() )
            # company = self.clean_spaces( annonce.css('.company::text').get() )
            summary = self.clean_spaces( annonce.css('.summary li::text').get() )
            salary = self.clean_spaces( annonce.css('.salaryText::text').get() )
            link_url = annonce.css('.jobtitle::attr(href)').get()
            crawl_url = response.url

            # Not all entries have a company
            if self.clean_spaces( annonce.css('.company::text').get() ) == '' :
                company = None
            else:
                company = self.clean_spaces( annonce.css('.company::text').get() )
            
            yield {
				'job' : job_title,
				'company' : company,
				'location' : location,
				'salary' : salary,
				'summary' : summary,
				'link' : link_url,
				'crawl_url' : crawl_url
			}
        
        next_page = ''.join(["http://www.indeed.fr", response.css('.pagination a::attr(href)').getall()[-1]])
        yield Request(next_page)

    def clean_spaces(self, string):
        if string: 
            return " ".join(string.split())
