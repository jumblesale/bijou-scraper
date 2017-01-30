from bs4 import BeautifulSoup
from .config import categories_config
from .config import product_config
from functools import partial


bs_parser = partial(BeautifulSoup, features='html.parser')


def parse_categories(html):
    """
    Given a html page containing a list of categories, produce a list of category names and urls
    :param html: the html of the page
    :return: a list of objects with url and title set
    """
    parsed = bs_parser(html)
    categories = []
    for li in parsed.find(id=categories_config['category_container_identifier']).findAll('li'):
        a = li.findAll('a')[0]
        href = a.get('href')
        title = a.string
        categories.append({'title': title, 'url': href})
    return categories


def parse_product_links_from_category_page(html):
    """
    Given a html page representing a category, extract the links to the products from it
    :param html: the html page
    :return: a list of url strings
    """
    links = []
    parsed = bs_parser(html)\
        .find(id=categories_config['category_page_products_container'])\
        .findAll(
            'div',
            {'class': categories_config['category_page_product_link_container']}
        )
    for link_container in parsed:
        for a in link_container.findAll('a'):
            links.append(a.get('href'))
    return links


def parse_product_details(html):
    """
    Given a html page representing product details, extract the indvidual details into a hash
    :param html: the product page
    :return: a hash of product details
    """
    parsed = bs_parser(html)\
        .find(id=product_config['product_details_container'])

    price_div = parsed.findAll('div', {'class': 'price'})[0]

    prices = extract_prices_from_product_details_div(price_div)
    name = parsed.find('h1', {'class': 'productname'}).string
    item_number = parsed.find('span', {'itemprop': 'productID'}).string

    return {
        'name': name,
        'discounted_price': format_price(prices['discounted_price']),
        'high_price': format_price(prices['high_price']),
        'item_number': item_number
    }


def extract_prices_from_product_details_div(price_div):
    """
    Prices appear in three formats: no discount, discounted and price range
    Try to parse all of them based on what markup is present
    :param price_div: the portion of html representing the price <div>
    :return: a hash with keys for discounted_price and high_price
    """
    prices = {}
    # check for a discounted price
    discounted_price = price_div.find('div', {'class': 'lowPrice'})
    if discounted_price is not None:
        prices['discounted_price'] = discounted_price.string
        prices['high_price'] = price_div.find('div', {'class': 'standardprice'}).string
        return prices
    # check for price range
    price_range_low_price = price_div.find('span', {'itemprop': 'lowPrice'})
    if price_range_low_price is not None:
        prices['discounted_price'] = price_range_low_price.string
        prices['high_price'] = price_div.find('span', {'itemprop': 'highPrice'}).string
        return prices
    prices['discounted_price'] = ''
    prices['high_price'] = price_div.find('div', {'class': 'salesprice'}).string
    return prices


def format_price(price):
    return price.strip('\n')
