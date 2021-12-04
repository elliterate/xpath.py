from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestMethod(DSLTestCase):
    __fixture__ = "simple.html"

    def test_calls_the_given_xpath_function_with_the_current_node_as_the_first_argument(self):
        xpath = to_xpath(x.descendant("span").where(x.attr("id") == "string-length").text.method("string-length"))
        results = self.find_all(xpath)
        self.assertEqual(results, 11)
