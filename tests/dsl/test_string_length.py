from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestStringLength(DSLTestCase):
    __fixture__ = "simple.html"

    def test_returns_the_length_of_a_string(self):
        xpath = to_xpath(x.descendant("span")[x.text.string_length == 11])
        results = self.find_all(xpath)
        self.assertEqual(results[1].get("id"), "string-length")
