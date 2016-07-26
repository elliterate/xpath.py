from tests.case import DSLTestCase
from xpath.renderer import attribute, descendant, equality, string_literal, this_node, where


class TestEquals(DSLTestCase):
    __fixture__ = "simple.html"

    def test_limits_the_expression_to_find_only_certain_nodes(self):
        xpath = where(
            descendant(this_node(), "div"),
            equality(
                attribute(this_node(), "id"),
                string_literal("foo")
            )
        )
        results = self.find_all(xpath)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")
