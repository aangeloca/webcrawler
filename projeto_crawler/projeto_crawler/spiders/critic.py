# -*- coding: utf-8 -*-
import scrapy


class CriticSpider(scrapy.Spider):
    name = 'critic'
    allowed_domains = ['metacritic.com/game']
    start_urls = ['https://www.metacritic.com/game']

    def parse(self, response):
        for critic in response.css('tr'):
            yield {
                'titulo': critic.css('h3::text').get(),
                'descricao': critic.css('div.summary::text').get(),                
            }