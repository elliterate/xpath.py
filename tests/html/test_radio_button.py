from tests.case import HTMLTestCase


class RadioButtonTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "radio_button"


class TestRadioButton(RadioButtonTestCase):
    def test_finds_radio_buttons_by_id(self):
        self.assertEqual(self.get("input-radio-with-id"), "input-radio-with-id-data")

    def test_finds_radio_buttons_by_name(self):
        self.assertEqual(self.get("input-radio-with-name"), "input-radio-with-name-data")

    def test_finds_radio_buttons_by_label(self):
        self.assertEqual(self.get("Input radio with label"), "input-radio-with-label-data")

    def test_finds_radio_buttons_by_approximate_label(self):
        self.assertEqual(self.get("dio with lab"), "input-radio-with-label-data")

    def test_finds_radio_buttons_by_parent_label(self):
        self.assertEqual(
            self.get("Input radio with parent label"),
            "input-radio-with-parent-label-data")

    def test_finds_radio_buttons_by_approximate_parent_label(self):
        self.assertEqual(self.get("dio with parent lab"), "input-radio-with-parent-label-data")


class TestExactRadioButton(RadioButtonTestCase):
    def test_finds_radio_buttons_by_label(self):
        self.assertEqual(
            self.get("Input radio with label", exact=True),
            "input-radio-with-label-data")

    def test_does_not_find_radio_buttons_by_approximate_label(self):
        self.assertIsNone(self.get("dio with lab", exact=True))

    def test_finds_radio_buttons_by_parent_label(self):
        self.assertEqual(
            self.get("Input radio with parent label", exact=True),
            "input-radio-with-parent-label-data")

    def test_does_not_find_radio_buttons_by_approximate_parent_label(self):
        self.assertIsNone(self.get("dio with parent lab", exact=True))
