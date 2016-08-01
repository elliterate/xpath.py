from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestDescendant(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_that_are_nested_below_the_current_node(self):
        xpath = to_xpath(descendant("p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].text, "Bax")

    def test_does_not_find_nodes_outside_the_context(self):
        foo_div = descendant("div")[attr("id").equals("foo")]
        xpath = to_xpath(descendant("p")[attr("id").equals(foo_div.attr("title"))])
        results = self.find_all(xpath)
        self.assertSequenceEqual(results, [])

    def test_finds_multiple_kinds_of_nodes(self):
        xpath = to_xpath(descendant("p", "ul"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[3].text, "A list")

    def test_finds_all_nodes_when_no_arguments_given(self):
        xpath = to_xpath(descendant()[attr("id").equals("foo")].descendant())
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[4].text, "A list")
