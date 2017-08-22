from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestStartsWith(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_begin_with_the_given_string(self):
        xpath = to_xpath(x.descendant("*")[x.attr("id").starts_with("foo")])
        results = self.find_all(xpath)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get("id"), "foo")
        self.assertEqual(results[1].get("id"), "fooDiv")

    def test_finds_nodes_that_contain_the_given_expression(self):
        expr = x.anywhere("div")[x.attr("title") == "fooDiv"].attr("id")
        xpath = to_xpath(x.descendant("div")[x.attr("title").starts_with(expr)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "foo")
