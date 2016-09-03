from tests.case import DSLTestCase
from xpath.dsl import anywhere, attr, descendant
from xpath.renderer import to_xpath


class TestAnywhere(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_regardless_of_the_context(self):
        foo_div = anywhere("div")[attr("id").equals("foo")]
        xpath = to_xpath(descendant("p")[attr("id").equals(foo_div.attr("title"))])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")

    def test_finds_multiple_kinds_of_nodes_regardless_of_the_context(self):
        xpath = to_xpath(descendant("div")[attr("id") == "woo"].anywhere("p", "ul"))
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[3].text, "A list")
        self.assertEqual(results[4].text, "A list")
        self.assertEqual(results[6].text, "Bax")

    def test_finds_all_nodes_when_no_arguments_given_regardless_of_the_context(self):
        xpath = to_xpath(descendant("div")[attr("id") == "woo"].anywhere())
        results = self.find_all(xpath)
        self.assertEqual(results[0].tag_name, "html")
        self.assertEqual(results[1].tag_name, "head")
        self.assertEqual(results[3].tag_name, "body")
        self.assertEqual(results[5].text, "Blah")
        self.assertEqual(results[9].text, "A list")
        self.assertEqual(results[12].text, "A list")
        self.assertEqual(results[14].text, "Bax")
