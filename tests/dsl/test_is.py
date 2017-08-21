from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestIs(DSLTestCase):
    __fixture__ = "simple.html"

    def test_uses_equality_when_exact_given(self):
        xpath1 = to_xpath(descendant("div")[attr("id").is_("foo")], exact=True)
        results = self.find_all(xpath1)
        self.assertEqual(results[0].get("title"), "fooDiv")

        xpath2 = to_xpath(descendant("div")[attr("id").is_("oo")], exact=True)
        results = self.find_all(xpath2)
        self.assertSequenceEqual(results, [])

    def test_uses_substring_matching_otherwise(self):
        xpath1 = to_xpath(descendant("div")[attr("id").is_("foo")])
        results = self.find_all(xpath1)
        self.assertEqual(results[0].get("title"), "fooDiv")

        xpath2 = to_xpath(descendant("div")[attr("id").is_("oo")])
        results = self.find_all(xpath2)
        self.assertEqual(results[0].get("title"), "fooDiv")
