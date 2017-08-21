from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestNextSibling(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_which_are_immediate_siblings_of_the_current_node(self):
        foo_div = descendant("p")[attr("id").equals("fooDiv")]
        monkey = descendant("p")[attr("title").equals("monkey")]

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
