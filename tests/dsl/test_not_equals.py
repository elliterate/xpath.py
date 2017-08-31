from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestNotEquals(DSLTestCase):
    __fixture__ = "simple.html"

    def test_matches_only_when_not_equal(self):
        xpath = to_xpath(x.descendant("div")[x.attr("id").not_equals("bar")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")

    def test_aliased_as_exclamation_equals(self):
        xpath = to_xpath(x.descendant("div")[x.attr("id") != "bar"])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "fooDiv")
