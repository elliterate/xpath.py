from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestFunction(DSLTestCase):
    __fixture__ = "simple.html"

    def test_calls_the_given_xpath_function(self):
        xpath = to_xpath(x.function("boolean", x.function("true") == x.function("false")))
        results = self.find_all(xpath)
        self.assertIs(results, False)
