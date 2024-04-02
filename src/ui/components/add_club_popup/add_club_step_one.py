from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_club_popup.add_club_step_two import AddClubStepTwo
from src.ui.components.base_component import BaseComponent
from src.ui.elements.dropdown import Dropdown
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors
from src.ui.elements.number_input import NumberInput


class AddClubStepOne(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "popup_title": ("xpath", ".//div[contains(@class,'add-club-header')]"),
            "next_step_button": ("xpath", ".//button[contains(@class,'add-club-content-next')]"),
            "name_input": ("xpath", "./descendant::div[contains(@class,'ant-form-item add-club-row')][1]"),
            "categories_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][2]"),
            "categories_node_list": ("xpath", ".//label[contains(@class,'ant-checkbox-wrapper')]"),
            "categories_input_list": ("xpath", ".//input[@class='ant-checkbox-input']"),
            "checked_categories_list": ("xpath", ".//span[contains(@class,'ant-checkbox-checked')]"
                                                 "/input[@class='ant-checkbox-input']"),
            "categories_error": ("xpath", ".//div[contains(@id,'ategories_help')]/div"),
            "age_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][3]"),
            "min_age_input": ("xpath", ".//span[contains(@class,'add-club-age')]"
                                       "/descendant::div[contains(@class,'ant-form-item ')][1]"),
            "max_age_input": ("xpath", ".//span[contains(@class,'add-club-age')]"
                                       "/descendant::div[contains(@class,'ant-form-item ')][2]"),
            "center_dropdown": ("xpath", ".//div[contains(@class, 'add-club-select')]"),
            "step_container": ("xpath", "//main[contains(@class,'add-club-container')]")
        }

    def get_popup_title_text(self) -> str:
        return self.popup_title.text

    @property
    def name_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.name_input)

    def get_categories_title_text(self) -> str:
        return self.categories_title.text

    @property
    def categories_node_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["categories_node_list"])

    @property
    def categories_input_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["categories_input_list"])

    def click_on_category_by_name(self, value: str) -> Self:
        for category in self.categories_input_list:
            if category.get_attribute("value") == value:
                category.click()
        return self

    def get_category_texts_list(self) -> list[str]:
        return [category.get_attribute("value") for category in self.categories_input_list]

    @property
    def checked_categories_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["checked_categories_list"])

    def get_checked_category_texts_list(self) -> list[str]:
        return [category.get_attribute("value") for category in self.checked_categories_list]

    def get_category_error_texts_list(self) -> list[str]:
        return [error.get_attribute("value") for error in self.categories_errors]

    def get_age_title_text(self) -> str:
        return self.age_title.text

    @property
    def min_age_input_element(self) -> NumberInput:
        return NumberInput(self.min_age_input)

    @property
    def max_age_input_element(self) -> NumberInput:
        return NumberInput(self.max_age_input)

    @property
    def center_dropdown_element(self) -> Dropdown:
        return Dropdown(self.center_dropdown)

    def click_next_step_button(self) -> AddClubStepTwo:
        self.next_step_button.click_button()
        return AddClubStepTwo(self.node)
