from scraper.model import category
import scraper.parse_html as parser


def get_categories_from_html(html):
    categories = []
    for parsed_category in parser.parse_categories(html):
        categories.append(category.Category(
            parsed_category["title"],
            strip_srule(parsed_category["url"])
        ))
    return categories


def strip_srule(url):
    srule = '/?srule=best-matches'
    if url.endswith(srule):
        return url[:-len(srule)]
    return url


def strip_get_parameters(url):
    return url.split('?')[0]


def get_product_links_from_category_page(category_html):
    product_links = []
    for url in parser.parse_product_links_from_category_page(category_html):
        stripped_url = strip_get_parameters(url)
        if stripped_url not in product_links:
            product_links.append(stripped_url)
    return product_links


def get_products_from_html(html):
    products = []
