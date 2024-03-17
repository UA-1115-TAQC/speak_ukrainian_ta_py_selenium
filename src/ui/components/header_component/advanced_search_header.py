from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent

ADVANCED_SEARCH_TEXT_HEADING = (By.XPATH, '//h2[@class=\'city-name\']')
SELECTION_SEARCH_INPUT_FIELD = (By.XPATH, '//div[contains(@class, "search")]//input[@type="search"]')
SELECTION_SEARCH_INPUT_FIELD_PLACEHOLDER = (By.XPATH, '//span[@class=\'ant-select-selection-placeholder\']')
SEARCH_ICON = (By.XPATH, '//div[contains(@class, "search-icon-group")]/span[@aria-label="search"]')
ADVANCED_SEARCH_ICON = (By.XPATH, '//div[contains(@class, "search-icon-group")]/span[@aria-label="control"]')
SEARCH_INPUT_CLOSE_BUTTON = (By.XPATH, '//span[@aria-label="close-circle"]')
ADVANCED_SEARCH_TOOLTIP_NODE = (By.XPATH, '//div[contains(@class, "rc-virtual-list-holder-inner")]')
SELECTION_SEARCH_CLOSE_BUTTON = (By.XPATH, '//span[@aria-label="close-circle"]')


class AdvancedSearchHeaderComponent(BaseComponent):
    def __init__(self,  driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self.driver = driver

    def get_text_selection_search_input_field(self) -> str:
        return self.node.find_element(*SELECTION_SEARCH_INPUT_FIELD).get_attribute("value")

    def set_text_selection_search_input_field(self, text):
        expected_input = self.get_text_selection_search_input_field() + text
        self.node.find_element(*SELECTION_SEARCH_INPUT_FIELD).send_keys(text)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_text_selection_search_input_field() == expected_input
        )
        return self

    def click_selection_search_input_field(self):
        self.node.find_element(*SELECTION_SEARCH_INPUT_FIELD).click()
        # return AdvancedSearchTooltip(self.driver, self.node.find_element(*ADVANCED_SEARCH_TOOLTIP_NODE))

    def click_search_icon(self):
        self.node.find_element(*SEARCH_ICON).click()
        return self

    def click_advanced_search_icon(self):
        self.node.find_element(*ADVANCED_SEARCH_ICON).click()

    # return ClubsPage(self.driver).wait_until_clubs_page_is_loaded(30)

    def click_selection_search_close_button(self):
        if self.get_text_selection_search_input_field() is not None:
            self.node.find_element(*SELECTION_SEARCH_CLOSE_BUTTON).click()
            return self
        else:
            raise ValueError("You haven't entered any text")
