import scrapy

from bookscraper.items import BookItem  

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]  
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css(".product_pod")
        for book in books:
            relative_url = book.css("h3 a::attr(href)").get()
            if "catalogue/" in relative_url:
                book_url = "https://books.toscrape.com/" + relative_url
            else:
                book_url = "https://books.toscrape.com/catalogue/" + relative_url       
            yield response.follow(book_url,callback=self.parse_book_page)
             
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page = "https://books.toscrape.com/" + next_page
            else:
                next_page = "https://books.toscrape.com/catalogue/" + next_page                
            yield response.follow(next_page,callback=self.parse)
        
    def parse_book_page(self,response):
    
        book_item = BookItem()
        table_row = response.css("table tr")
            
        book_item["title"] = response.css("h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = table_row[0].css("td::text").get()
        book_item["price_excl_tax"] = table_row[2].css("td::text").get()
        book_item["price_incl_tax"] = table_row[3].css("td::text").get()
        book_item["tax"] = table_row[4].css("td::text").get()
        book_item["availibility"] = table_row[5].css("td::text").get()
        book_item["star"] = response.css(".star-rating").attrib["class"]
        book_item["product_type"] = table_row[1].css("td::text").get()

        yield book_item 
