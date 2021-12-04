from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestPosition(DSLTestCase):
    __fixture__ = "simple.html"

    def test_returns_the_position_of_elements_in_the_context(self):
        xpath = to_xpath(x.descendant("p")[x.position() == 2])
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")
        self.assertEqual(inner_text(results[1]), "Bax")
