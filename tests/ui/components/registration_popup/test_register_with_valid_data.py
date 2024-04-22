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

    #TUA-15
    #Verify that new user is not registered if at least one of mandatory fields is empty
    def test_user_not_registered_if_mandatory_fields_empty(self):
        self.register_popup.click_user_type_button()
        self.assertEqual(self.register_popup.lastname_input_element.get_input_value(), "")
        self.assertTrue(self.register_popup.registration_button.get_attribute("disabled"))

        self.register_popup.lastname_input_element.set_input_value(" ")
        self.register_popup.lastname_input_element.clear_input()
        self.assertTrue("Введіть прізвище" in self.register_popup.lastname_input_element.get_error_messages_text_list())

        self.register_popup.email_input_element.set_input_value(self.VALID_EMAIL)
        self.assertEqual(self.register_popup.email_input_element.get_input_value(), self.VALID_EMAIL)
        self.register_popup.firstname_input_element.set_input_value(self.VALID_FIRSTNAME)
        self.assertEqual(self.register_popup.firstname_input_element.get_input_value(), self.VALID_FIRSTNAME)
        self.register_popup.phone_input_element.set_input_value(self.VALID_PHONE)
        self.assertEqual(self.register_popup.phone_input_element.get_input_value(), self.VALID_PHONE)

        self.register_popup.password_input_element.set_input_value(self.VALID_PASSWORD)
        self.assertEqual(self.register_popup.password_input_element.get_input_value(), self.VALID_PASSWORD)

        self.register_popup.password_confirmation_input_element.set_input_value(self.VALID_CONFIRMATION)
        self.assertEqual(self.register_popup.password_confirmation_input_element.get_input_value(), self.VALID_CONFIRMATION)
        self.assertEqual(self.register_popup.lastname_input_element.input_element_with_attributes.value_of_css_property('border-color'), "rgb(255, 77, 79)")

        #all the same but for manager
        self.register_popup.email_input_element.clear_input()
        self.register_popup.firstname_input_element.clear_input()
        self.register_popup.phone_input_element.clear_input()
        self.register_popup.password_input_element.clear_input()
        self.register_popup.password_confirmation_input_element.clear_input()

        self.register_popup.click_manager_type_button()
        self.assertEqual(self.register_popup.lastname_input_element.get_input_value(), "")
        self.assertTrue(self.register_popup.registration_button.get_attribute("disabled"))

        self.assertTrue("Введіть прізвище" in self.register_popup.lastname_input_element.get_error_messages_text_list())
        self.register_popup.email_input_element.set_input_value(self.VALID_EMAIL)
        self.assertEqual(self.register_popup.email_input_element.get_input_value(), self.VALID_EMAIL)
        self.register_popup.firstname_input_element.set_input_value(self.VALID_FIRSTNAME)
        self.assertEqual(self.register_popup.firstname_input_element.get_input_value(), self.VALID_FIRSTNAME)
        self.register_popup.phone_input_element.set_input_value(self.VALID_PHONE)
        self.assertEqual(self.register_popup.phone_input_element.get_input_value(), self.VALID_PHONE)

        self.register_popup.password_input_element.set_input_value(self.VALID_PASSWORD)
        self.assertEqual(self.register_popup.password_input_element.get_input_value(), self.VALID_PASSWORD)

        self.register_popup.password_confirmation_input_element.set_input_value(self.VALID_CONFIRMATION)
        self.assertEqual(self.register_popup.password_confirmation_input_element.get_input_value(), self.VALID_CONFIRMATION)
        self.assertEqual(self.register_popup.lastname_input_element.input_element_with_attributes.value_of_css_property('border-color'), "rgb(255, 77, 79)")