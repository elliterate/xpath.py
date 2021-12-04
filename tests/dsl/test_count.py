from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestCount(DSLTestCase):
    __fixture__ = "simple.html"

    def test_counts_the_number_of_occurrences(self):
        xpath = to_xpath(x.descendant("div")[x.descendant("p").count == 2])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get("id"), "preference")
