# bijou-scraper

Scrapes a html page for categories and products.

## Requirements

* Python 3
* An internet connection for the `@remote` tests

## Building

Clone this repo then:

```
# create a virtual environment
python3 -m venv venv
# activate venv
source venv/bin/activate.sh
# install requirements
pip install -r requirements.txt
```

Now you can generate a JSON dump of the website by running:

`./job.py`

This will take a few minutes as it has to go and fetch the website. If you
 don't have time for that then there's some example output in `examples/output`
 organised by the date it was produced.

## Structure

The main aim of this project was to be as light-weight as possible. I've therefore
 avoiding using lots of classes and instead just created modules which provide
 functions to work on data. Classes are used for the two models - `Category` and
 `Product` but are just POPOs which do not implement any functionality.


The project is necessarily brittle as it relies on an external data source which
 it has no control over. I've tried to keep everything which is coupled to the remote
 page structure in `parse_html.py` and `config.py`. If something changes on the remote end
 this is easily discoverable by running the functional tests. If it's a simple change
 such as a required container getting a new class or id, only `config.py` will have
 to be updated. If it is a more complex change to the page structure, `parse_html.py`
 will need to be updated.

## Testing

Testing is done with Python unit tests and also `behave` cucumber-style tests.
 You can run all tests at once with `make tests`. Using the Makefile will only
 run local tests so this should be fast.

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

To run just the local tests you can use `behave --tags=local scraper/tests/functional/`

## Improvements
* Get the details property of a product.
* Product image URL - this seems to be being produced by JavaScript. The scraper could try
  to figure out the relationship between a product and a product image?
* The `parse_html` methods are terribly unsafe! These should be wrapped with some `try` blocks
  and should do something sensible on error - this indicates the page structure has changed.
* This won't work if there are > 60 items in a single category! Is there a page
  that lists the products without setting a maximum number of items bein required?
* It would be great to see some progress when you run `job.py` - this would
  require the scraping to provide some indication of how many categories it
  has processed / how many it has to fetch in total. Using the logger for this
  and allowing the job to redirect its result to a file could be another approach.
* This should handle price ranges better - at the moment it is just setting a low
  and high price. It would be better to model the three different types of price:
  full price / discounted, price range and standard price.
* Reading [this](http://www.smashcompany.com/technology/object-oriented-programming-is-an-expensive-disaster-which-must-end)
  made me think about the ceremony of creating classes and that perhaps the
  models used could belong in a single file like `models.py` rather than
  spread out like they are now. This maybe feels like a more pythonic approach?

## Resources used

* https://jenisys.github.io/behave.example/tutorials was invaluable in understanding
  how to do some of the matching in behave.
* http://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
  for the `__eq__` method on the `Category` and `Product` model - is this the nicest / most pythonic
  way to do this?

## Dependencies

* **BeautifulSoup** for web scraping - this seemed like a lighter component than Scrapy
* **behave** for functional tests
* **pyHamcrest** for functional test matchers
* **requests** for retrieving pages from the site
