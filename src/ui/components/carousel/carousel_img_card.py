from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

BACKGROUND_IMAGE = (By.XPATH, ".//div[@class=\"carousel-item\"]")
CARD_HEADING = (By.XPATH, ".//h2")
CARD_TEXT = (By.XPATH, ".//span[contains(@class,\"description\")]")
CARD_BUTTON = (By.XPATH, ".//a/button")
CARD_BUTTON_TEXT = (By.XPATH, ".//a/button/span")
CARD_LINK = (By.XPATH, ".//a")


class CarouselImgCard(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver)
        self._driver = driver
        self._node = node
        self._background_image = None
        self._card_heading = None
        self._card_text = None
        self._card_button = None
        self._card_button_text = None
        self._card_link = None

    @property
    def background_image(self) -> WebElement:
        if not self._background_image:
            self._background_image = self._node.find_element(*BACKGROUND_IMAGE)
        return self._background_image

    @property
    def card_heading(self) -> WebElement:
        if not self._card_heading:
            self._card_heading = self._node.find_element(*CARD_HEADING)
        return self._card_heading

    @property
    def card_text(self) -> WebElement:
        if not self._card_text:
            self._card_text = self._node.find_element(*CARD_TEXT)
        return self._card_text

    @property
    def card_button(self) -> WebElement:
        if not self._card_button:
            self._card_button = self._node.find_element(*CARD_BUTTON)
        return self._card_button

    @property
    def card_button_text(self) -> WebElement:
        if not self._card_button_text:
            self._card_button_text = self._node.find_element(*CARD_BUTTON_TEXT)
        return self._card_button_text

    @property
    def card_link(self) -> WebElement:
        if not self._card_link:
            self._card_link = self._node.find_element(*CARD_LINK)
        return self._card_link

    def get_card_link_text(self) -> str:
        return self.card_link.get_attribute("href")

    def click_card_button(self):
        self.card_button.click()
