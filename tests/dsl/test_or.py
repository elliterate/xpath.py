from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestOr(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_all_nodes_in_either_expression(self):
        xpath = to_xpath(descendant("*")[attr("id").equals("foo").or_(attr("id").equals("fooDiv"))])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")
        self.assertEqual(results[1].text, "Blah")

    def test_aliased_as_pipe(self):
        xpath = to_xpath(descendant("*")[attr("id").equals("foo") | attr("id").equals("fooDiv")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")
        self.assertEqual(results[1].text, "Blah")
