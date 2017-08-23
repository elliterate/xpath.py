from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestAncestor(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_ancestor_nodes(self):
        xpath = to_xpath(x.descendant("p")[1].ancestor())
        results = self.find_all(xpath)
        self.assertEqual(results[0].tag, "html")
        self.assertEqual(results[1].tag, "body")
        self.assertEqual(results[2].get("id"), "foo")
