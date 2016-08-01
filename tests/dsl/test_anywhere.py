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
