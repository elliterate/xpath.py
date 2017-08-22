from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestMultiply(DSLTestCase):
    __fixture__ = "simple.html"

    def test_multiplies(self):
        xpath = to_xpath(x.descendant("p")[x.position().multiply(3) == 3])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "fooDiv")
        self.assertEqual(results[1].get("title"), "gorilla")

    def test_aliased_as_multiply(self):
        xpath = to_xpath(x.descendant("p")[x.position() * 3 == 3])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "fooDiv")
        self.assertEqual(results[1].get("title"), "gorilla")
