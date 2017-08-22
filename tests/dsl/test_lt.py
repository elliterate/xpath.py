from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestLt(DSLTestCase):
    __fixture__ = "simple.html"

    def test_checks_lesser_than(self):
        xpath = to_xpath(x.descendant("p")[x.position().lt(2)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].get("title"), "gorilla")

    def test_aliased_as_left_angle_bracket(self):
        xpath = to_xpath(x.descendant("p")[x.position() < 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].get("title"), "gorilla")
