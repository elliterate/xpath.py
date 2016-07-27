from tests.case import HTMLTestCase


class OptionTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "option"


class TestOption(OptionTestCase):
    def test_finds_options_by_text(self):
        self.assertEqual(self.get("Option with text"), "option-with-text-data")

    def test_finds_options_by_approximate_text(self):
        self.assertEqual(self.get("Option with"), "option-with-text-data")


class TestExactOption(OptionTestCase):
    def test_finds_options_by_text(self):
        self.assertEqual(self.get("Option with text", exact=True), "option-with-text-data")

    def test_does_not_find_options_by_approximate_text(self):
        self.assertIsNone(self.get("Option with", exact=True))
