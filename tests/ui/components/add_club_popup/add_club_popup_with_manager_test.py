from selenium.webdriver import Keys

from tests.base_test_runner import LogInWithManagerTestRunner
from tests.utils.config_properties import ConfigProperties


class AddClubPopUpWithManagerTest(LogInWithManagerTestRunner):
    VALID_CLUB_NAME = "Add club name 2"
    CATEGORY = "Спортивні секції"
    VALID_MIN_AGE = "5"
    VALID_MAX_AGE = "8"
    VALID_TELEPHONE_NUMBER = "0987656453"
    TEXT_50_SYMBOLS = "Abcd " * 10
    VALID_CIRCLE_ICON = "check-circle"
    INVALID_CIRCLE_ICON = "close-circle"
    ERROR_MESSAGE = "Некоректний опис гуртка"

    def setUp(self):
        super().setUp()
        self.add_club_popup = self.homepage.header.add_club_click()
        self.add_club_popup.wait_popup_open(5)

    def fill_step_one(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(self.VALID_CLUB_NAME)
        step_one.click_on_category_by_name(self.CATEGORY)
        step_one.min_age_input_element.set_input_value(self.VALID_MIN_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.max_age_input_element.set_input_value(self.VALID_MAX_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.click_next_step_button()

    def fill_step_two(self):
        step_two = self.add_club_popup.step_two_container
        step_two.telephone_input_element.set_input_value(self.VALID_TELEPHONE_NUMBER)
        step_two.click_next_step_button()

    def test_check_when_add_club_textarea_field_is_blank(self):
        self.fill_step_one()
        self.fill_step_two()

        step_three = self.add_club_popup.step_three_container
        step_three.clear_textarea()
        step_three.click_complete_button()

        self.assertEqual(step_three.get_error_messages_text_list()[0], self.ERROR_MESSAGE,
                         f"[STEP_THREE] Shown error message : {self.ERROR_MESSAGE}. "
                         f"Message under description textarea")
        self.assertTrue(self.INVALID_CIRCLE_ICON in
                        step_three.textarea_validation_icon.getAttribute("class"),
                        "[STEP_THREE] Red circle appeared in right side on the description textarea")


    def test_club_without_center_created(self):
        test_image = "harrybean.jpg"

        self.fill_step_one()
        self.fill_step_two()

        step_three = self.add_club_popup.step_three_container
        step_three.click_logo_download_button()
        path = ConfigProperties.get_image_path(test_image)
        step_three.upload_logo(path)
