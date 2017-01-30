from bs4 import BeautifulSoup
from scraper.model import category


def get_categories_from_html(html):
    categories = []
    parsed = BeautifulSoup(html, 'html.parser')
    for li in parsed.find(id='category-level-1').findAll('li'):
        a = li.findAll('a')[0]
        categories.append(category.Category(a.get('href'), a.string))
    return categories
