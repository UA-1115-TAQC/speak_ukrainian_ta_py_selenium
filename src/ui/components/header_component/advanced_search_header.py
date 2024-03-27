from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.ui.components.header_component.advanced_search_tooltip import AdvancedSearchToolTip
from src.ui.components.base_component import BaseComponent


class AdvancedSearchHeaderComponent(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self._driver = driver
        self._node = node
        self.locators = {
            "advanced_search_text_heading": ("xpath", "//h2[@class=\'city-name\']"),
            "selection_search_input_field": ("xpath", '//div[contains(@class, "search")]//input[@type="search"]'),
            "selection_search_input_field_placeholder": ("xpath", '//span[@class=\'ant-select-selection-placeholder\']'),
            "search_icon": ("xpath", '//div[contains(@class, "search-icon-group")]/span[@aria-label="search"]'),
            "advanced_search_icon": ("xpath", '//div[contains(@class, "search-icon-group")]/span[@aria-label="control"]'),
            "advanced_search_tooltip_node": ("xpath", '//div[contains(@class, "rc-virtual-list-holder-inner")]'),
            "selection_search_close_button": ("xpath", '//span[@aria-label="close-circle"]'),
            "show_on_map_button": ("xpath", ".//button[contains(@class,'show-map-button')]"),
        }

    @property
    def advanced_search_text_heading(self) -> WebElement:
        return self._node.find_element(*self.locators["advanced_search_text_heading"])

    @property
    def selection_search_input_field(self) -> WebElement:
        return self._node.find_element(*self.locators["selection_search_input_field"])

    @property
    def selection_search_input_field_placeholder(self) -> WebElement:
        return self._node.find_element(*self.locators["selection_search_input_field_placeholder"])

    @property
    def search_icon(self) -> WebElement:
        return self._node.find_element(*self.locators["search_icon"])

    @property
    def advanced_search_icon(self) -> WebElement:
        return self._node.find_element(*self.locators["advanced_search_icon"])

    @property
    def selection_search_close_button(self) -> WebElement:
        return self._node.find_element(*self.locators["selection_search_close_button"])

    @property
    def advanced_search_tooltip_node(self) -> WebElement:
        return self._node.find_element(*self.locators["advanced_search_tooltip_node"])

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

    def click_selection_search_close_button(self):
        if self.get_text_selection_search_input_field() is not None:
            self.selection_search_close_button.click()
            return self
        else:
            raise ValueError("You haven't entered any text")


class AdvancedSearchClubsHeaderComponent(AdvancedSearchHeaderComponent):

    def __init__(self, driver, node):
        super().__init__(driver, node)
        self._show_on_map_button = None

    @property
    def show_on_map_button(self):
        return self._node.find_element(*self.locators["show_on_map_button"])

    def click_show_on_map_button(self):
        self.show_on_map_button.click()
