from behave import *
from scraper.scraper import scrape


@given(u'I have the example page {page}')
def step_impl(context, page):
    context.page = page


@when(u'I scrape that page for categories')
def step_impl(context):
    context.categories = scrape.get_categories_from_html(context.page)


@then(u'I get the categories')
def step_impl(context):
    expected_persons = [row["title"] for row in context.table]
    print(expected_persons)
