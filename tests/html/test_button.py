from tests.case import HTMLTestCase


class ButtonTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "button"


class TestSubmitTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("submit-with-id"), "id-submit")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("submit-with-value"), "value-submit")

    def test_finds_buttons_by_approximate_value(self):
        self.assertEqual(self.get("mit-with-val"), "value-submit")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My submit title"), "title-submit")

    def test_finds_buttons_by_approximate_title(self):
        self.assertEqual(self.get("submit title"), "title-submit")


class TestExactSubmitTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("submit-with-value", exact=True), "value-submit")

    def test_does_not_find_buttons_by_approximate_value(self):
        self.assertIsNone(self.get("mit-with-val", exact=True))

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My submit title", exact=True), "title-submit")

    def test_does_not_find_buttons_by_approximate_title(self):
        self.assertIsNone(self.get("submit title", exact=True))


class TestButtonTag(ButtonTestCase):
    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("btag-with-id"), "id-btag")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("btag-with-value"), "value-btag")

    def test_finds_buttons_by_approximate_value(self):
        self.assertEqual(self.get("tag-with-val"), "value-btag")

    def test_finds_buttons_by_text(self):
        self.assertEqual(self.get("btag-with-text"), "text-btag")

    def test_finds_buttons_by_text_ignoring_whitespace(self):
        self.assertEqual(self.get("My whitespaced button"), "btag-with-whitespace")

    def test_finds_buttons_by_approximate_text(self):
        self.assertEqual(self.get("tag-with-tex"), "text-btag")

    def test_finds_buttons_with_child_tags_by_text(self):
        self.assertEqual(self.get("An emphatic button"), "btag-with-children")

    def test_finds_buttons_by_text_of_their_children(self):
        self.assertEqual(self.get("emphatic"), "btag-with-children")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My btag title"), "title-btag")

    def test_finds_buttons_by_approximate_title(self):
        self.assertEqual(self.get("btag title"), "title-btag")


class TestExactButtonTag(ButtonTestCase):
    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("btag-with-value", exact=True), "value-btag")

    def test_does_not_find_buttons_by_approximate_value(self):
        self.assertIsNone(self.get("tag-with-val", exact=True))

    def test_finds_buttons_by_text(self):
        self.assertEqual(self.get("btag-with-text", exact=True), "text-btag")

    def test_does_not_find_buttons_by_approximate_text(self):
        self.assertIsNone(self.get("tag-with-tex", exact=True))

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My btag title", exact=True), "title-btag")

    def test_does_not_find_buttons_by_approximate_title(self):
        self.assertIsNone(self.get("btag title", exact=True))
