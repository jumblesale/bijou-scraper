# bijou-scraper

Scrapes a html page for categories and products

## Improvements
* Get the details property of a product.
* The `parse_html` methods are terribly unsafe! These should be wrapped with some `try` blocks
  and should do something sensible on error - this indicates the page structure has changed.
* Image URL - this seems to be being produced by JavaScript. The scraper could try
  to figure out the relationship between a product and a product image?

## Resources used

* https://jenisys.github.io/behave.example/tutorials was invaluable in understanding
  how to do some of the matching in behave.
* http://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
  for the `__eq__` method on the Category model - is this the nicest
  way to do this?

## Dependencies

* **BeautifulSoup** for web scraping - this seemed like a lighter component than Scrapy
* **behave** for functional tests
* **pyHamcrest** for functional test matchers
