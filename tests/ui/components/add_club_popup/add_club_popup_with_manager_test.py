from selenium.webdriver import Keys

from tests.base_test_runner import LogInWithManagerTestRunner
from tests.utils.config_properties import ConfigProperties


class AddClubPopUpWithManagerTest(LogInWithManagerTestRunner):
    VALID_CLUB_NAME = "Add club name 5"
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
        step_one = self.add_club_popup.step_one_container
        self.assertTrue(step_one.name_input_element.get_input_value() == "")

        categories = step_one.categories_node_list
        self.assertFalse(categories[0].is_selected(),
                         f"{categories[0].get_attribute("value")} is not selected")
        self.assertFalse(categories[1].is_selected(),
                         f"{categories[1].get_attribute("value")} is not selected")
        self.assertFalse(categories[2].is_selected(),
                         f"{categories[2].get_attribute("value")} is not selected")
        self.assertFalse(categories[3].is_selected(),
                         f"{categories[3].get_attribute("value")} is not selected")
        self.assertFalse(categories[4].is_selected(),
                         f"{categories[4].get_attribute("value")} is not selected")
        self.assertFalse(categories[5].is_selected(),
                         f"{categories[5].get_attribute("value")} is not selected")
        self.assertFalse(categories[6].is_selected(),
                         f"{categories[6].get_attribute("value")} is not selected")
        self.assertFalse(categories[7].is_selected(),
                         f"{categories[7].get_attribute("value")} is not selected")
        self.assertFalse(categories[8].is_selected(),
                         f"{categories[8].get_attribute("value")} is not selected")
        self.assertFalse(categories[9].is_selected(),
                         f"{categories[9].get_attribute("value")} is not selected")
        self.assertFalse(categories[10].is_selected(),
                         f"{categories[10].get_attribute("value")} is not selected")
        self.assertTrue(step_one.min_age_input_element.get_input_value() == "",
                        "Min age input should be empty")
        self.assertTrue(step_one.max_age_input_element.get_input_value() == "",
                        "Max age input should be empty")
        self.assertTrue(step_one.dropdown_placeholder_text() == "Назва центру",
                        "Default inner text is Назва центру")

        self.fill_step_one()

        step_two = self.add_club_popup.step_two_container
        work_days = step_two.work_days_list
        self.assertFalse(work_days[0].is_selected(), f"{work_days[0]} is not selected")
        self.assertFalse(work_days[1].is_selected(), f"{work_days[1]} is not selected")
        self.assertFalse(work_days[2].is_selected(), f"{work_days[2]} is not selected")
        self.assertFalse(work_days[3].is_selected(), f"{work_days[3]} is not selected")
        self.assertFalse(work_days[4].is_selected(), f"{work_days[4]} is not selected")
        self.assertFalse(work_days[5].is_selected(), f"{work_days[5]} is not selected")
        self.assertFalse(work_days[6].is_selected(), f"{work_days[6]} is not selected")

        self.assertTrue(step_two.telephone_input_element.get_input_value() == "",
                        "Telephone input is empty")
        self.assertTrue(step_two.facebook_input_element.get_input_value() == "",
                        "Facebook input is empty")
        self.assertTrue(step_two.whatsapp_input_element.get_input_value() == "",
                        "Whatsapp input is empty")
        self.assertTrue(step_two.skype_input_element.get_input_value() == "",
                        "Skype input is empty")
        self.assertTrue(step_two.site_input_element.get_input_value() == "",
                        "Skype input is empty")

        self.fill_step_two()

        step_three = self.add_club_popup.step_three_container
        self.assertTrue(step_three.get_description_textarea_value() == "",
                        "Description textarea is empty")

        step_three.click_logo_download_button()
        step_three.upload_logo(ConfigProperties.get_image_path(test_image))
        step_three.logo_uploaded_img_element.wait_image_loaded(5)
        self.assertTrue(step_three.logo_uploaded_img_element.is_displayed(),
                        f"Logo uploaded image name is : {test_image}")

        step_three.click_cover_download_button()
        step_three.upload_cover(ConfigProperties.get_image_path(test_image))
        step_three.cover_uploaded_img_element.wait_image_loaded(5)
        self.assertTrue(step_three.cover_uploaded_img_element.is_displayed(),
                        f"Cover uploaded image name is : {test_image}")

        step_three.click_gallery_download_button()
        step_three.upload_img_to_gallery(ConfigProperties.get_image_path(test_image))
        step_three.click_gallery_download_button()
        step_three.upload_img_to_gallery(ConfigProperties.get_image_path(test_image))
        self.assertEqual(len(step_three.get_list_of_gallery_image_elements()), 2,
                         "Should be uploaded 2 images")

        step_three.set_description_textarea_value(self.TEXT_50_SYMBOLS)
        self.assertTrue(step_three.get_error_messages_text_list() == [])
        step_three.click_complete_button()
