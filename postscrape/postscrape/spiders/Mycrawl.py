import scrapy
from scrapy import Request
import string
from scrapy.crawler import CrawlerProcess


class AdviceSpider(scrapy.Spider):

    name = "advice"
    
    allowed_domains = ['www.advice.co.th']
    start_urls = ['https://www.advice.co.th/product/notebooks' ]
    

    def parse(self, response):

        price = response.css('div.sale-font::text').extract()
        name = response.css('div.product-name-font::text').extract()
        img = response.css('img.img-fluid').xpath('@src').extract()
        link = response.css('div.product-content-font a::attr(href)').extract()
            
        for item in zip(price,name,img,link):
            scraped_info = {
                
                'price' : item[0],
                'name' : item[1],
                'img' : item[2],
                'link' : item[3]
                 
            }
            yield scraped_info

            

        #next_page = response.css('a.line-35::attr("href")').extract()
        #for next_page in next_page:
            #yield Request(response.urljoin(next_page), callback=self.parse)
            
        
        #response.xpath("//li[@class='menu-link']/a/@href").extract()

class JibSpider(scrapy.Spider):

    name = "jib"
    
    page_number = 2
    allowed_domains = ['www.jib.co.th']
    start_urls = ['https://www.jib.co.th/web/product/product_list/1/24' ]
    
    

    def parse(self, response):

        response.selector.remove_namespaces()

        #for sel in response.xpath("//div[@class='col-md-3 col-sm-4 col-xs-6 divboxpro']"):

        price = response.xpath("//p[@class='price_total']/text()").extract()
        name = response.xpath("//span[@class='promo_name']/text()").extract()
        img = response.xpath("//img[@class='img-responsive imgpspecial']/@src").extract()
        link = response.xpath("//div[@class='row']/a/@href").extract()


        for item in zip(price,name,img,link):
            scraped_info = {
                
                'price' : item[0],
                'name' : item[1],
                'img' : item[2],
                'link' : item[3]
                
            }
            yield scraped_info
            
            #
        next_page = response.css('li.page a::attr("href")').extract()
        for next_page in next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)


process = CrawlerProcess({
'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
'FEED_FORMAT': 'json',
'FEED_URI': 'tmp/Crawl.json'
})
process.crawl(AdviceSpider)
process.crawl(JibSpider)
process.start()