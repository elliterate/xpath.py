from tests.case import HTMLTestCase


class SelectTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "select"


class TestSelect(SelectTestCase):
    def test_finds_selects_by_id(self):
        self.assertEqual(self.get("select-with-id"), "select-with-id-data")

    def test_finds_selects_by_name(self):
        self.assertEqual(self.get("select-with-name"), "select-with-name-data")

    def test_finds_selects_by_label(self):
        self.assertEqual(self.get("Select with label"), "select-with-label-data")

    def test_finds_selects_by_approximate_label(self):
        self.assertEqual(self.get("ect with lab"), "select-with-label-data")

    def test_finds_selects_by_parent_label(self):
        self.assertEqual(self.get("Select with parent label"), "select-with-parent-label-data")

    def test_finds_selects_by_approximate_parent_label(self):
        self.assertEqual(self.get("ect with parent lab"), "select-with-parent-label-data")


class TestExactSelect(SelectTestCase):
    def test_finds_selects_by_label(self):
        self.assertEqual(self.get("Select with label", exact=True), "select-with-label-data")

    def test_does_not_find_selects_by_approximate_label(self):
        self.assertIsNone(self.get("ect with lab", exact=True))

    def test_finds_selects_by_parent_label(self):
        self.assertEqual(
            self.get("Select with parent label", exact=True),
            "select-with-parent-label-data")

    def test_does_not_find_selects_by_approximate_parent_label(self):
        self.assertIsNone(self.get("ect with parent lab", exact=True))
