from tests.case import HTMLTestCase


class CheckboxTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "checkbox"


class TestCheckbox(CheckboxTestCase):
    def test_finds_checkboxes_by_id(self):
        self.assertEqual(self.get("input-checkbox-with-id"), "input-checkbox-with-id-data")

    def test_finds_checkboxes_by_name(self):
        self.assertEqual(self.get("input-checkbox-with-name"), "input-checkbox-with-name-data")

    def test_finds_checkboxes_by_label(self):
        self.assertEqual(self.get("Input checkbox with label"), "input-checkbox-with-label-data")

    def test_finds_checkboxes_by_approximate_label(self):
        self.assertEqual(self.get("box with lab"), "input-checkbox-with-label-data")

    def test_finds_checkboxes_by_parent_label(self):
        self.assertEqual(
            self.get("Input checkbox with parent label"),
            "input-checkbox-with-parent-label-data")

    def test_finds_checkboxes_by_approximate_parent_label(self):
        self.assertEqual(self.get("box with parent lab"), "input-checkbox-with-parent-label-data")


class TestExactCheckbox(CheckboxTestCase):
    def test_finds_checkboxes_by_label(self):
        self.assertEqual(
            self.get("Input checkbox with label", exact=True),
            "input-checkbox-with-label-data")

    def test_finds_checkboxes_by_approximate_label(self):
        self.assertIsNone(self.get("box with lab", exact=True))

    def test_finds_checkboxes_by_parent_label(self):
        self.assertEqual(
            self.get("Input checkbox with parent label", exact=True),
            "input-checkbox-with-parent-label-data")

    def test_does_not_find_checkboxes_by_approximate_parent_label(self):
        self.assertIsNone(self.get("box with parent lab", exact=True))
