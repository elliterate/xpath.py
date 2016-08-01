from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestUnion(DSLTestCase):
    __fixture__ = "simple.html"

    def test_creates_a_union_expression(self):
        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(collection[attr("id").equals("foo")])
        xpath2 = to_xpath(collection[attr("id").equals("fooDiv")])

        results = self.find_all(xpath1)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].get_attribute("id"), "fooDiv")

    def test_aliased_as_plus_sign(self):
        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1 + expr2

        xpath1 = to_xpath(collection[attr("id").equals("foo")])
        xpath2 = to_xpath(collection[attr("id").equals("fooDiv")])

        results = self.find_all(xpath1)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].get_attribute("id"), "fooDiv")
