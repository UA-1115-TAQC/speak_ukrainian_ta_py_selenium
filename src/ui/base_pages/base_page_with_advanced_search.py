from selenium import webdriver
from src.ui.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
from selenium.webdriver.common.by import By

from src.ui.pages.base_page import BasePage

ADVANCED_SEARCH_HEADER = (By.XPATH, '//div[contains(@class, "lower-header-box")]')


class BasePageWithAdvancedSearch(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.advanced_search_header = AdvancedSearchHeaderComponent(self.driver.find_element(*ADVANCED_SEARCH_HEADER))
