from tests.base_test_runner import BaseTestRunner


class RegisterWithInvalidDataTest(BaseTestRunner):

    ERROR_MESSAGE_EMAIl_FORMAT = "Некоректний формат email"
    ERROR_MESSAGE_EMAIl_EMPTY = "Введіть email"
    INVALID_EMAIl_VALUES = ["email", "111", "default@1", "Email.com"]

    def setUp(self):
        super().setUp()
        self.register_popup = self.homepage.header.click_profile_button().open_registration_form()
        self.register_popup.wait_popup_open(5)

    def test_registering_with_invalid_email(self):
        for INVALID_EMAIL_VALUE in self.INVALID_EMAIl_VALUES:
            self.register_popup.email_input_element.set_input_value(INVALID_EMAIL_VALUE)
            self.assertIn(self.ERROR_MESSAGE_EMAIl_FORMAT,
                          self.register_popup.email_input_element.get_error_messages_text_list(),
                          "Email error list should contain: " + self.ERROR_MESSAGE_EMAIl_FORMAT)
            self.register_popup.email_input_element.clear_input()
            self.assertIn(self.ERROR_MESSAGE_EMAIl_EMPTY,
                          self.register_popup.email_input_element.get_error_messages_text_list(),
                          "Email error list should contain: " + self.ERROR_MESSAGE_EMAIl_EMPTY)
