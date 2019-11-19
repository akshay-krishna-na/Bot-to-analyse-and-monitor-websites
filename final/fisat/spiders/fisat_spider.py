# -*- coding: utf-8 -*-
import scrapy
from ..items import FisatItem
f=open("url.txt","r")
i=f.read()

class FisatSpySpider(scrapy.Spider):
    name = 'finder'
    allowed_domains = [i]
    start_urls = ['http://'+i]

    def parse(self, response):
        data1 = response.css('a::text,p::text').extract()
        yield{'home':data1}
        links = response.css("a::attr('href')").extract()
        for l in links:
            new_url = response.urljoin(l)
            dec=input("\nDo you want to follow to next url?\n>>>")
            if dec.lower()=="yes":
                yield scrapy.Request(new_url,callback=self.parse_url)
            else:
                break

    def parse_url(self,response):
        itm=FisatItem()
        itm['data']= response.css('a::text,p::text').extract()
        yield itm
   


        
