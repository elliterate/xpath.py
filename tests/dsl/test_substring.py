from tests.case import DSLTestCase
from xpath.dsl import descendant, text
from xpath.renderer import to_xpath


class TestSubstring(DSLTestCase):
    __fixture__ = "simple.html"

    def test_selects_the_part_of_a_string_after_the_specified_character(self):
        xpath = to_xpath(descendant("*")[text.substring(7).equals("there")])
        results = self.find_all(xpath)
        self.assertEquals(results[0].get("id"), "substring")

    def test_selects_the_part_of_a_string_after_the_specified_character_and_up_to_the_given_length(self):
        xpath = to_xpath(descendant("*")[text.substring(2, 4).equals("ello")])
        results = self.find_all(xpath)
        self.assertEquals(results[0].get("id"), "substring")
