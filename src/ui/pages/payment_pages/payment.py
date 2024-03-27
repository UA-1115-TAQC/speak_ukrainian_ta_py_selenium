from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter

INITIATIVE_HEADER_PATH = "//div[contains(@class,\"header\")]"
INITIATIVE_DESCRIPTION_PATH = "//div[contains(@class,\"description\")]"

LARGE_LOGO_IMAGE = (By.XPATH, INITIATIVE_HEADER_PATH + "//div[contains(@class,\"large\")]")
INITIATIVE_TITLE = (By.XPATH, INITIATIVE_HEADER_PATH + "//div[contains(@class,\"title\")]")
INITIATIVE_DESCRIPTION = (By.XPATH, INITIATIVE_DESCRIPTION_PATH + "//p[not (contains(text(),\"http\"))]")
INITIATIVE_VIDEO_LINK_TEXT = (By.XPATH, INITIATIVE_DESCRIPTION_PATH + "//p[contains(text(),\"http\")]")


class Payment(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self._large_logo_image = None
        self._initiative_title = None
        self._initiative_description = None
        self._initiative_video_link_text = None

    @property
    def large_logo_image(self) -> WebElement:
        if not self._large_logo_image:
            self._large_logo_image = self._driver.find_element(*LARGE_LOGO_IMAGE)
        return self._large_logo_image

    @property
    def initiative_title(self) -> WebElement:
        if not self._initiative_title:
            self._initiative_title = self._driver.find_element(*INITIATIVE_TITLE)
        return self._initiative_title

    @property
    def initiative_description(self) -> WebElement:
        if not self._initiative_description:
            self._initiative_description = self._driver.find_element(*INITIATIVE_DESCRIPTION)
        return self._initiative_description

    @property
    def initiative_video_link_text(self) -> WebElement:
        if not self._initiative_video_link_text:
            self._initiative_video_link_text = self._driver.find_element(*INITIATIVE_VIDEO_LINK_TEXT)
        return self._initiative_video_link_text
