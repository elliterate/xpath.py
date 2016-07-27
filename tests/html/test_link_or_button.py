from tests.case import HTMLTestCase


class LinkOrButtonTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "link_or_button"


class TestLinkOrButton(LinkOrButtonTestCase):
    def test_finds_links_by_id(self):
        self.assertEqual(self.get("some-id"), "link-id")

    def test_finds_links_by_content(self):
        self.assertEqual(self.get("An awesome link"), "link-text")

    def test_finds_links_by_title(self):
        self.assertEqual(self.get("My title"), "link-title")

    def test_finds_buttons_by_id(self):
        self.assertEqual(self.get("btag-with-id"), "id-btag")

    def test_finds_buttons_by_value(self):
        self.assertEqual(self.get("btag-with-value"), "value-btag")

    def test_finds_buttons_by_text(self):
        self.assertEqual(self.get("btag-with-text"), "text-btag")

    def test_finds_buttons_by_title(self):
        self.assertEqual(self.get("My btag title"), "title-btag")
