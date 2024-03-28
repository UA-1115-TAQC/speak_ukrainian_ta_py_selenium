from selenium.webdriver import Keys

from src.ui.components.add_club_popup.add_club_step_three import AddClubStepThree
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubSider
from tests.base_test_runner import LogInWithManagerTestRunner


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
