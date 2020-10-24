# -*- coding: utf-8 -*-
import scrapy

class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            countryName = row.xpath(".//td[1]/a/text()").get()
            gdpRatio = row.xpath(".//td[2]/text()").get()
            
            yield {
                'country_name' : countryName,
                'gdp_debt' : gdpRatio
            }
