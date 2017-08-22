from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestGt(DSLTestCase):
    __fixture__ = "simple.html"

    def test_checks_greater_than(self):
        xpath = to_xpath(x.descendant("p")[x.position().gt(2)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")
        self.assertEqual(results[1].text, "Blah")

    def test_aliased_as_right_angle_bracket(self):
        xpath = to_xpath(x.descendant("p")[x.position() > 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("title"), "monkey")
        self.assertEqual(results[1].text, "Blah")
