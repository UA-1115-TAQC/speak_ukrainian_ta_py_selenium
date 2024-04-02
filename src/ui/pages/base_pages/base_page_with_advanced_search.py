from selenium import webdriver
from selenium.webdriver.common.by import By

from src.ui.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
from src.ui.pages.base_pages.base_page import BasePage

ADVANCED_SEARCH_HEADER = (By.XPATH, '//div[contains(@class, "lower-header-box")]')


class BasePageWithAdvancedSearch(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)

    @property
    def advanced_search_header_component(self) -> AdvancedSearchHeaderComponent:
        return AdvancedSearchHeaderComponent(self.driver.find_element(*ADVANCED_SEARCH_HEADER))
