from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestMinus(DSLTestCase):
    __fixture__ = "simple.html"

    def test_subtracts(self):
        xpath = to_xpath(x.descendant("p")[x.position().minus(1) == 0])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "fooDiv")
        self.assertEqual(results[1].get("title"), "gorilla")
