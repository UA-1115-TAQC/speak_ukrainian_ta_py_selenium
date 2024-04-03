from selenium.webdriver.remote.webelement import WebElement

from src.ui.pages.base_pages.base_page import BasePage


class ApplicationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "title": ("xpath", "descendant::div[contains(@class, 'contentTitle')]"),
            "search_input": ("xpath", "descendant::input[contains(@class, 'searchBox')]"),
            "statuses_dropdown": ("xpath", ".//div[contains(@class, 'filterSelectStatuses')]//span[contains(., "
                                           "'статуси')]/.."),
            "applications_dropdown": ("xpath", ".//div[contains(@class, 'filterSelectStatuses')]//span[contains(., "
                                               "'заявки')]/.."),
            "clubs_dropdown": ("xpath", ".//div[contains(@class, 'filterSelectRight')]"),
            "no_applications_title": ("xpath", ".//div[contains(@class, 'noRegistrations')]"),
            "all_radio_button": ("xpath", "//label[contains(@class, 'ant-radio-wrapper ')]//span[contains(text(), 'Всі')]"),
            "not_confirmed_radio_button": ("xpath", "//label[contains(@class, 'ant-radio-wrapper ')]//span[contains(text(), 'Не підтверджені')]")
        }

    def search_input_send_keys(self, keys):
        self.search_input.send_keys(keys)

    def statuses_dropdown_click(self):
        self.statuses_dropdown.click()

    def applications_dropdown_click(self):
        self.applications_dropdown.click()

    def clubs_dropdown_click(self):
        self.clubs_dropdown.click()

    def all_radio_button_click(self):
        self.all_radio_button.click()

    def not_confirmed_radio_button_click(self):
        self.not_confirmed_radio_button.click()
