from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class CarouselImgCard(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver)
        self._driver = driver
        self._node = node
        self.locators = {
            "background_image": ("xpath", ".//div[@class=\"carousel-item\"]"),
            "card_heading": ("xpath", ".//h2"),
            "card_text": ("xpath", ".//span[contains(@class,\"description\")]"),
            "card_button": ("xpath", ".//a/button"),
            "card_button_text": ("xpath", ".//a/button/span"),
            "card_link": ("xpath", ".//a"),
        }

    @property
    def background_image(self) -> WebElement:
        return self._node.find_element(*self.locators["background_image"])

    @property
    def card_heading(self) -> WebElement:
        return self._node.find_element(*self.locators["card_heading"])

    @property
    def card_text(self) -> WebElement:
        return self._node.find_element(*self.locators["card_text"])

    @property
    def card_button(self) -> WebElement:
        return self._node.find_element(*self.locators["card_button"])

    @property
    def card_button_text(self) -> WebElement:
        return self._node.find_element(*self.locators["card_button_text"])

    @property
    def card_link(self) -> WebElement:
        return self._node.find_element(*self.locators[".//a"])

    def get_card_link_text(self) -> str:
        return self.card_link.get_attribute("href")

    def click_card_button(self):
        self.card_button.click()
