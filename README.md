# bijou-scraper

Scrapes a html page for categories and products

## Resources used

* https://jenisys.github.io/behave.example/tutorials was invaluable in understanding
  how to do some of the matching in behave
* http://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
  for the `__eq__` method on the Category model - is this the nicest
  way to do this?

## Dependencies

* **BeautifulSoup** for web scraping - this seemed like a lighter component than Scrapy
* **behave** for functional tests
* **pyHamcrest** for functional test matchers
