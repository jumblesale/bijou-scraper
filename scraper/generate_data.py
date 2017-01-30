import scraper.scrape as scrape
from scraper.config import categories_config
import scraper.retrieve_url as retrieve_url
import json
import logging


def scrape_data():
    categories = get_categories()
    for category in categories:
        category_products = get_category_products(category)
        category.products = category_products
    return categories


def get_categories():
    url = categories_config['categories_url']
    logging.info('Fetching {0}'.format(url))
    html = retrieve_url.get(url)
    categories = scrape.get_categories_from_html(html)
    return categories


def get_category_products(category):
    url = category.url
    logging.info('\tFor category {0}, fetching {1}'.format(category.title, url))
    product_links = scrape.get_product_links_from_category_page(
        retrieve_url.get(url)
    )
    products = []
    for product_link in product_links:
        products.append(get_product_details_from_product_url(product_link))
    return products


def get_product_details_from_product_url(url):
    logging.info('\t\tFetching {0}'.format(url))
    product = scrape.get_product_details_from_product_page(
        retrieve_url.get(url)
    )
    return product


def categories_to_json(categories):
    return json.dumps(categories, default=lambda o: o.__dict__)
