from tests.case import DSLTestCase
from xpath.dsl import anywhere, attr, descendant
from xpath.renderer import to_xpath


class TestStartsWith(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_begin_with_the_given_string(self):
        xpath = to_xpath(descendant("*")[attr("id").starts_with("foo")])
        results = self.find_all(xpath)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get("id"), "foo")
        self.assertEqual(results[1].get("id"), "fooDiv")

    def test_finds_nodes_that_contain_the_given_expression(self):
        expr = anywhere("div")[attr("title") == "fooDiv"].attr("id")
        xpath = to_xpath(descendant("div")[attr("title").starts_with(expr)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "foo")
