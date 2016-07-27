from tests.case import HTMLTestCase


class FieldsetTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "fieldset"


class TestFieldset(FieldsetTestCase):
    def test_finds_fieldsets_by_id(self):
        self.assertEqual(self.get("some-fieldset-id"), "fieldset-id")

    def test_finds_fieldsets_by_legend(self):
        self.assertEqual(self.get("Some Legend"), "fieldset-legend")

    def test_finds_fieldsets_by_approximate_legend(self):
        self.assertEqual(self.get("Legend"), "fieldset-legend")

    def test_finds_fieldsets_by_legend_child_tags(self):
        self.assertEqual(self.get("Span Legend"), "fieldset-legend-span")

    def test_finds_fieldsets_by_approximate_legend_child_tags(self):
        self.assertEqual(self.get("Span"), "fieldset-legend-span")

    def test_finds_nested_fieldsets_by_legend(self):
        self.assertEqual(self.get("Inner legend"), "fieldset-inner")

    def test_finds_nested_fieldsets_by_approximate_legend(self):
        self.assertEqual(self.get("Inner"), "fieldset-inner")


class TestExactFieldset(FieldsetTestCase):
    def test_finds_fieldsets_by_legend(self):
        self.assertEqual(self.get("Some Legend", exact=True), "fieldset-legend")

    def test_does_not_find_fieldsets_by_approximate_legend(self):
        self.assertIsNone(self.get("Legend", exact=True))

    def test_finds_fieldsets_by_legend_child_tags(self):
        self.assertEqual(self.get("Span Legend", exact=True), "fieldset-legend-span")

    def test_does_not_find_fieldsets_by_approximate_legend_child_tags(self):
        self.assertIsNone(self.get("Span", exact=True))

    def test_finds_nested_fieldsets_by_legend(self):
        self.assertEqual(self.get("Inner legend", exact=True), "fieldset-inner")

    def test_does_not_find_nested_fieldsets_by_approximate_legend(self):
        self.assertIsNone(self.get("Inner", exact=True))
