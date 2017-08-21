from tests.case import DSLTestCase
from xpath.dsl import descendant, text
from xpath.renderer import to_xpath


class TestStringLength(DSLTestCase):
    __fixture__ = "simple.html"

    def test_returns_the_length_of_a_string(self):
        xpath = to_xpath(descendant("span")[text.string_length == 11])
        results = self.find_all(xpath)
        self.assertEqual(results[1].get("id"), "string-length")
