from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter


class LanguageSphereFacebookPage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self.locators = {
            "facebook_logo": ("xpath", "//body//a[@aria-label=\"Facebook\"]"),
            "initiative_heading": ("xpath", "//body//span[contains(text(),'Сімейний фестиваль \"Мовосфера\"')]"),
        }

    @property
    def facebook_logo(self) -> WebElement:
        return self._driver.find_element(*self.locators["facebook_logo"])

    @property
    def initiative_heading(self) -> WebElement:
        return self._driver.find_element(*self.locators["initiative_heading"])
