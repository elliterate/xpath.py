from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath.dsl import anywhere, attr, descendant
from xpath.renderer import to_xpath


class TestAnywhere(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_regardless_of_the_context(self):
        foo_div = anywhere("div")[attr("id").equals("foo")]
        xpath = to_xpath(descendant("p")[attr("id").equals(foo_div.attr("title"))])
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Blah")

    def test_finds_multiple_kinds_of_nodes_regardless_of_the_context(self):
        xpath = to_xpath(descendant("div")[attr("id") == "woo"].anywhere("p", "ul"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Blah")
        self.assertEqual(inner_text(results[3]), "A list")
        self.assertEqual(inner_text(results[4]), "A list")
        self.assertEqual(inner_text(results[6]), "Bax")

    def test_finds_all_nodes_when_no_arguments_given_regardless_of_the_context(self):
        xpath = to_xpath(descendant("div")[attr("id") == "woo"].anywhere())
        results = self.find_all(xpath)
        self.assertEqual(results[0].tag, "html")
        self.assertEqual(results[1].tag, "head")
        self.assertEqual(results[3].tag, "body")
        self.assertEqual(inner_text(results[5]), "Blah")
        self.assertEqual(inner_text(results[9]), "A list")
        self.assertEqual(inner_text(results[12]), "A list")
        self.assertEqual(inner_text(results[14]), "Bax")
