from bs4 import BeautifulSoup
from .config import categories_config
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
