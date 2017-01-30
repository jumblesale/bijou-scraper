import mock
import scraper.scrape as scrape
import scraper.model.category as category
import unittest


class TestScraping(unittest.TestCase):
    def test_stripping_srule(self):
        result = scrape.strip_srule('http://www.farah.co.uk/clothing/polo-shirts/?srule=best-matches')
        assert result == 'http://www.farah.co.uk/clothing/polo-shirts'

    def test_ignoring_non_srule_urls(self):
        result = scrape.strip_srule('http://www.farah.co.uk/clothing/polo-shirts')
        assert result == 'http://www.farah.co.uk/clothing/polo-shirts'

    def test_stripping_get_parameters(self):
        result = scrape.strip_get_parameters('www.hats.com?param=value')
        assert result == 'www.hats.com'

    @mock.patch('scraper.scrape.parser')
    def test_parsing_category_page(self, mock_parser):
        html = 'html'
        mock_parser.parse_categories.return_value = [
            {'title': 'socks', 'url': '/socks.html'},
            {'title': 'hats', 'url': 'www.hats.com'},
        ]
        assert mock_parser.parse_categories.called_with(html)
        categories = scrape.get_categories_from_html(html)
        assert categories[0] == category.Category('socks', '/socks.html')
        assert categories[1] == category.Category('hats', 'www.hats.com')

    @mock.patch('scraper.scrape.parser')
    def test_parsing_links_from_category_page(self, mock_parser):
        html = 'html'
        mock_parser.parse_product_links_from_category_page.return_value = \
            ['url1?q=whatever', 'url2?something=otherthing', 'url1?p=v']
        urls = scrape.get_product_links_from_category_page(html)
        assert mock_parser.parse_product_links_from_category_page.called_with(html)
        assert urls == ['url1', 'url2']