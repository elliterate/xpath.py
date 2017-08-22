from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestModulo(DSLTestCase):
    __fixture__ = "simple.html"

    def test_takes_modulo(self):
        xpath = to_xpath(x.descendant("p")[x.position().mod(2) == 1])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].get("title"), "monkey")
        self.assertEqual(results[2].get("title"), "gorilla")

    def test_aliased_as_modulo(self):
        xpath = to_xpath(x.descendant("p")[x.position() % 2 == 1])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].get("title"), "monkey")
        self.assertEqual(results[2].get("title"), "gorilla")
