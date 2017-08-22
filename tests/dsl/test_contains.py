from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestContains(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_contain_the_given_string(self):
        xpath = to_xpath(x.descendant("div")[x.attr("title").contains("ooD")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "foo")

    def test_finds_nodes_that_contain_the_given_expression(self):
        expr = x.anywhere("div")[x.attr("title").equals("fooDiv")].attr("id")
        xpath = to_xpath(x.descendant("div")[x.attr("title").contains(expr)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "foo")
