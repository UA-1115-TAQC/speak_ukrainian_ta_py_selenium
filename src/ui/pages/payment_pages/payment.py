from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter

INITIATIVE_HEADER_PATH = "//div[contains(@class,\"header\")]"
INITIATIVE_DESCRIPTION_PATH = "//div[contains(@class,\"description\")]"


class Payment(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self.locators = {
            "large_logo_image": ("xpath", INITIATIVE_HEADER_PATH + "//div[contains(@class,\"large\")]"),
            "initiative_title": ("xpath", INITIATIVE_HEADER_PATH + "//div[contains(@class,\"title\")]"),
            "initiative_description": ("xpath", INITIATIVE_DESCRIPTION_PATH + "//p[not (contains(text(),\"http\"))]"),
            "initiative_video_link_text": ("xpath", INITIATIVE_DESCRIPTION_PATH + "//p[contains(text(),\"http\")]"),
        }

    @property
    def large_logo_image(self) -> WebElement:
        return self._driver.find_element(*self.locators["large_logo_image"])

    @property
    def initiative_title(self) -> WebElement:
        return self._driver.find_element(*self.locators["initiative_title"])

    @property
    def initiative_description(self) -> WebElement:
        return self._driver.find_element(*self.locators["initiative_description"])

    @property
    def initiative_video_link_text(self) -> WebElement:
        return self._driver.find_element(*self.locators["initiative_video_link_text"])
