from typing import Self

from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent


class FooterComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "logo": ("xpath", "//div[contains(@class,'footer-logo')]"),
            "motto_under_logo": ("xpath", "//div[contains(@class,'text')]"),
            "social_links": ("xpath", "//div[contains(@class,'links')]/a[contains(@href, 'https')]"),
            "copyright_text": ("xpath", "//div[contains(@class,'qubstudio')]"),
            "sponsors_title": ("xpath", "//div[@class='footer-partners']/div[@class='article']"),
            "sponsors_links": ("xpath", "//div[contains(@class,'sponsors')]/a[contains(@href, 'https')]"),
            "donate_title": ("xpath", "//div[@class='footer-donate']/div[@class='article']"),
            "donate_explanation": ("xpath", "//div[@class='desc']"),
            "donate_button": ("xpath", "//button[contains(@class,'donate-button')]"),
            "social_block": ("xpath", "//div[@class='footer-social']"),
            "sponsors_block": ("xpath", "//div[@class='footer-partners']"),
            "donate_block": ("xpath", "//div[@class='footer-donate']")
        }

    def click_on_logo(self) -> Self:
        return self.logo.click

    @property
    def list_of_social_links(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["social_links"])

    def get_social_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_social_links]

    @property
    def list_of_sponsors_links(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["sponsors_links"])

    def get_sponsors_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_sponsors_links]

    def click_on_donate_button(self) -> Self:
        return self.donate_button.click
