from tests.case import HTMLTestCase


class FillableFieldTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "fillable_field"


class TestFillableField(FillableFieldTestCase):
    def test_finds_inputs_with_text_type(self):
        self.assertEqual(self.get("input-text-with-id"), "input-text-with-id-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(self.get("input-password-with-id"), "input-password-with-id-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(self.get("input-custom-with-id"), "input-custom-with-id-data")

    def test_finds_textareas(self):
        self.assertEqual(self.get("textarea-with-id"), "textarea-with-id-data")

    def test_does_not_find_inputs_with_file_type(self):
        self.assertIsNone(self.get("input-file-with-id"))

    def test_does_not_find_inputs_with_submit_type(self):
        self.assertIsNone(self.get("input-submit-with-id"))

    def test_does_not_find_inputs_with_image_type(self):
        self.assertIsNone(self.get("input-image-with-id"))

    def test_does_not_find_inputs_with_hidden_type(self):
        self.assertIsNone(self.get("input-hidden-with-id"))

    def test_does_not_find_inputs_with_checkbox_type(self):
        self.assertIsNone(self.get("input-checkbox-with-id"))

    def test_does_not_find_inputs_with_radio_type(self):
        self.assertIsNone(self.get("input-radio-with-id"))
