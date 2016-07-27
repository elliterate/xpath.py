from tests.case import HTMLTestCase


class FieldTestCase(HTMLTestCase):
    __fixture__ = "form.html"
    __matcher__ = "field"


class TestFieldById(FieldTestCase):
    def test_finds_inputs_with_no_type(self):
        self.assertEqual(self.get("input-with-id"), "input-with-id-data")

    def test_finds_inputs_with_text_type(self):
        self.assertEqual(self.get("input-text-with-id"), "input-text-with-id-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(self.get("input-password-with-id"), "input-password-with-id-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(self.get("input-custom-with-id"), "input-custom-with-id-data")

    def test_finds_textareas(self):
        self.assertEqual(self.get("textarea-with-id"), "textarea-with-id-data")

    def test_finds_select_boxes(self):
        self.assertEqual(self.get("select-with-id"), "select-with-id-data")

    def test_does_not_find_submit_buttons(self):
        self.assertIsNone(self.get("input-submit-with-id"))

    def test_does_not_find_image_buttons(self):
        self.assertIsNone(self.get("input-image-with-id"))

    def test_does_not_find_hidden_fields(self):
        self.assertIsNone(self.get("input-hidden-with-id"))


class TestFieldByName(FieldTestCase):
    def test_finds_inputs_with_no_type(self):
        self.assertEqual(self.get("input-with-name"), "input-with-name-data")

    def test_finds_inputs_with_text_type(self):
        self.assertEqual(self.get("input-text-with-name"), "input-text-with-name-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(self.get("input-password-with-name"), "input-password-with-name-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(self.get("input-custom-with-name"), "input-custom-with-name-data")

    def test_finds_textarea(self):
        self.assertEqual(self.get("textarea-with-name"), "textarea-with-name-data")

    def test_finds_select_boxes(self):
        self.assertEqual(self.get("select-with-name"), "select-with-name-data")

    def test_does_not_find_submit_buttons(self):
        self.assertIsNone(self.get("input-submit-with-name"))

    def test_does_not_find_image_buttons(self):
        self.assertIsNone(self.get("input-image-with-name"))

    def test_does_not_find_hidden_fields(self):
        self.assertIsNone(self.get("input-hidden-with-name"))


class TestFieldByPlaceholder(FieldTestCase):
    def test_finds_inputs_with_no_type(self):
        self.assertEqual(self.get("input-with-placeholder"), "input-with-placeholder-data")

    def test_finds_inputs_with_text_type(self):
        self.assertEqual(
            self.get("input-text-with-placeholder"),
            "input-text-with-placeholder-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(
            self.get("input-password-with-placeholder"),
            "input-password-with-placeholder-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(
            self.get("input-custom-with-placeholder"),
            "input-custom-with-placeholder-data")

    def test_finds_textareas(self):
        self.assertEqual(self.get("textarea-with-placeholder"), "textarea-with-placeholder-data")

    def test_does_not_find_hidden_fields(self):
        self.assertIsNone(self.get("input-hidden-with-placeholder"))


class TestFieldByReferencedLabel(FieldTestCase):
    def test_finds_inputs_with_no_type(self):
        self.assertEqual(self.get("Input with label"), "input-with-label-data")

    def test_finds_inputs_with_text_type(self):
        self.assertEqual(self.get("Input text with label"), "input-text-with-label-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(self.get("Input password with label"), "input-password-with-label-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(self.get("Input custom with label"), "input-custom-with-label-data")

    def test_finds_textareas(self):
        self.assertEqual(self.get("Textarea with label"), "textarea-with-label-data")

    def test_finds_select_boxes(self):
        self.assertEqual(self.get("Select with label"), "select-with-label-data")

    def test_does_not_find_submit_buttons(self):
        self.assertIsNone(self.get("Input submit with label"))

    def test_does_not_find_image_buttons(self):
        self.assertIsNone(self.get("Input image with label"))

    def test_does_not_find_hidden_fields(self):
        self.assertIsNone(self.get("Input hidden with label"))


class TestFieldByParentLabel(FieldTestCase):
    def test_finds_inputs_with_no_type(self):
        self.assertEqual(self.get("Input with parent label"), "input-with-parent-label-data")

    def test_finds_inputs_with_text_type(self):
        self.assertEqual(
            self.get("Input text with parent label"),
            "input-text-with-parent-label-data")

    def test_finds_inputs_with_password_type(self):
        self.assertEqual(
            self.get("Input password with parent label"),
            "input-password-with-parent-label-data")

    def test_finds_inputs_with_custom_type(self):
        self.assertEqual(
            self.get("Input custom with parent label"),
            "input-custom-with-parent-label-data")

    def test_finds_textareas(self):
        self.assertEqual(self.get("Textarea with parent label"), "textarea-with-parent-label-data")

    def test_finds_select_boxes(self):
        self.assertEqual(self.get("Select with parent label"), "select-with-parent-label-data")

    def test_does_not_find_submit_buttons(self):
        self.assertIsNone(self.get("Input submit with parent label"))

    def test_does_not_find_image_buttons(self):
        self.assertIsNone(self.get("Input image with parent label"))

    def test_does_not_find_hidden_fields(self):
        self.assertIsNone(self.get("Input hidden with parent label"))
