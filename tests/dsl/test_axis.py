from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestAxis(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_given_the_xpath_axis(self):
        xpath = to_xpath(x.axis("descendant", "p"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")

    def test_finds_nodes_given_the_xpath_axis_without_a_specific_tag(self):
        xpath = to_xpath(x.descendant("div")[x.attr("id").equals("foo")].axis("descendant"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "fooDiv")
