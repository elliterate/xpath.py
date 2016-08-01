from tests.case import DSLTestCase
from xpath.dsl import child, descendant
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
