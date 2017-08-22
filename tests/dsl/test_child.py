from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath.dsl import attr, child, descendant
from xpath.renderer import to_xpath


class TestChild(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_are_nested_directly_below_the_current_node(self):
        xpath = to_xpath(descendant("div").child("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].text, "Bax")

    def test_does_not_find_nodes_that_are_nested_further_down_below_the_current_node(self):
        xpath = to_xpath(child("p"))
        results = self.find_all(xpath)
        self.assertSequenceEqual(results, [])

    def test_finds_multiple_kinds_of_nodes(self):
        xpath = to_xpath(descendant("div").child("p", "ul"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Blah")
        self.assertEqual(inner_text(results[3]), "A list")

    def test_finds_all_nodes_when_no_arguments_given(self):
        xpath = to_xpath(descendant()[attr("id") == "foo"].child())
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Blah")
        self.assertEqual(inner_text(results[3]), "A list")
