import mock
import scraper.scrape as scrape
import scraper.model.category as category
import scraper.model.product as product
import unittest
from hamcrest import assert_that, equal_to


class TestScraping(unittest.TestCase):
    def test_stripping_srule(self):
        result = scrape.strip_srule('http://www.farah.co.uk/clothing/polo-shirts/?srule=best-matches')
        assert_that(result, equal_to('http://www.farah.co.uk/clothing/polo-shirts'))

    def test_ignoring_non_srule_urls(self):
        result = scrape.strip_srule('http://www.farah.co.uk/clothing/polo-shirts')
        assert_that(result, equal_to('http://www.farah.co.uk/clothing/polo-shirts'))

    def test_stripping_get_parameters(self):
        result = scrape.strip_get_parameters('www.hats.com?param=value')
        assert_that(result, equal_to('www.hats.com'))

    @mock.patch('scraper.scrape.parser')
    def test_parsing_category_page(self, mock_parser):
        html = 'html'
        mock_parser.parse_categories.return_value = [
            {'title': 'socks', 'url': '/socks.html'},
            {'title': 'hats', 'url': 'www.hats.com'},
        ]
        assert mock_parser.parse_categories.called_with(html)
        categories = scrape.get_categories_from_html(html)
        assert_that(categories[0], equal_to(category.Category('socks', '/socks.html?sz=60')))
        assert_that(categories[1], equal_to(category.Category('hats', 'www.hats.com?sz=60')))

    @mock.patch('scraper.scrape.parser')
    def test_parsing_links_from_category_page(self, mock_parser):
        html = 'html'
        mock_parser.parse_product_links_from_category_page.return_value = \
            ['url1?q=whatever', 'url2?something=otherthing', 'url1?p=v']
        urls = scrape.get_product_links_from_category_page(html)
        assert mock_parser.parse_product_links_from_category_page.called_with(html)
        assert_that(urls, equal_to(['url1', 'url2']))

    @mock.patch('scraper.scrape.parser')
    def test_parsing_product_details(self, mock_parser):
        html = 'html'
        mock_parser.parse_product_details.return_value = {
            'name': 'a lovely shirt',
            'discounted_price': '20.00',
            'high_price': '40.00',
            'item_number': '1234'
        }
        result = scrape.get_product_details_from_product_page(html)
        assert mock_parser.parse_product_details.called_with(html)
        assert_that(result, equal_to(product.Product(
            'a lovely shirt',
            '20.00',
            '40.00',
            '1234'
        )))
