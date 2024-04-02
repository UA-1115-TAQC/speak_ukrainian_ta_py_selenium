from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.club_checkbox_logo_name_component import ClubCheckboxLogoNameComponent
from src.ui.components.base_component import BaseComponent


class AddCenterStepFour(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "center_popup_title": ("xpath", ".//div[@class='modal-title']"),
            "select_club_title": ("xpath", ".//form[contains(@class,'clubsOfCenter')]/span"),
            "club_webelements": ("xpath", ".//div[@class='checkbox-item']"),
            "complete_button": ("xpath", ".//button[contains(@class,'finish-btn')]"),
            "previous_step_button": ("xpath", ".//button[contains(@class,'prev-btn')]")
        }

    def get_center_popup_title_text(self) -> str:
        return self.center_popup_title.text

    def get_select_club_title_text(self) -> str:
        return self.select_club_title.text

    @property
    def club_webelements_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["club_webelements"])

    @property
    def club_checkbox_logo_names_list(self) -> list[ClubCheckboxLogoNameComponent]:
        return [ClubCheckboxLogoNameComponent(club_webelement) for club_webelement in self.club_webelements_list]

    def click_on_club_checkbox_by_name(self, name: str) -> Self:
        for club in self.club_checkbox_logo_names_list:
            if name in club.get_club_name_text():
                club.click_on_checkbox()
        return self

    def click_on_club_checkbox_by_index(self, index: int) -> Self:
        self.club_checkbox_logo_names_list[index].click_on_checkbox()
        return self

    def click_complete_button(self) -> None:
        self.complete_button.click_button()

    def click_previous_step_button(self) -> 'AddCenterStepThree':
        self.previous_step_button.click_button()
        from src.ui.components.add_center_popup.add_center_step_three import AddCenterStepThree
        return AddCenterStepThree(self.node)
