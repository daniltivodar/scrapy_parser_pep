import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для работы с официальным сайтом документов PEP."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Метод собирает ссылки на документы PEP."""
        for pep_link in response.css('tbody tr a::attr(href)').getall():
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Метод парсит страницы документов PEP."""
        text_match = re.search(
            r'PEP (?P<number>\d*) – (?P<name>.*)',
            response.css('.page-title::text').get(),
        )
        number, name = text_match.groups()
        yield PepParseItem(
            {
                'number': number,
                'name': name,
                'status': response.css('abbr::text').get(),
            }
        )
