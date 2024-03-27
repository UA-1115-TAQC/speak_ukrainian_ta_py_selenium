from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from typing import Self


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
            "donate_button": ("xpath", "//button[contains(@class,'donate-button')]")

        }

    def click_on_logo(self) -> None:
        return self.logo.click()

    def get_motto_under_logo_text(self) -> str:
        return self.motto_under_logo.text()

    @property
    def list_of_social_links(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["social_links"])

    def get_social_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_social_links]

    def get_copyright_text(self) -> str:
        return self.copyright_text.text

    def get_sponsors_title_text(self) -> str:
        return self.sponsors_title.text

    def get_sponsors_title_attribute(self, name: str) -> str:
        return self.sponsors_title.get_attribute(name)

    @property
    def list_of_sponsors_links(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["sponsors_links"])

    def get_sponsors_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_sponsors_links]

    def get_donate_title_text(self) -> str:
        return self.donate_title.text()

    def get_donate_explanation_text(self) -> str:
        return self.donate_explanation.text()

    def click_on_donate_button(self):
        return self.donate_button.click()
