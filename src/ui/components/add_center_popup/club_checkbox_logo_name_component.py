from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent


class ClubCheckboxLogoNameComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "club_checkbox": ("xpath", ".//input"),
            "club_logo": ("xpath", ".//img"),
            "club_name": ("xpath", ".//span[@class='club-name']")
        }

    def scroll_to_club(self) -> Self:
        self.get_actions().scroll_to_element(self.node).perform()
        return self

    def get_club_name_text(self) -> str:
        return self.club_name.text

    def get_logo_image_path(self) -> str:
        return self.club_logo.getAttribute("src")

    def click_on_checkbox(self) -> Self:
        self.scroll_to_club().club_checkbox.click()
        return self
