from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath.dsl import descendant, last, position
from xpath.renderer import to_xpath


class TestLast(DSLTestCase):
    __fixture__ = "simple.html"

    def test_returns_the_number_of_elements_in_the_context(self):
        xpath = to_xpath(descendant("p")[position() == last()])
        results = self.find_all(xpath)
        self.assertEquals(inner_text(results[0]), "Bax")
        self.assertEquals(inner_text(results[1]), "Blah")
        self.assertEquals(inner_text(results[2]), "llama")
