from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestCSS(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_by_the_given_css_selector(self):
        xpath = to_xpath(x.css("#preference p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "allamas")
        self.assertEqual(results[1].text, "llama")

    def test_respects_previous_expression(self):
        xpath = to_xpath(x.descendant()[x.attr("id").equals("moar")].css("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "flamingo")

    def test_is_composable(self):
        xpath = to_xpath(x.css("#moar").descendant("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "flamingo")

    def test_allows_comma_separated_selectors(self):
        xpath = to_xpath(x.descendant()[x.attr("id").equals("moar")].css("div, p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "chimp")
        self.assertEqual(results[1].text, "elephant")
        self.assertEqual(results[2].text, "flamingo")
