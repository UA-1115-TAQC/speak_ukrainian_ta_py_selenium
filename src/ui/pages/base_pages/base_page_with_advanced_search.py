from selenium import webdriver
from src.ui.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
from selenium.webdriver.common.by import By

from src.ui.pages.base_pages.base_page import BasePage

ADVANCED_SEARCH_HEADER = (By.XPATH, '//div[contains(@class, "lower-header-box")]')


class BasePageWithAdvancedSearch(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self._advanced_search_header = None

    def get_advanced_search_header_component(self) -> AdvancedSearchHeaderComponent:
        if not self._advanced_search_header:
            self._advanced_search_header = AdvancedSearchHeaderComponent(self._driver, self._driver
                                                                        .find_element(*ADVANCED_SEARCH_HEADER))
        return self._advanced_search_header
