from typing import Self
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.add_center_step_two import AddCenterStepTwo
from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.components.base_component import BaseComponent
from src.ui.elements.input_with_info_tooltip import InputWithInfoTooltip


class AddCenterStepOne(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "center_popup_title": ("xpath", ".//div[@class='modal-title']"),
            "center_input_node": ("xpath", "./descendant::div[contains(@class,'ant-form-item-with-help')][1]"),
            "center_location_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][2]"),
            "add_location_button": ("xpath", ".//button[contains(@class,'add-location-btn')]"),
            "location_error_message": ("xpath", ".//div[(@id='basic_locations_help')]"
                                                "//div[@class='ant-form-item-explain-error']"),
            "location_popup": ("xpath", "//descendant::div[contains(@class,'modal-add-club')]"),

            "locations_elements": ("xpath", "//div[(@id='basic_locations')]/div[@class='checkbox-item']/label"),
            "checked_locations": ("xpath", ".//div[(@id='basic_locations')]"
                                           "//label[contains(@class,'ant-checkbox-wrapper-checked')]"),
            "next_step_button": ("xpath", ".//button[contains(@class,'next-btn')]")
        }

    def get_center_popup_title_text(self) -> str:
        return self.center_popup_title.text

    @property
    def center_name_element(self) -> InputWithInfoTooltip:
        return InputWithInfoTooltip(self.center_input_node)

    def get_center_location_title_text(self) -> str:
        return self.center_location_title.text

    def click_add_location_button(self) -> AddLocationPopUp:
        self.add_location_button.click_button()
        return AddLocationPopUp(self.location_popup)

    @property
    def locations_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["locations_elements"])

    def get_locations_list_names(self) -> list[str]:
        return [location.text for location in self.locations_list]

    @property
    def checked_locations_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["checked_locations"])

    def checked_locations_list_names(self) -> list[str]:
        return [location.text for location in self.checked_locations_list]

    def click_location_checkbox_by_name(self, name: str) -> Self:
        for location in self.locations_list:
            if name in location.text:
                location.click()
        return self

    def click_location_checkbox_by_index(self, index: int) -> Self:
        self.locations_list[index].click()
        return self

    def click_next_step_button(self) -> AddCenterStepTwo:
        self.next_step_button.click_button()
        return AddCenterStepTwo(self.node)
