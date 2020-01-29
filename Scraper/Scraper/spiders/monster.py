import scrapy
from scrapy.spiders import CrawlSpider

from Scraper.items import ScraperItem

class MonsterSpider(CrawlSpider):
    name = 'monster'
    allowed_domains = ['monster.fr']
    start_urls = [
        # On scrappe les 5 premieres pages grace à 'page=5'
        "https://www.monster.fr/emploi/recherche/?q=Informatique&where=Paris&page=5",
    ]

    def parse(self, response):
        self.log('\n\n Crawling  %s\n' % response.url)

        for annonce in response.css('#SearchResults .card-content'):
            job_title = annonce.css('.title a::text').get()
            location = annonce.css('div .location .name::text').get()
            # summary = annonce.get()
            #Si on veut ajouter les dates
            # date = annonce.css('time::text').get()
            # salary = None
            link_url = annonce.css('.title a::attr(href)').get()
            crawl_url = response.url

            # Not all entries have a company
            if annonce.css('div .company .name::text').get() == '':
                company = None
            else:
                company = annonce.css('div .company .name::text').get()

            yield ScraperItem(
                site = 'Monster',
                job_title = job_title,
                company = company,
                location = location,
                link_url = link_url,
                crawl_url = crawl_url
            )

