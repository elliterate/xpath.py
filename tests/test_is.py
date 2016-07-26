from tests.case import DSLTestCase
from xpath.renderer import attribute, descendant, is_, string_literal, this_node, where


class TestIs(DSLTestCase):
    __fixture__ = "simple.html"

    def test_uses_equality_when_exact_given(self):
        xpath1 = where(
            descendant(this_node(), "div"),
            is_(
                attribute(this_node(), "id"),
                string_literal("foo"),
                exact=True))
        results = self.find_all(xpath1)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")

        xpath2 = where(
            descendant(this_node(), "div"),
            is_(
                attribute(this_node(), "id"),
                string_literal("oo"),
                exact=True))
        results = self.find_all(xpath2)
        self.assertSequenceEqual(results, [])

    def test_uses_substring_matching_otherwise(self):
        xpath1 = where(
            descendant(this_node(), "div"),
            is_(
                attribute(this_node(), "id"),
                string_literal("foo")))
        results = self.find_all(xpath1)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")

        xpath2 = where(
            descendant(this_node(), "div"),
            is_(
                attribute(this_node(), "id"),
                string_literal("oo")))
        results = self.find_all(xpath2)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")
