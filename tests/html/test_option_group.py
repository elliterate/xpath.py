from tests.case import HTMLTestCase


class OptionGroupTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "optgroup"


class TestOptionGroup(OptionGroupTestCase):
    def test_finds_option_groups_by_label(self):
        self.assertEqual(self.get("Group A"), "optgroup-a")

    def test_finds_option_groups_by_approximate_text(self):
        self.assertEqual(self.get("oup A"), "optgroup-a")


class TestExactOptionGroup(OptionGroupTestCase):
    def test_finds_option_groups_by_text(self):
        self.assertEqual(self.get("Group A", exact=True), "optgroup-a")

    def test_does_not_find_option_groups_by_approximate_text(self):
        self.assertIsNone(self.get("oup A", exact=True))
