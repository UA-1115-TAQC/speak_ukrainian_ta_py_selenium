from tests.base_test_runner import LogInWithUserTestRunner


class TestEditProfilePageWithUser(LogInWithUserTestRunner):
    def setUp(self):
        super().setUp()

    def inalid_last_name_and_msg(self):
        return [
            ("AfBbCcDdEeFfGgHhIiJjKkLlMmNn", "Прізвище не може містити більше, ніж 25 символів"),
            ("AfBbCcDdEeFfGgHhIiJjKkLlMm", "Прізвище не може містити більше, ніж 25 символів"),
            ("!@#$%^&,", "Прізвище не може містити спеціальні символи"),
            ("1234", "Прізвище не може містити цифри"),
            ("-Lastname", "Прізвище не може містити символи"),
            ("< Lastname>", "Прізвище повинно починатися та закінчуватися літерою"),
            ("'Lastname", "Прізвище повинно починатися та закінчуватися літерою"),
            ("Lastname-", "Прізвище повинно починатися та закінчуватися літерою"),
            ("Lastname'", "Прізвище повинно починатися та закінчуватися літерою")
        ]

    def test_edit(self):
        empty_field_error_msg = "Будь ласка введіть Ваше прізвище"
        profile_page = self.homepage.header.open_user_menu().click_profile()
        edit_user = profile_page.click_edit_profile_button()

        for invalid_name, error_message in self.inalid_last_name_and_msg():
            with self.subTest(description=f"Testing last name error messages with invalid data: {invalid_name}"):
                (edit_user.last_name_element.clear_edit_profile_input()
                    .set_edit_profile_input_value(invalid_name))
                self.assertEqual(edit_user.last_name_element.get_edit_profile_error_messages_text_list()[0],
                                 error_message,
                                 "Error messages for " + invalid_name + " are different")
                self.assertFalse(edit_user.submit_button.is_enabled(), "Submit button should not be enabled")

        edit_user.last_name_element.clear_edit_profile_input()
        self.assertEqual(edit_user.last_name_element.get_edit_profile_error_messages_text_list()[0],
                         empty_field_error_msg,
                         "Error message for an empty filed is different")

