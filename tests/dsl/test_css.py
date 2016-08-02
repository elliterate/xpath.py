from tests.case import DSLTestCase
from xpath.dsl import attr, css, descendant
from xpath.renderer import to_xpath


class TestCSS(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_by_the_given_css_selector(self):
        xpath = to_xpath(css("#preference p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "allamas")
        self.assertEqual(results[1].text, "llama")

    def test_respects_previous_expression(self):
        xpath = to_xpath(descendant()[attr("id").equals("moar")].css("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "flamingo")

    def test_is_composable(self):
        xpath = to_xpath(css("#moar").descendant("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "flamingo")

    def test_allows_comma_separated_selectors(self):
        xpath = to_xpath(descendant()[attr("id").equals("moar")].css("div, p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "elephant")
        self.assertEqual(results[2].text, "flamingo")
