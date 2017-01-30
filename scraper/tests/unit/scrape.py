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

    @mock.patch('scraper.scrape.parser')
    def test_parsing_html_page(self, mock_parser):
        html = 'html'
        mock_parser.parse_categories.return_value = [
            {'title': 'socks', 'url': '/socks.html'},
            {'title': 'hats', 'url': 'www.hats.com'},
        ]
        assert mock_parser.parse_categories.called_with(html)
        assert scrape.get_categories_from_html(html)[0] == category.Category('socks', '/socks.html')
        assert scrape.get_categories_from_html(html)[1] == category.Category('hats', 'www.hats.com')
