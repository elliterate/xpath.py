from tests.case import DSLTestCase
from xpath.dsl import attr, contains, descendant
from xpath.renderer import to_xpath


class TestAnd(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_all_nodes_in_both_expressions(self):
        xpath = to_xpath(descendant("*")[contains("Bax").and_(attr("title").equals("monkey"))])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")

    def test_aliased_as_ampersand(self):
        xpath = to_xpath(descendant("*")[contains("Bax") & attr("title").equals("monkey")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")
