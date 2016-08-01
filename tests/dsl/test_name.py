from tests.case import DSLTestCase
from xpath.dsl import descendant, name
from xpath.renderer import to_xpath


class TestName(DSLTestCase):
    __fixture__ = "simple.html"

    def test_matches_by_node_name(self):
        xpath = to_xpath(descendant("*")[name == "ul"])
        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "A list")
