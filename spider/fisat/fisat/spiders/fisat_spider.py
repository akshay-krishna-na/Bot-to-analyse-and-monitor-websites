# -*- coding: utf-8 -*-
import scrapy
from ..items import FisatItem


class FisatSpySpider(scrapy.Spider):
    name = 'fisat'
    allowed_domains = ['www.fisat.ac.in']
    start_urls = ['http://www.fisat.ac.in']

    #def __init__(self):
     #   self.allowed_domains.append(line)
      #  self.start_urls.append('http://%s' % line)

    def parse(self, response):
        data1 = response.css('a::text,p::text').extract()
        yield{'home':data1}
        links = response.css("a::attr('href')").extract()
        for l in links:
            new_url = response.urljoin(l)
            yield scrapy.Request(new_url,callback=self.parse_url)

    def parse_url(self,response):
        itm=FisatItem()
        itm['data']= response.css('a::text,p::text').extract()
        yield itm

        
