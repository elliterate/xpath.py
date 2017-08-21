# coding=utf-8
import sys
from tests.case import DSLTestCase
from xpath.dsl import attr, descendant, string
from xpath.renderer import to_xpath


class TestStringLiteral(DSLTestCase):
    __fixture__ = "simple.html"

    def test_matches_decoded_unicode_characters(self):
        locator = "이름" if sys.version_info >= (3, 0) else u"이름"

        xpath = to_xpath(descendant("div")[string.n.is_(locator)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "unicode")

        xpath = to_xpath(descendant("div")[attr("title") == locator])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "unicode")

    def test_matches_encoded_unicode_characters(self):
        locator = "이름".encode("UTF-8") if sys.version_info >= (3, 0) else "이름"

        xpath = to_xpath(descendant("div")[string.n.is_(locator)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "unicode")

        xpath = to_xpath(descendant("div")[attr("title") == locator])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "unicode")

    def test_matches_quotes(self):
        locator = "Who's quotes? \"Their\" quotes."

        xpath = to_xpath(descendant("div")[string.n.is_(locator)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "quotes")

        xpath = to_xpath(descendant("div")[attr("title") == locator])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "quotes")
