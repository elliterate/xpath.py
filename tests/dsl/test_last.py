from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestLast(DSLTestCase):
    __fixture__ = "simple.html"

    def test_returns_the_number_of_elements_in_the_context(self):
        xpath = to_xpath(x.descendant("p")[x.position() == x.last()])
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")
        self.assertEqual(inner_text(results[1]), "Blah")
        self.assertEqual(inner_text(results[2]), "llama")
