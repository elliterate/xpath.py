from tests.case import HTMLTestCase


class DefinitionDescriptionTestCase(HTMLTestCase):
    __fixture__ = "stuff.html"
    __matcher__ = "definition_description"


class TestDefinitionDescription(DefinitionDescriptionTestCase):
    def test_finds_definition_descriptions_by_id(self):
        self.assertEqual(self.get("latte"), "with-id")

    def test_finds_definition_descriptions_by_term(self):
        self.assertEqual(self.get("Milk"), "with-dt")
