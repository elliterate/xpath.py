from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestGte(DSLTestCase):
    __fixture__ = "simple.html"

    def test_checks_greater_than_or_equal(self):
        xpath = to_xpath(x.descendant("p")[x.position().gte(2)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].get("title"), "monkey")
        self.assertEqual(results[2].text, "Bax")
        self.assertEqual(results[3].text, "Blah")

    def test_aliased_as_right_angle_bracket_equals(self):
        xpath = to_xpath(x.descendant("p")[x.position() >= 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].get("title"), "monkey")
        self.assertEqual(results[2].text, "Bax")
        self.assertEqual(results[3].text, "Blah")
