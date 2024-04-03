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


    def test_the_corresponding_message(self):
        email = "a40qwxrnd518dd@emailabox.pro"
        self.register_popup.click_manager_type_button()
        self.register_popup.lastname_input_element.set_input_value(self.VALID_LASTNAME)
        self.assertEqual(self.register_popup.lastname_input_element.get_input_value(),
                         self.VALID_LASTNAME,
                         "The expected last name is different from the entered one")

        self.register_popup.firstname_input_element.set_input_value(self.VALID_FIRSTNAME)
        self.assertEqual(self.register_popup.firstname_input_element.get_input_value(),
                         self.VALID_FIRSTNAME,
                         "The expected first name is different from the entered one")

        self.register_popup.phone_input_element.set_input_value(self.VALID_PHONE)
        self.assertEqual(self.register_popup.phone_input_element.get_input_value(),
                         self.VALID_PHONE,
                         "The expected phone number is different from the entered one")

        self.register_popup.email_input_element.set_input_value(email)
        self.assertEqual(self.register_popup.email_input_element.get_input_value(),
                         email,
                         "The expected email address is different from the entered one")

        self.register_popup.password_input_element.set_input_value(self.VALID_PASSWORD)
        self.assertEqual(self.register_popup.password_input_element.get_input_value(),
                         self.VALID_PASSWORD,
                         "The expected password is different from the entered one")

        self.register_popup.password_confirmation_input_element.set_input_value(self.VALID_CONFIRMATION)
        self.assertEqual(self.register_popup.password_confirmation_input_element.get_input_value(),
                         self.VALID_PASSWORD,
                         "Password and confirm password data are different")

        self.register_popup.register()
        self.assertIn(self.homepage.get_top_notice_message(), self.REGISTRATION_SUCCESS,
                      "After registration popup with the following text should appear " + self.REGISTRATION_SUCCESS)

