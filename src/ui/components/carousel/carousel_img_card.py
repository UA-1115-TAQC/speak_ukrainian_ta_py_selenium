from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent


class CarouselImgCard(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "background_image": ("xpath", ".//div[@class=\"carousel-item\"]"),
            "card_heading": ("xpath", ".//h2"),
            "card_text": ("xpath", ".//span[contains(@class,\"description\")]"),
            "card_button": ("xpath", ".//a/button"),
            "card_button_text": ("xpath", ".//a/button/span"),
            "card_link": ("xpath", ".//a"),
        }

    def get_card_link_text(self) -> str:
        return self.card_link.get_attribute("href")

    def click_card_button(self):
        self.card_button.click()
