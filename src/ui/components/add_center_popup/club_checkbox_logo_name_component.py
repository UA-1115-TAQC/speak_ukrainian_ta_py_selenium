from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent


class ClubCheckboxLogoNameComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators ={
            "club_checkbox": ("xpath",".//input[@type='checkbox']"),
            "club_logo": ("xpath", ".//div[@class='icon-box']//img"),
            "club_name": ("xpath", ".//span[@class='club-name']")
        }

    def get_club_name_text(self) -> str:
        return self.club_name.text

    def click_on_checkbox(self) -> Self:
        self.club_checkbox.click()
        return self
