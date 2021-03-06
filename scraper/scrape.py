from scraper.model import category
from scraper.model import product
import scraper.parse_html as parser


def get_categories_from_html(html):
    categories = []
    for parsed_category in parser.parse_categories(html):
        categories.append(category.Category(
            parsed_category["title"],
            add_max_items_per_page(strip_srule(parsed_category["url"]))
        ))
    return categories


def strip_srule(url):
    srule = '/?srule=best-matches'
    if url.endswith(srule):
        return url[:-len(srule)]
    return url


def strip_get_parameters(url):
    return url.split('?')[0]


def add_max_items_per_page(url):
    return url + '?sz=60'


def get_product_links_from_category_page(category_html):
    product_links = []
    for url in parser.parse_product_links_from_category_page(category_html):
        stripped_url = strip_get_parameters(url)
        if stripped_url not in product_links:
            product_links.append(stripped_url)
    return product_links


def get_product_details_from_product_page(product_page_html):
    details = parser.parse_product_details(product_page_html)
    return product.Product(
        details['name'],
        details['discounted_price'],
        details['high_price'],
        details['item_number']
    )
