from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestWhere(DSLTestCase):
    __fixture__ = "simple.html"

    def test_limits_the_expression_to_find_only_certain_nodes(self):
        xpath = to_xpath(x.descendant("div").where(x.attr("id").equals("foo")))
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")

    def test_aliased_as_square_brackets(self):
        xpath = to_xpath(x.descendant("div")[x.attr("id").equals("foo")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")
