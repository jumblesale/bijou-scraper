# bijou-scraper

Scrapes a html page for categories and products

## Testing

Testing is done with Python unit tests and also `behave` cucumber-style tests.
You can run all tests at once with `make tests`.

### Unit tests

To run the unit test suite, use `nosetests`:

`nosetests -v scraper/tests/unit/`

The only module with tests is the `scrape` module as this is the only one which
is not responsible for interfacing with a dependency and so does some business
logic which is testable in isolation. All other parts of the codebase are covered
by functional tests.

Given more time, tests could be applied to the `parse_html` module, passing in
faked chunks of html to test the outcome of parsing it. However this would mean
doubling the work required every time the remote website updated.

### Functional tests

Functional tests are run in `behave`. You can invoke them like:

`behave scraper/tests/functional/`

There are two tags: `@local` and `@remote`. Only `@remote` tests will make a call
to the live site. To verify everything is working internally, calling the `@local`
tests will use stored html as fixtures for testing.

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
  for the `__eq__` method on the `Category` and `Product`` model - is this the nicest
  way to do this?

## Dependencies

* **BeautifulSoup** for web scraping - this seemed like a lighter component than Scrapy
* **behave** for functional tests
* **pyHamcrest** for functional test matchers
* **request** for retrieving pages from the site
