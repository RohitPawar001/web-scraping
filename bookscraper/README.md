<h1>scraping bookstoscrape.com</h1>


## Files in a Scrapy Project
1. **`scrapy.cfg`**:
    Configuration file for Scrapy settings.
2. **`myproject/` (Project Folder)**:
   - **`__init__.py`**:
      Empty file to mark the folder as a Python package.
   - **`items.py`**:
       Define data structures (items) to hold scraped data.
   - **`middlewares.py`**:
       Custom middleware components. i.e to add the fake user agents and fake broaser agents so as to the website should not block us
   - **`pipelines.py`**:
       Define item processing pipelines. pipelines are used to organize the data
   - **`settings.py`**:
       Scrapy project settings enable or disable user-agent, pipelines, etc. .
   - **`spiders/` (Folder)**:
     - **`__init__.py`**:
        Empty file to mark the folder as a Python package.
     - **`my_spider.py`**:
        Your custom spider(s) for scraping specific websites.

## To run scraper  
 enter the following commands on the terminal
  - cd bookscraper
   - scrapy crawl bookspider 

