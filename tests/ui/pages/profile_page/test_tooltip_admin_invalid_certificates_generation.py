from selenium.webdriver import  Keys
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.pages.home_page.home_page import HomePage
from tests.base_test_runner import LogInWithAdminTestRunner
from selenium.webdriver.support import expected_conditions as EC


class TestInvalidCertificatesGetToolTipWithAdmin(LogInWithAdminTestRunner):

    def setUp(self):
        super().setUp()
        self.admin_generate_certificate_page = (HomePage(self.driver).header.open_admin_menu()
                                                .open_content_popup().open_certificates_submenu_popup()
                                                .click_generate_certificate())
        self.wait = WebDriverWait(self.driver, 30)

    def invalid_values(self):
        return [
            ("1000", "999"),
            ("1300", "999"),
            ("0", "1")
        ]
    # Verify that the Admin can't continue generating certificates with an invalid value
    # in the 'Тривалість навчання' field and will receive a tooltip
    def test_invalid_certificates_get_tool_tip(self):
        for input_value, expected_value in self.invalid_values():
            self.enter_invalid_value(input_value)
            study_duration_input = self.admin_generate_certificate_page.study_duration_input
            self.admin_generate_certificate_page.study_duration_label.click()
            self.wait.until(lambda driver: input_value not in self.admin_generate_certificate_page.study_duration_input.get_attribute("value"))
            updated_value = study_duration_input.get_attribute("value")
            self.assertTrue(updated_value is not None and expected_value in updated_value,
                            f"The duration input accepts an invalid value {input_value}")

    def clear_input_field(self, input_field):
        input_field.send_keys(Keys.COMMAND + "a")
        input_field.send_keys(Keys.DELETE)

    def enter_invalid_value(self, value):
        study_duration_input = self.admin_generate_certificate_page.study_duration_input
        current_value = study_duration_input.get_attribute("value")

        if current_value is not None and current_value != "":
            self.clear_input_field(study_duration_input)

        study_duration_input.send_keys(value)
        updated_value = study_duration_input.get_attribute("value")
        self.assertTrue(updated_value is not None and value in updated_value,
                        "The entered value isn't present in the duration input")
