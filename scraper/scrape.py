from bs4 import BeautifulSoup
from scraper.model import category


def get_categories_from_html(html):
    categories = []
    parsed = BeautifulSoup(html, 'html.parser')
    for li in parsed.find(id='category-level-1').findAll('li'):
        a = li.findAll('a')[0]
        href = _strip_srule(a.get('href'))
        title = a.string
        categories.append(category.Category(title, href))
    return categories


def _strip_srule(url):
    srule = '/?srule=best-matches'
    if url.endswith(srule):
        return url[:-len(srule)]
