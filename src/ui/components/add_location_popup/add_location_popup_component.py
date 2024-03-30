from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.dropdown_with_icon_errors import DropdownWithIconErrors
from src.ui.elements.input_with_info_tooltip import InputWithInfoTooltip
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors


class AddLocationPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "location_popup_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][1]"),
            "location_name_input": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][1]"),
            "location_city": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][2]"),
            "location_district": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][3]"),
            "location_metro": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][4]"),
            "location_address": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][5]"),
            "location_coordinates": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][6]"),
            "location_telephone": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][7]"),
            "submit_button": ("xpath", ".//button[contains(@class,'add-club-content-next')]")
        }

    def get_location_popup_title_text(self) -> str:
        return self.location_popup_title.text

    @property
    def name_input_element(self) -> InputWithInfoTooltip:
        return InputWithInfoTooltip(self.location_name_input)

    @property
    def city_dropdown_element(self) -> DropdownWithIconErrors:
        return DropdownWithIconErrors(self.location_city)

    @property
    def district_dropdown_element(self) -> DropdownWithIconErrors:
        return DropdownWithIconErrors(self.location_district)

    @property
    def metro_dropdown_element(self) -> DropdownWithIconErrors:
        return DropdownWithIconErrors(self.location_metro)

    @property
    def address_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.location_address)

    @property
    def coordinates_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.location_coordinates)

    @property
    def telephone_input_element(self) -> InputWithInfoTooltip:
        return InputWithInfoTooltip(self.location_telephone)

    def click_submit_button(self) -> None:
        self.submit_button.click_button()
