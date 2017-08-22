from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestAnd(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_all_nodes_in_both_expressions(self):
        xpath = to_xpath(x.descendant("*")[x.contains("Bax").and_(x.attr("title").equals("monkey"))])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")

    def test_aliased_as_ampersand(self):
        xpath = to_xpath(x.descendant("*")[x.contains("Bax") & x.attr("title").equals("monkey")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")
