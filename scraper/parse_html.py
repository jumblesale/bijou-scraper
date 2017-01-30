from bs4 import BeautifulSoup
from .config import categories_config


def parse_categories(html):
    """
    Given a html page containing a list of categories, produce a list of category names and urls
    :param html: the html of the page
    :return: a list of objects with url and title set
    """
    parsed = BeautifulSoup(html, 'html.parser')
    categories = []
    for li in parsed.find(id=categories_config["categories_url"]).findAll('li'):
        a = li.findAll('a')[0]
        href = a.get('href')
        title = a.string
        categories.append({'title': title, 'url': href})
    return categories
