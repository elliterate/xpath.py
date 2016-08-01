from tests.case import DSLTestCase
from xpath.dsl import descendant, text
from xpath.renderer import to_xpath


class TestText(DSLTestCase):
    __fixture__ = "simple.html"

    def test_selects_a_nodes_text(self):
        xpath = to_xpath(descendant("p")[text == "Bax"])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Bax")
        self.assertEqual(results[1].get_attribute("title"), "monkey")

        xpath = to_xpath(descendant("div")[descendant("p").text == "Bax"])
        results = self.find_all(xpath)
        self.assertEqual(results[0].get_attribute("title"), "fooDiv")
