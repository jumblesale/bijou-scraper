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
