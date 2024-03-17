from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.ui.components.header_component.advanced_search_tooltip import AdvancedSearchToolTip

from src.ui.components.base_component import BaseComponent

ADVANCED_SEARCH_TEXT_HEADING = (By.XPATH, '//h2[@class=\'city-name\']')
SELECTION_SEARCH_INPUT_FIELD = (By.XPATH, '//div[contains(@class, "search")]//input[@type="search"]')
SELECTION_SEARCH_INPUT_FIELD_PLACEHOLDER = (By.XPATH, '//span[@class=\'ant-select-selection-placeholder\']')
SEARCH_ICON = (By.XPATH, '//div[contains(@class, "search-icon-group")]/span[@aria-label="search"]')
ADVANCED_SEARCH_ICON = (By.XPATH, '//div[contains(@class, "search-icon-group")]/span[@aria-label="control"]')
ADVANCED_SEARCH_TOOLTIP_NODE = (By.XPATH, '//div[contains(@class, "rc-virtual-list-holder-inner")]')
SELECTION_SEARCH_CLOSE_BUTTON = (By.XPATH, '//span[@aria-label="close-circle"]')


class AdvancedSearchHeaderComponent(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self._driver = driver
        self._advanced_search_text_heading = None
        self._selection_search_input_field = None
        self._selection_search_input_field_placeholder = None
        self._search_icon = None
        self._advanced_search_icon = None
        self._advanced_search_tooltip_node = None
        self._selection_search_close_button = None

    @property
    def advanced_search_text_heading(self) -> WebElement:
        if not self._advanced_search_text_heading:
            self._advanced_search_text_heading = self.node.find_element(*ADVANCED_SEARCH_TEXT_HEADING)
        return self._advanced_search_text_heading

    @property
    def selection_search_input_field(self) -> WebElement:
        if not self._selection_search_input_field:
            self._selection_search_input_field = self.node.find_element(*SELECTION_SEARCH_INPUT_FIELD)
        return self._selection_search_input_field

    @property
    def selection_search_input_field_placeholder(self) -> WebElement:
        if not self._selection_search_input_field_placeholder:
            self._selection_search_input_field_placeholder = self.node.find_element(
                *SELECTION_SEARCH_INPUT_FIELD_PLACEHOLDER)
        return self._selection_search_input_field_placeholder

    @property
    def search_icon(self) -> WebElement:
        if not self._search_icon:
            self._search_icon = self.node.find_element(*SEARCH_ICON)
        return self._search_icon

    @property
    def advanced_search_icon(self) -> WebElement:
        if not self._advanced_search_icon:
            self._advanced_search_icon = self.node.find_element(*ADVANCED_SEARCH_ICON)
        return self._advanced_search_icon

    @property
    def selection_search_close_button(self) -> WebElement:
        if not self._selection_search_close_button:
            self._selection_search_close_button = self.node.find_element(*SELECTION_SEARCH_CLOSE_BUTTON)
        return self._selection_search_close_button

    @property
    def advanced_search_tooltip_node(self) -> WebElement:
        if not self._advanced_search_tooltip_node:
            self._advanced_search_tooltip_node = self.node.find_element(*ADVANCED_SEARCH_TOOLTIP_NODE)
        return self._advanced_search_tooltip_node

    def get_text_selection_search_input_field(self) -> str:
        return self.selection_search_input_field.get_attribute("value")

    def set_text_selection_search_input_field(self, text):
        expected_input = self.get_text_selection_search_input_field() + text
        self.selection_search_input_field.send_keys(text)
        WebDriverWait(self._driver, 10).until(
            lambda driver: self.get_text_selection_search_input_field() == expected_input
        )
        return self

    def click_selection_search_input_field(self) -> AdvancedSearchToolTip:
        self.selection_search_input_field.click()
        return AdvancedSearchToolTip(self._driver, self.advanced_search_tooltip_node)

    def click_search_icon(self):
        self.search_icon.click()
        return self

    def click_advanced_search_icon(self):
        self.advanced_search_icon.click()

    # return ClubsPage(self.driver).wait_until_clubs_page_is_loaded(30)

    def click_selection_search_close_button(self):
        if self.get_text_selection_search_input_field() is not None:
            self.selection_search_close_button.click()
            return self
        else:
            raise ValueError("You haven't entered any text")
