from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestNextSibling(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_which_are_immediate_siblings_of_the_current_node(self):
        foo_div = x.descendant("p")[x.attr("id").equals("fooDiv")]
        monkey = x.descendant("p")[x.attr("title").equals("monkey")]

        xpath = to_xpath(foo_div.next_sibling("p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")

        xpath = to_xpath(foo_div.next_sibling("ul", "p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")

        xpath = to_xpath(monkey.next_sibling("ul", "p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "A list")

        xpath = to_xpath(foo_div.next_sibling("ul", "li"))
        results = self.find_all(xpath)
        self.assertSequenceEqual(results, [])

        xpath = to_xpath(foo_div.next_sibling())
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")
