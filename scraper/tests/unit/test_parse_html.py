import unittest
import scraper.parse_html as parse_html
from hamcrest import assert_that, equal_to


class TestParsingHtml(unittest.TestCase):
    def test_stripping_newlines_from_price(self):
        result = parse_html.format_price('\n\n£302.00\n\n\n')
        assert_that(result, equal_to('302.00'))
