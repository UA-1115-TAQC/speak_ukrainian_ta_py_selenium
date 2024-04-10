from selenium.webdriver import Keys
from tests.base_test_runner import LogInWithAdminTestRunner
from tests.utils.credentials import Credentials


class AddClubPopUpWithAdminTest(LogInWithAdminTestRunner):
    INVALID_CLUB_NAME = "ÄыЁЪùייראפ"
    VALID_CLUB_NAME = "ПОРівд(*^*&%jhTY"
    ERROR_SYMBOL_MESSAGE = "Це поле може містити тільки українські та англійські літери, цифри та спеціальні символи"
    TELEPHONE_ERROR_SYMBOL_MESSAGE = "Телефон не може містити спеціальні символи, літери та пробіли"
    TELEPHONE_ERROR_FORMAT_MESSAGE = "Телефон не відповідає вказаному формату"
    VALID_CATEGORY = "Спортивні секції"
    INVALID_MIN_AGE = "0"
    VALID_MIN_AGE = "2"
    INVALID_MAX_AGE = "35"
    VALID_MAX_AGE = "18"
    VALID_CENTER_NAME = "INVENTOR СТЕМ-Школа"
    INVALID_TELEPHONE_NUMBER = "&*^роYT8"
    VALID_TELEPHONE_NUMBER = "0987656453"
    INVALID_DESCRIPTION = "%;№?*(?:фЙїqfG123456789 ÄыЁЪ ¥¼µ€"
    VALID_DESCRIPTION = "Bla bla, 123!! Text@ 1232"
    VALID_CIRCLE_ICON = "check-circle"
    INVALID_CIRCLE_ICON = "close-circle"
    SECOND_STEP = "2"
    THIRD_STEP = "3"
    TEXT_40_SYMBOLS = "Abc " * 10
    TEXT_1000_SYMBOLS = "AaBbCcDdEeFfGgHhIiJjKkLl " * 4
    TEXT_1500_SYMBOLS = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxY " * 30

    def setUp(self):
        super().setUp()
        self.add_club_popup = self.homepage.header.add_club_click()
        self.add_club_popup.wait_popup_open(5)

    def valid_description_textarea_value(self):
        return [
            (self.TEXT_40_SYMBOLS, "Green circle check icon should appear on the description textarea"),
            (self.TEXT_1000_SYMBOLS, "Green circle check icon should appear on the description textarea"),
            (self.TEXT_1500_SYMBOLS, "Green circle check icon should appear on the description textarea")
        ]

    def fill_step_one_with_valid_data_preconditions(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(self.VALID_CLUB_NAME)
        step_one.click_on_category_by_name(self.VALID_CATEGORY)
        step_one.min_age_input_element.set_input_value(self.VALID_MIN_AGE)
        step_one.max_age_input_element.set_input_value(self.VALID_MAX_AGE)
        step_one.click_next_step_button()

    def fill_step_two_with_valid_data_preconditions(self):
        step_two = self.add_club_popup.step_two_container
        step_two.telephone_input_element.set_input_value(self.VALID_TELEPHONE_NUMBER)
        step_two.click_next_step_button()

    #TUA-928
    def test_adding_club_with_corrected_data(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(self.INVALID_CLUB_NAME)
        self.assertIn(self.ERROR_SYMBOL_MESSAGE,
                      step_one.name_input_element.get_error_messages_text_list(),
                      "Name error list should have error: " + self.ERROR_SYMBOL_MESSAGE)
        self.assertTrue(self.INVALID_CIRCLE_ICON in
                        step_one.name_input_element.validation_circle_icon.getAttribute("class"),
                        "Red circle check icon should appear on the club name input")
        step_one.min_age_input_element.set_input_value(self.INVALID_MIN_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        self.assertEqual(self.VALID_MIN_AGE,
                          step_one.min_age_input_element.get_input_value(),
                          "Min age input should have value: " + self.VALID_MIN_AGE)
        step_one.max_age_input_element.set_input_value(self.INVALID_MAX_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        self.assertEqual(self.VALID_MAX_AGE,
                         step_one.max_age_input_element.get_input_value(),
                         "Max age input should have value: " + self.VALID_MAX_AGE)

        step_one.click_next_step_button()

        self.assertEqual(self.INVALID_CLUB_NAME,
                         step_one.name_input_element.get_input_value(),
                         "After next button click Name input should have invalid club name: " + self.INVALID_CLUB_NAME)
        self.assertEqual(self.VALID_MIN_AGE,
                         step_one.min_age_input_element.get_input_value(),
                         "After next button click Min age input should have age: " + self.VALID_MIN_AGE)
        self.assertEqual(self.VALID_MAX_AGE,
                         step_one.max_age_input_element.get_input_value(),
                         "After next button click Max age input should have age: " + self.VALID_MAX_AGE)

        step_one.name_input_element.clear_input().set_input_value(self.VALID_CLUB_NAME)
        self.assertTrue(self.VALID_CIRCLE_ICON in
                        step_one.name_input_element.validation_circle_icon.getAttribute("class"),
                        "Green circle check icon should appear on the club name input")

        step_one.click_on_category_by_name(self.VALID_CATEGORY)

        step_two = step_one.click_next_step_button()

        self.assertEqual(self.SECOND_STEP,
                         self.add_club_popup.get_active_step.get_attribute("innerText"),
                         "Second step should be active")

        step_two.telephone_input_element.set_input_value(self.INVALID_TELEPHONE_NUMBER)
        self.assertTrue(self.INVALID_CIRCLE_ICON in
                        step_two.telephone_input_element.validation_circle_icon.getAttribute("class"),
                        "Red circle check icon should appear on the telephone input")
        self.assertIn(self.TELEPHONE_ERROR_SYMBOL_MESSAGE,
                      step_two.telephone_input_element.get_error_messages_text_list(),
                      "Telephone error list should have error: " + self.TELEPHONE_ERROR_SYMBOL_MESSAGE)
        self.assertIn(self.TELEPHONE_ERROR_FORMAT_MESSAGE,
                      step_two.telephone_input_element.get_error_messages_text_list(),
                      "Telephone error list should have error: " + self.TELEPHONE_ERROR_FORMAT_MESSAGE)

        step_two.click_next_step_button()

        self.assertEqual(self.INVALID_TELEPHONE_NUMBER,
                         step_two.telephone_input_element.get_input_value(),
                         "After next button click Telephone input should have invalid telephone value: "
                         + self.INVALID_TELEPHONE_NUMBER)

        step_two.telephone_input_element.clear_input().set_input_value(self.VALID_TELEPHONE_NUMBER)
        self.assertTrue(self.VALID_CIRCLE_ICON in
                        step_two.telephone_input_element.validation_circle_icon.getAttribute("class"),
                        "Green circle check icon should appear on the telephone input")

        step_three = self.add_club_popup.step_two_container.click_next_step_button()
        self.assertEqual(self.THIRD_STEP,
                         self.add_club_popup.get_active_step.get_attribute("innerText"),
                         "Third step should be active")

        step_three.set_description_textarea_value(self.INVALID_DESCRIPTION)
        self.assertTrue(self.INVALID_CIRCLE_ICON in
                        step_three.textarea_validation_icon.getAttribute("class"),
                        "Red circle check icon should appear on the description textarea")
        self.assertIn(self.ERROR_SYMBOL_MESSAGE,
                      step_three.get_error_messages_text_list(),
                      "Description error list should have error: " + self.ERROR_SYMBOL_MESSAGE)

        step_three.click_complete_button()

        self.assertEqual(self.INVALID_DESCRIPTION,
                         step_three.get_description_textarea_value(),
                         "After complete button click Description textarea should have invalid description value: "
                         + self.INVALID_DESCRIPTION)

        step_three.clear_textarea().set_description_textarea_value(self.TEXT_40_SYMBOLS)
        self.assertTrue(self.VALID_CIRCLE_ICON in
                        step_three.textarea_validation_icon.getAttribute("class"),
                        "Green circle check icon should appear on the description textarea")

        self.assertTrue(self.driver.current_url == (Credentials.get_url()),
                        "Home Page should be opened after adding club")


    def test_add_club_with_valid_data(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(self.VALID_CLUB_NAME)
        step_one.click_on_category_by_name(self.VALID_CATEGORY)
        step_one.min_age_input_element.set_input_value(3)
        step_one.max_age_input_element.set_input_value(15)
        step_one.click_next_step_button()

        step_two = self.add_club_popup.step_two_container
        step_two.telephone_input_element.set_input_value(self.VALID_TELEPHONE_NUMBER)

        step_three = step_two.click_next_step_button()
        step_three.set_description_textarea_value(self.VALID_DESCRIPTION)
        self.assertTrue(step_three.complete_button.is_enabled(), "Complete button is not enabled")

    #TUA-312
    def test_display_add_club_popup(self):
        self.assertTrue(self.add_club_popup.is_open())

    # TUA-931
    def test_valid_club_name(self):
        names = ["0123456789",
                 "фЙїqfGJHdsmnФІля",
                 "!@#$%^&*()_{:\"}]'",
                 "%;?*(?:фЙїqfG123456789",
                 "1&hЦ*",
                 "123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ123Qw*&#єЇ"]
        step_one = self.add_club_popup.step_one_container

        for name in names:
            step_one.name_input_element.set_input_value(name)
            self.assertEqual(step_one.name_input_element.validation_circle_icon.value_of_css_property("color"), "rgba(82, 196, 26, 1)")

            step_one.name_input_element.clear_input()
            self.assertEqual(step_one.name_input_element.validation_circle_icon.value_of_css_property("color"), "rgba(255, 77, 79, 1)")
            self.assertEqual(step_one.name_input_element.get_error_messages_text_list()[0], "Введіть назву гуртка")

    def test_check_validation_icon_with_valid_data_for_description_field(self):
        self.fill_step_one_with_valid_data_preconditions()
        self.fill_step_two_with_valid_data_preconditions()
        step_three = self.add_club_popup.step_three_container
        for valid_value, error_message in self.valid_description_textarea_value():
            with self.subTest(description=f"Testing description text area with text: {valid_value}"):
                step_three.clear_textarea().set_description_textarea_value(valid_value)
                self.assertTrue(self.VALID_CIRCLE_ICON in step_three.textarea_validation_icon.getAttribute("class"),
                                error_message)

