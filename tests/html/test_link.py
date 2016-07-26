from tests.case import HTMLTestCase


class LinkTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "link"


class TestLink(LinkTestCase):
    def test_finds_links_by_id(self):
        self.assertEqual(self.get("some-id"), "link-id")

    def test_finds_links_by_content(self):
        self.assertEqual(self.get("An awesome link"), "link-text")

    def test_finds_links_by_content_regardless_of_whitespace(self):
        self.assertEqual(self.get("My whitespaced link"), "link-whitespace")

    def test_finds_links_with_child_tags_by_content(self):
        self.assertEqual(self.get("An emphatic link"), "link-children")

    def test_finds_links_by_the_content_of_their_child_tags(self):
        self.assertEqual(self.get("emphatic"), "link-children")

    def test_finds_links_by_approximate_content(self):
        self.assertEqual(self.get("awesome"), "link-text")

    def test_finds_by_title(self):
        self.assertEqual(self.get("My title"), "link-title")

    def test_finds_by_approximate_title(self):
        self.assertEqual(self.get("title"), "link-title")

    def test_finds_links_by_images_alt_attribute(self):
        self.assertEqual(self.get("Alt link"), "link-img")

    def test_finds_links_by_images_approximate_alt_attribute(self):
        self.assertEqual(self.get("Alt"), "link-img")

    def test_does_not_find_links_without_href_attributes(self):
        self.assertIsNone(self.get("Wrong Link"))


class TestExactLink(LinkTestCase):
    def test_finds_links_by_content(self):
        self.assertEqual(self.get("An awesome link", exact=True), "link-text")

    def test_does_not_find_links_by_approximate_content(self):
        self.assertIsNone(self.get("awesome", exact=True))

    def test_finds_links_by_title(self):
        self.assertEqual(self.get("My title", exact=True), "link-title")

    def test_does_not_find_links_by_title(self):
        self.assertIsNone(self.get("title", exact=True))

    def test_finds_links_by_images_alt_attribute(self):
        self.assertEqual(self.get("Alt link", exact=True), "link-img")

    def test_does_not_find_links_by_images_approximate_alt_attribute(self):
        self.assertIsNone(self.get("Alt", exact=True))
