from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestContainsWord(DSLTestCase):
    __fixture__ = "simple.html"

    def test_find_nodes_that_contain_the_given_word_in_its_entirety(self):
        xpath = to_xpath(x.descendant()[x.attr("class").contains_word("fish")])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].text, "llama")
        self.assertEqual(len(results), 2)
