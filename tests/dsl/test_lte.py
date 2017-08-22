from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestLte(DSLTestCase):
    __fixture__ = "simple.html"

    def test_checks_lesser_than_or_equal(self):
        xpath = to_xpath(x.descendant("p")[x.position().lte(2)])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].text, "Bax")
        self.assertEqual(results[2].get("title"), "gorilla")
        self.assertEqual(results[3].text, "Bax")

    def test_aliased_as_left_angle_bracket_equals(self):
        xpath = to_xpath(x.descendant("p")[x.position() <= 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Blah")
        self.assertEqual(results[1].text, "Bax")
        self.assertEqual(results[2].get("title"), "gorilla")
        self.assertEqual(results[3].text, "Bax")
