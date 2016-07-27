from tests.case import HTMLTestCase


class TableTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "table"


class TestTable(TableTestCase):
    def test_finds_tables_by_id(self):
        self.assertEqual(self.get("table-with-id"), "table-with-id-data")

    def test_finds_tables_by_caption(self):
        self.assertEqual(self.get("Table with caption"), "table-with-caption-data")

    def test_finds_tables_by_approximate_caption(self):
        self.assertEqual(self.get("Table with"), "table-with-caption-data")


class TestExactTable(TableTestCase):
    def test_finds_tables_by_caption(self):
        self.assertEqual(self.get("Table with caption", exact=True), "table-with-caption-data")

    def test_does_not_find_tables_by_approximate_caption(self):
        self.assertIsNone(self.get("Table with", exact=True))
