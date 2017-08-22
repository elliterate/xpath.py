from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestDivide(DSLTestCase):
    __fixture__ = "simple.html"

    def test_divides(self):
        xpath = to_xpath(x.descendant("p")[x.position().divide(2) == 1])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].text, "Bax")

    def test_aliased_as_divide(self):
        xpath = to_xpath(x.descendant("p")[x.position() / 2 == 1])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].text, "Bax")
