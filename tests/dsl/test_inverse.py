from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestInverse(DSLTestCase):
    __fixture__ = "simple.html"

    def test_inverts_the_expression(self):
        xpath = to_xpath(x.descendant("p")[x.attr("id").equals("fooDiv").inverse])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")

    def test_aliased_as_the_unary_tilde(self):
        xpath = to_xpath(x.descendant("p")[~x.attr("id").equals("fooDiv")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
