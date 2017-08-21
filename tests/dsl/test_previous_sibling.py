from tests.case import DSLTestCase
from tests.helpers import inner_text
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestPreviousSibling(DSLTestCase):
    __fixture__ = "simple.html"

    def test_finds_nodes_which_are_exactly_preceding_the_current_node(self):
        woo_div = descendant("p")[attr("id").equals("wooDiv")]
        gorilla = descendant("p")[attr("title").equals("gorilla")]

        xpath = to_xpath(woo_div.previous_sibling("p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")

        xpath = to_xpath(woo_div.previous_sibling("ul", "p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")

        xpath = to_xpath(gorilla.previous_sibling("ul", "p"))
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "A list")

        xpath = to_xpath(woo_div.previous_sibling("ul", "li"))
        results = self.find_all(xpath)
        self.assertSequenceEqual(results, [])

        xpath = to_xpath(woo_div.previous_sibling())
        results = self.find_all(xpath)
        self.assertEqual(inner_text(results[0]), "Bax")
