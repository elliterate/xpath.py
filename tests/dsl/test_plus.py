from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestPlus(DSLTestCase):
    __fixture__ = "simple.html"

    def test_adds(self):
        xpath = to_xpath(x.descendant("p")[x.position().plus(1) == 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "fooDiv")
        self.assertEqual(results[1].get("title"), "gorilla")
