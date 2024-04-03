from tests.base_test_runner import BaseTestRunner


class RegisterWithValidDataTest(BaseTestRunner):
    VALID_FIRSTNAME = "John"
    VALID_LASTNAME = "Doe"
    VALID_PHONE = "0987654321"
    VALID_EMAIL = "newemailexample1@email.com"
    VALID_PASSWORD = "Password1;"
    VALID_CONFIRMATION = "Password1;"
    REGISTRATION_SUCCESS = "Ви успішно зареєструвалися! Вам на пошту відправлено лист з лінком для підтвердження реєстрації"

    def setUp(self):
        super().setUp()
        self.register_popup = self.homepage.header.click_profile_button().open_registration_form()
        self.register_popup.wait_popup_open(5)

    def test_registering_with_valid_data(self):
        self.register_popup.email_input_element.set_input_value(self.VALID_EMAIL)
        self.register_popup.firstname_input_element.set_input_value(self.VALID_FIRSTNAME)
        self.register_popup.lastname_input_element.set_input_value(self.VALID_LASTNAME)
        self.register_popup.phone_input_element.set_input_value(self.VALID_PHONE)
        self.register_popup.password_input_element.set_input_value(self.VALID_PASSWORD)
        self.register_popup.password_confirmation_input_element.set_input_value(self.VALID_CONFIRMATION)
        self.register_popup.register()
        self.assertIn(self.homepage.get_top_notice_message(), self.REGISTRATION_SUCCESS,
                      "After registration popup with the following text should appear " + self.REGISTRATION_SUCCESS)
