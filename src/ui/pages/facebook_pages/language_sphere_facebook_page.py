from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter

FACEBOOK_LOGO = (By.XPATH, "//body//a[@aria-label=\"Facebook\"]")
INITIATIVE_HEADING = (By.XPATH, "//body//span[contains(text(),'Сімейний фестиваль \"Мовосфера\"')]")


class LanguageSphereFacebookPage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self._facebook_logo = None
        self._initiative_heading = None

    @property
    def facebook_logo(self) -> WebElement:
        if not self._facebook_logo:
            self._facebook_logo = self._driver.find_element(*FACEBOOK_LOGO)
        return self._facebook_logo

    @property
    def initiative_heading(self) -> WebElement:
        if not self._initiative_heading:
            self._initiative_heading = self._driver.find_element(*INITIATIVE_HEADING)
        return self._initiative_heading
