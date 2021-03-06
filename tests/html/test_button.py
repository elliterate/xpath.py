from tests.case import HTMLTestCase


class ButtonTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "button"


class TestButtonTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("button-with-id"), "id-button")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("button-with-value"), "value-button")

    def test_finds_buttons_by_approximate_value(self):
        self.assertEqual(self.get("ton-with-val"), "value-button")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My button title"), "title-button")

    def test_finds_buttons_by_approximate_title(self):
        self.assertEqual(self.get("button title"), "title-button")


class TestExactButtonTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("button-with-value", exact=True), "value-button")

    def test_does_not_find_buttons_by_approximate_value(self):
        self.assertIsNone(self.get("ton-with-val", exact=True))

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My button title", exact=True), "title-button")

    def test_does_not_find_buttons_by_title(self):
        self.assertIsNone(self.get("button title", exact=True))


class TestImageTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("imgbut-with-id"), "id-imgbut")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("imgbut-with-value"), "value-imgbut")

    def test_finds_buttons_by_approximate_value(self):
        self.assertEqual(self.get("gbut-with-val"), "value-imgbut")

    def test_finds_buttons_by_alt_attribute(self):
        self.assertEqual(self.get("imgbut-with-alt"), "alt-imgbut")

    def test_finds_buttons_by_approximate_alt_attribute(self):
        self.assertEqual(self.get("mgbut-with-al"), "alt-imgbut")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My imgbut title"), "title-imgbut")

    def test_finds_buttons_by_approximate_title(self):
        self.assertEqual(self.get("imgbut title"), "title-imgbut")


class TestExactImageTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("imgbut-with-value", exact=True), "value-imgbut")

    def test_does_not_find_buttons_by_approximate_value(self):
        self.assertIsNone(self.get("gbut-with-val", exact=True))

    def test_finds_buttons_by_alt_attribute(self):
        self.assertEqual(self.get("imgbut-with-alt", exact=True), "alt-imgbut")

    def test_does_not_find_buttons_by_approximate_alt_attribute(self):
        self.assertIsNone(self.get("mgbut-with-al", exact=True))

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My imgbut title", exact=True), "title-imgbut")

    def test_does_not_find_buttons_by_title(self):
        self.assertIsNone(self.get("imgbut title", exact=True))


class TestResetTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("reset-with-id"), "id-reset")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("reset-with-value"), "value-reset")

    def test_finds_buttons_by_approximate_value(self):
        self.assertEqual(self.get("set-with-val"), "value-reset")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My reset title"), "title-reset")

    def test_finds_buttons_by_approximate_title(self):
        self.assertEqual(self.get("reset title"), "title-reset")


class TestExactResetTypeInputTag(ButtonTestCase):
    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("reset-with-value", exact=True), "value-reset")

    def test_does_not_find_buttons_by_approximate_value(self):
        self.assertIsNone(self.get("set-with-val", exact=True))

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My reset title", exact=True), "title-reset")

    def test_does_not_find_buttons_by_title(self):
        self.assertIsNone(self.get("reset title", exact=True))


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
