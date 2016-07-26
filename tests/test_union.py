from tests.case import DSLTestCase
from xpath.renderer import attribute, descendant, equality, string_literal, this_node, union, where


class TestUnion(DSLTestCase):
    __fixture__ = "simple.html"

    def test_creates_a_union_expression(self):
        expr1 = descendant(this_node(), "p")
        expr2 = descendant(this_node(), "div")

        collection = union(expr1, expr2)

        xpath1 = where(
            collection,
            equality(
                attribute(this_node(), "id"),
                string_literal("foo")))

        xpath2 = where(
            collection,
            equality(
                attribute(this_node(), "id"),
                string_literal("fooDiv")))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].get_attribute("id"), "fooDiv")
