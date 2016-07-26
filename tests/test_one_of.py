from tests.case import DSLTestCase
from xpath.renderer import attribute, descendant, one_of, string_literal, this_node, where


class TestOneOf(DSLTestCase):
    __fixture__ = "simple.html"

    def test_matches_all_nodes_where_the_condition_matches(self):
        xpath = where(
            descendant(this_node(), "*"),
            one_of(
                attribute(this_node(), "id"),
                [string_literal("foo"),
                 string_literal("baz")]))
        results = self.find_all(xpath)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")
        self.assertEqual(results[1].get_attribute("title"), "bazDiv")
