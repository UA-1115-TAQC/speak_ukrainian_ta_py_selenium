from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.dropdown_with_icon_errors import DropdownWithIconErrors
from src.ui.elements.input_with_info_tooltip import InputWithInfoTooltip
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors

LOCATION_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][1]")
LOCATION_NAME_INPUT = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][1]")
LOCATION_CITY = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][2]")
LOCATION_DISTRICT = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][3]")
LOCATION_METRO = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][4]")
LOCATION_ADDRESS = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][5]")
LOCATION_COORDINATES = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][6]")
LOCATION_TELEPHONE = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][7]")
SUBMIT_BUTTON = (By.XPATH, ".//button[@type='submit']")


class AddLocationPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._location_popup_title = None
        self._name_input = None
        self._city_dropdown = None
        self._district_dropdown = None
        self._metro_dropdown = None
        self._address_input = None
        self._coordinates_input = None
        self._telephone_input = None
        self._submit_button = None

    @property
    def location_popup_title(self) -> WebElement:
        if not self._location_popup_title:
            self._location_popup_title = self.node.find_element(*LOCATION_TITLE)
        return self._location_popup_title

    @property
    def name_input(self) -> InputWithInfoTooltip:
        if not self._name_input:
            self._name_input = InputWithInfoTooltip(self.node.find_element(*LOCATION_NAME_INPUT))
        return self._name_input

    @property
    def city_dropdown(self) -> DropdownWithIconErrors:
        if not self._city_dropdown:
            self._city_dropdown = DropdownWithIconErrors(self.node.find_element(*LOCATION_CITY))
        return self._city_dropdown

    @property
    def district_dropdown(self) -> DropdownWithIconErrors:
        if not self._district_dropdown:
            self._district_dropdown = DropdownWithIconErrors(self.node.find_element(*LOCATION_DISTRICT))
        return self._district_dropdown

    @property
    def metro_dropdown(self) -> DropdownWithIconErrors:
        if not self._metro_dropdown:
            self._metro_dropdown = DropdownWithIconErrors(self.node.find_element(*LOCATION_METRO))
        return self._metro_dropdown

    @property
    def address_input(self) -> InputWithLabelIconsErrors:
        if not self._address_input:
            self._address_input = InputWithLabelIconsErrors(self.node.find_element(*LOCATION_ADDRESS))
        return self._address_input

    @property
    def coordinates_input(self) -> InputWithLabelIconsErrors:
        if not self._coordinates_input:
            self._coordinates_input = InputWithLabelIconsErrors(self.node.find_element(*LOCATION_COORDINATES))
        return self._coordinates_input

    @property
    def telephone_input(self) -> InputWithLabelIconsErrors:
        if not self._telephone_input:
            self._telephone_input = InputWithLabelIconsErrors(self.node.find_element(*LOCATION_TELEPHONE))
        return self._telephone_input

    @property
    def submit_button(self) -> WebElement:
        if not self._submit_button:
            self._submit_button = self.node.find_element(*SUBMIT_BUTTON)
        return self._submit_button

    def click_submit_button(self) -> None:
        self.submit_button.click()
