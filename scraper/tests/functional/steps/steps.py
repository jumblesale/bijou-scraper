from behave import *
from os import path
from scraper import scrape
from scraper.model import category
from scraper.generate_data import scrape_data, scrape_single_category, categories_to_json
from hamcrest import assert_that, equal_to
import json


# the html examples directory relative to this file
examples_directory = path.join(path.dirname(__file__), '..', '..', '..', '..', 'examples/html')


@given(u'I have the example page {page}')
def step_impl(context, page):
    example = path.join(examples_directory, page)
    with open(example, 'r') as contents:
        html = contents.read()
    context.html = html


@when(u'I scrape that page for categories')
def step_impl(context):
    context.categories = scrape.get_categories_from_html(context.html)


@then(u'I get the categories')
def step_impl(context):
    expected_categories = [category.Category(row['title'], row['url']) for row in context.table]
    actual_categories = context.categories
    for (expected, actual) in zip(expected_categories, actual_categories):
        assert_that(
            actual,
            equal_to(expected),
            'Category has title "%s" and url "%s"\n'
            'but expected was title "%s" and url "%s"' %
            (actual.title, actual.url, expected.title, expected.url)
        )


@when(u'I scrape that page for product links')
def step_impl(context):
    context.product_links = scrape.get_product_links_from_category_page(context.html)


@then(u'I get the urls')
def step_impl(context):
    expected_links = [row['url'] for row in context.table]
    actual_links = context.product_links
    assert_that(actual_links, equal_to(expected_links))


@when(u'I scrape that page for product details')
def step_impl(context):
    context.product_details = scrape.get_product_details_from_product_page(context.html)


@then(u'I get the product details')
def step_impl(context):
    attributes = []
    for row in context.table:
        attributes.append((row['attribute'], row['value']))
    expected_attributes = dict(attributes)
    actual_attributes = context.product_details.__dict__
    assert_that(actual_attributes, equal_to(expected_attributes))


@when(u'I fetch all categories and associated products from the website')
def step_impl(context):
    context.categories = scrape_data()


@when(u'I fetch the first category and associated products from the website')
def step_impl(context):
    context.categories = scrape_single_category()


@when(u'I convert it to json')
def step_impl(context):
    context.json = categories_to_json(context.categories)


@then(u'I get a valid set of categories and products')
def step_impl(context):
    for category in json.loads(context.json):
        assert 'title' in category
        assert 'url' in category
        for product in category['products']:
            for attribute in ['name', 'discounted_price', 'high_price', 'item_number']:
                assert attribute in product
