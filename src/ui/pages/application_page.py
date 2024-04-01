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

    @property
    def title(self) -> WebElement:
        return self.node.find_elements(*self.locators["title"])

    @property
    def search_input(self) -> WebElement:
        return self.node.find_elements(*self.locators["search_input"])

    def search_input_send_keys(self, keys):
        self.search_input.send_keys(keys)

    @property
    def statuses_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["statuses_dropdown"])

    def statuses_dropdown_click(self):
        self.statuses_dropdown.click()

    @property
    def applications_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["applications_dropdown"])

    def applications_dropdown_click(self):
        self.applications_dropdown.click()

    @property
    def clubs_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["clubs_dropdown"])

    def clubs_dropdown_click(self):
        self.clubs_dropdown.click()

    @property
    def no_applications_title(self) -> WebElement:
        return self.node.find_elements(*self.locators["no_applications_title"])

    @property
    def all_radio_button(self) -> WebElement:
        return self.node.find_elements(*self.locators["all_radio_button"])

    def all_radio_button_click(self):
        self.all_radio_button.click()

    @property
    def not_confirmed_radio_button(self) -> WebElement:
        return self.node.find_elements(*self.locators["not_confirmed_radio_button"])

    def not_confirmed_radio_button_click(self):
        self.not_confirmed_radio_button.click()
