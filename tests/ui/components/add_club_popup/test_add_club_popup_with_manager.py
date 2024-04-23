from selenium.webdriver import Keys

from src.ui.components.add_club_popup.add_club_step_three import AddClubStepThree
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubSider
from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.pages.profile_page import ProfilePage
from tests.base_test_runner import LogInWithManagerTestRunner
from tests.utils.config_properties import ConfigProperties


class AddClubPopUpWithManagerTest(LogInWithManagerTestRunner):
    VALID_CLUB_NAME = "New Club Name"
    VALID_CATEGORY = "Спортивні секції"
    VALID_MIN_AGE = "4"
    VALID_MAX_AGE = "8"
    VALID_CENTER_NAME = "INVENTOR СТЕМ-Школа"
    VALID_TELEPHONE_NUMBER = "0987656453"
    VALID_CIRCLE_ICON = "check-circle"
    SECOND_STEP = "2"
    THIRD_STEP = "3"
    TEXT_40_SYMBOLS = "Abc " * 10
    INVALID_CIRCLE_ICON = "close-circle"
    ERROR_MESSAGE = "Некоректний опис гуртка"
    INVALID_DESCRIPTION = "Blaэ blъa teät ödesciption"
    ERROR_RUSSIAN_LETTERS_MESSAGE = "Опис гуртка не може містити російські літери"
    VALID_DESCRIPTION = "Lorem ipsum dolor sit amet orci aliquam."

    def setUp(self):
        super().setUp()
        self.add_club_popup = self.homepage.header.add_club_click()
        self.add_club_popup.wait_popup_open(5)

    def fill_step_one_mandatory_fields_with_valid_data(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(self.VALID_CLUB_NAME)
        step_one.click_on_category_by_name(self.VALID_CATEGORY)
        step_one.min_age_input_element.set_input_value(self.VALID_MIN_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.max_age_input_element.set_input_value(self.VALID_MAX_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.click_next_step_button()

    def fill_step_two_mandatory_fields_with_valid_data(self):
        step_two = self.add_club_popup.step_two_container
        step_two.telephone_input_element.set_input_value(self.VALID_TELEPHONE_NUMBER)
        step_two.click_next_step_button()

    def check_step_three_description_elements_present(self, sider: AddClubSider, step_three: AddClubStepThree):
        self.assertTrue(sider.step_one.step_icon.is_displayed(), "Step One icon should be displayed")
        self.assertTrue(sider.step_one.step_title.is_displayed(), "Step One title should be displayed")

        self.assertTrue(sider.step_two.step_icon.is_displayed(), "Step Two icon should be displayed")
        self.assertTrue(sider.step_two.step_title.is_displayed(), "Step Two title should be displayed")

        self.assertTrue(sider.step_three.step_icon.is_displayed(), "Step Three icon should be displayed")
        self.assertTrue(sider.step_three.step_title.is_displayed(), "Step Three title should be displayed")

        self.assertTrue(step_three.club_popup_title.is_displayed(), "Step Club title should be displayed")

        self.assertTrue(step_three.club_logo_title.is_displayed(), "Step Logo title should be displayed")
        self.assertTrue(step_three.logo_download_button.is_displayed(),
                        "Step Logo Download Button should be displayed")

        self.assertTrue(step_three.club_cover_title.is_displayed(), "Step Cover title should be displayed")
        self.assertTrue(step_three.cover_download_button.is_displayed(),
                        "Step Cover Download Button should be displayed")

        self.assertTrue(step_three.club_gallery_title.is_displayed(), "Step Gallery title should be displayed")
        self.assertTrue(step_three.gallery_download_button.is_displayed(),
                        "Step Gallery Download Button should be displayed")

        self.assertTrue(step_three.description_title.is_displayed(), "Step Description title should be displayed")
        self.assertTrue(step_three.description_textarea.is_displayed(),
                        "Step Description textarea should be displayed")

        self.assertTrue(step_three.previous_step_button.is_displayed(),
                        "Step Previous Step Button should be displayed")
        self.assertTrue(step_three.complete_button.is_displayed(), "Step Submit Button should be displayed")

    #TUA-119
    def test_step_three_description_ui(self):
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 600

        self.fill_step_one_mandatory_fields_with_valid_data()
        self.fill_step_two_mandatory_fields_with_valid_data()

        step_three = self.add_club_popup.step_three_container
        sider = self.add_club_popup.sider_element

        self.check_step_three_description_elements_present(sider, step_three)

        self.assertEqual("check", sider.step_one.step_success_icon.get_attribute("aria-label"))
        self.assertEqual("Основна інформація", sider.step_one.step_title.text)
        self.assertEqual("check", sider.step_two.step_success_icon.get_attribute("aria-label"))
        self.assertEqual("Контакти", sider.step_two.step_title.text)
        self.assertEqual("3", sider.step_three.step_icon.text)
        self.assertEqual("Опис", sider.step_three.step_title.text, )

        self.assertEqual("Додати гурток", step_three.club_popup_title.text)
        self.assertEqual("rgba(45, 76, 104, 1)", step_three.club_popup_title.value_of_css_property("color"))
        self.assertEqual("24px", step_three.club_popup_title.value_of_css_property("font-size"))

        self.assertEqual("Логотип", step_three.club_logo_title.text)
        self.assertEqual("rgba(128, 128, 128, 1)", step_three.club_logo_title.value_of_css_property("color"))
        self.assertEqual("19px", step_three.club_logo_title.value_of_css_property("font-size"))
        self.assertEqual("Завантажити лого", step_three.logo_download_button.text)

        self.assertEqual("Обкладинка", step_three.club_cover_title.text)
        self.assertEqual("rgba(128, 128, 128, 1)", step_three.club_cover_title.value_of_css_property("color"))
        self.assertEqual("19px", step_three.club_cover_title.value_of_css_property("font-size"))
        self.assertEqual("Завантажити обкладинку", step_three.cover_download_button.text)

        self.assertEqual("Галерея", step_three.club_gallery_title.text)
        self.assertEqual("rgba(128, 128, 128, 1)", step_three.club_gallery_title.value_of_css_property("color"))
        self.assertEqual("19px", step_three.club_gallery_title.value_of_css_property("font-size"))
        self.assertEqual("Додати", step_three.gallery_download_button.text)

        self.assertEqual("Опис", step_three.description_title.text)
        self.assertEqual("rgba(128, 128, 128, 1)", step_three.description_title.value_of_css_property("color"))
        self.assertEqual("19px", step_three.description_title.value_of_css_property("font-size"), )

        self.assertEqual("Назад", step_three.previous_step_button.text)
        self.assertEqual("Завершити", step_three.complete_button.text)
        self.assertFalse(step_three.complete_button.is_enabled(), "Button should be not active")

        actions = step_three.get_actions()
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.logo_download_button == self.driver.switch_to.active_element,
                        "Focus should be on Logo Download Button")
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.cover_download_button == self.driver.switch_to.active_element,
                        "Focus should be on Cover Download Button")
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.gallery_download_button == self.driver.switch_to.active_element,
                        "Focus should be on Gallery Download Button")
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.description_textarea == self.driver.switch_to.active_element,
                        "Focus should be on Description Textarea")
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.previous_step_button == self.driver.switch_to.active_element,
                        "Focus should be on Previous Step Button")
        actions.send_keys(Keys.TAB).perform()
        self.assertTrue(step_three.complete_button == self.driver.switch_to.active_element,
                        "Focus should be on Submit Button")

        self.driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.check_step_three_description_elements_present(sider, step_three)

    def test_check_when_add_club_textarea_field_is_blank(self):
        self.fill_step_one_mandatory_fields_with_valid_data()
        self.fill_step_two_mandatory_fields_with_valid_data()

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
        self.assertTrue(step_one.center_dropdown_element.get_dropdown_placeholder_text() == "Назва центру",
                        "Default inner text is Назва центру")

        self.fill_step_one_mandatory_fields_with_valid_data()

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

        self.fill_step_two_mandatory_fields_with_valid_data()

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

        step_three.set_description_textarea_value(self.TEXT_40_SYMBOLS)
        self.assertTrue(step_three.get_error_messages_text_list() == [])
        step_three.click_complete_button()

    def test_check_russian_language_error(self):
        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element = self.VALID_CLUB_NAME
        step_one.click_on_category_by_name(self.VALID_CATEGORY)
        step_one.min_age_input_element = self.VALID_MIN_AGE
        step_one.max_age_input_element = self.VALID_MAX_AGE
        step_one.click_next_step_button()

        step_two = self.add_club_popup.step_two_container
        step_two.telephone_input_element = self.VALID_TELEPHONE_NUMBER
        step_three = step_two.click_next_step_button

        step_three.set_description_textarea_value(self.INVALID_DESCRIPTION)
        self.assertEqual(step_three.get_description_textarea_value, self.ERROR_RUSSIAN_LETTERS_MESSAGE)

    # TUA-173
    def test_description_valid_data(self):
        descriptions = ["Lorem ipsum dolor sit amet consectetur efficitur",
                        "123 Lorem ipsum dolor 456 sit amet consectetur 789",
                        "!\\\"Lorem!#$%&'()*+ipsum,-./:;<=>?@dolor[]^_`{}~"]
        self.fill_step_one_mandatory_fields_with_valid_data()
        self.fill_step_two_mandatory_fields_with_valid_data()
        step_three = self.add_club_popup.step_three_container

        for description in descriptions:
            step_three.set_description_textarea_value(description)
            self.assertTrue(not step_three.error_messages_list)
            self.assertEqual(step_three.textarea_validation_icon.value_of_css_property("color"), "rgba(82, 196, 26, 1)")
            step_three.clear_textarea()

    # TUA-250
    def test_error_invalid_address_add_location(self):
        addresses = ["Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean ma",
                "абвг",
                "абвгдъ",
                "абвгдё",
                "абвгдэ",
                "абвгды"]
        self.fill_step_one_mandatory_fields_with_valid_data()
        step_two = self.add_club_popup.step_two_container
        add_location = step_two.click_add_location_button()
        add_location.name_input_element.set_input_value("Lorem")
        add_location.city_dropdown_element.click_dropdown().select_item("Одеса")
        add_location.district_dropdown_element.click_dropdown().select_item("Малиновський")
        add_location.metro_dropdown_element.click_dropdown().select_item("Фонтан")

        for address in addresses:
            add_location.address_input_element.set_input_value(address)
            self.assertEqual(add_location.address_input_element.get_error_messages_text_list()[0], "Некоректна адреса")

            add_location.address_input_element.clear_input_with_wait()
            (self.assertEqual(add_location.address_input_element.get_error_messages_text_list()[0]+
                              "\n"+
                              add_location.address_input_element.get_error_messages_text_list()[1],
                "Це поле є обов'язковим\nНекоректна адреса"))

    # TUA-923
    def test_default_icon_is_set(self):
        new_club_name = "Club With Default Icon"

        step_one = self.add_club_popup.step_one_container
        step_one.name_input_element.set_input_value(new_club_name)
        step_one.click_on_category_by_name(self.VALID_CATEGORY)
        step_one.min_age_input_element.set_input_value(self.VALID_MIN_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.max_age_input_element.set_input_value(self.VALID_MAX_AGE)
        step_one.get_actions().send_keys(Keys.TAB).perform()
        step_one.click_next_step_button()

        self.fill_step_two_mandatory_fields_with_valid_data()

        step_three = self.add_club_popup.step_three_container
        step_three.set_description_textarea_value(self.VALID_DESCRIPTION)
        step_three.click_complete_button()

        new_club = self.get_club_added_club(new_club_name)
        if not new_club:
            self.assertTrue(False, "Club was not added")

        logo_src = new_club.get_logo_src()

        new_club.click_more_button()
        new_club.click_delete_club()

        self.assertNotEqual(logo_src, None)

    def get_club_added_club(self, club_name):
        while True:
            profile_page = ProfilePage(self.driver)
            clubs = profile_page.club_cards_list()

            for club in clubs:
                if club.get_name_text() == club_name:
                    return club

            pagination = profile_page.switch_pagination_web_element
            if not pagination or pagination.is_next_disabled():
                return None
            pagination.click_next()
