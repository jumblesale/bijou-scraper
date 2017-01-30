from behave import *
from os import path
from scraper import scrape
from scraper.model import category
from hamcrest import assert_that, equal_to


# the html examples directory relative to this file
examples_directory = path.join(path.dirname(__file__), '../../../../examples/html')


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
