from tests.case import HTMLTestCase


class FileFieldTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "file_field"


class TestFileField(FileFieldTestCase):
    def test_finds_file_fields_by_id(self):
        self.assertEqual(self.get("input-file-with-id"), "input-file-with-id-data")

    def test_finds_file_fields_by_name(self):
        self.assertEqual(self.get("input-file-with-name"), "input-file-with-name-data")

    def test_finds_file_fields_by_label(self):
        self.assertEqual(self.get("Input file with label"), "input-file-with-label-data")

    def test_finds_file_fields_by_approximate_label(self):
        self.assertEqual(self.get("ile with lab"), "input-file-with-label-data")

    def test_finds_file_fields_by_parent_label(self):
        self.assertEqual(
            self.get("Input file with parent label"),
            "input-file-with-parent-label-data")

    def test_finds_file_fields_by_approximate_parent_label(self):
        self.assertEqual(self.get("ile with parent lab"), "input-file-with-parent-label-data")


class TestExactFileField(FileFieldTestCase):
    def test_finds_file_fields_by_label(self):
        self.assertEqual(
            self.get("Input file with label", exact=True),
            "input-file-with-label-data")

    def test_does_not_find_file_fields_by_approximate_label(self):
        self.assertIsNone(self.get("ile with lab", exact=True))

    def test_finds_file_fields_by_parent_label(self):
        self.assertEqual(
            self.get("Input file with parent label", exact=True),
            "input-file-with-parent-label-data")

    def test_does_not_find_file_fields_by_approximate_parent_label(self):
        self.assertIsNone(self.get("ile with parent lab", exact=True))
