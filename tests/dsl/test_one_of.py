from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestOneOf(DSLTestCase):
    __fixture__ = "simple.html"

    def test_matches_all_nodes_where_the_condition_matches(self):
        xpath = to_xpath(descendant("*")[attr("id").one_of("foo", "baz")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")
        self.assertEqual(results[1].get("title"), "bazDiv")
