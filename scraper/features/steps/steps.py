from behave import *
import os
from scraper import scrape
from scraper.model import category
from hamcrest.library.collection.issequence_containinginanyorder \
    import contains_inanyorder
from hamcrest import assert_that


# the html examples directory relative to this file
examples_directory = os.path.join(os.path.dirname(__file__), '../../../examples/html')


@given(u'I have the example page {page}')
def step_impl(context, page):
    path = os.path.join(examples_directory, page)
    with open(path, 'r') as contents:
        html = contents.read()
    context.html = html


@when(u'I scrape that page for categories')
def step_impl(context):
    context.categories = scrape.get_categories_from_html(context.html)


@then(u'I get the categories')
def step_impl(context):
    expected_categories = [category.Category(row['title'], row['url']) for row in context.table]
    actual_categories = context.categories
    print(expected_categories)
    assert_that(contains_inanyorder(*expected_categories), actual_categories)
