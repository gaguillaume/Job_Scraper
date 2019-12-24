# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy import Request
from scrapy.utils.markup import replace_escape_chars, remove_tags

from Scraper.items import ScraperItem

what = "Informatique"
where = "Paris"

class IndeedSpider(CrawlSpider):
    name = 'indeed2'
    allowed_domains = ['indeed.fr']
    start_urls = [
        "https://www.indeed.fr/jobs?q=Informatique&l=Paris&sort=date&start=00",
    ]

    def parse(self, response):
        self.log('\n\n Crawling  %s\n' % response.url)

        for annonce in response.css('.row '):
            job_title = annonce.css('.jobtitle::attr(title)').get()
            location = annonce.css('.location::text').get()
            summary = annonce.css('.summary li::text').get()
            salary = annonce.css('.salaryText::text').get()
            link_url = annonce.css('.jobtitle::attr(href)').get()
            crawl_url = response.url

            # Not all entries have a company
            if annonce.css('.company::text').get() == '':
                company = None
            else:
                company = annonce.css('.company::text').get()

            yield ScraperItem(
                job_title = job_title,
                company = company,
                location = location,
                salary = salary,
                summary = summary,
                link_url = link_url,
                crawl_url = crawl_url
            )

        next_page = ''.join(["https://www.indeed.fr", response.css('.pagination a::attr(href)').getall()[-1]])
        yield Request(next_page)
