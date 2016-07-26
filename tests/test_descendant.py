from tests.case import DSLTestCase
from xpath.renderer import attribute, descendant, equality, string_literal, this_node, where


class TestDescendant(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_are_nested_below_the_current_node(self):
        results = self.find_all(descendant(this_node(), "p"))
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].text, "Bax")

    def test_does_not_find_nodes_outside_the_context(self):
        xpath = where(
            descendant(this_node(), "p"),
            equality(
                attribute(this_node(), "id"),
                where(
                    descendant(this_node(), "div"),
                    equality(
                        attribute(this_node(), "id"),
                        string_literal("foo")))))

        results = self.find_all(xpath)
        self.assertSequenceEqual(results, [])
