from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_club_popup.add_club_step_two import AddClubStepTwo
from src.ui.components.base_component import BaseComponent
from src.ui.elements.dropdown import Dropdown
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors
from src.ui.elements.number_input import NumberInput

CLUB_POPUP_TITLE = (By.XPATH, ".//div[contains(@class,'add-club-header')]")
NEXT_STEP_BUTTON = (By.XPATH, ".//button[contains(@class,'add-club-content-next')]")
INPUT_NODE = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item add-club-row')][1]")
CATEGORIES_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][2]")
CATEGORIES_NODE_LIST = (By.XPATH, ".//label[contains(@class,'ant-checkbox-wrapper')]")
CATEGORIES_INPUT_LIST = (By.XPATH, ".//input[@class='ant-checkbox-input']")
CHECKED_CATEGORIES_LIST = (By.XPATH, ".//span[contains(@class,'ant-checkbox-checked')]"
                                     "/input[@class='ant-checkbox-input']")
CATEGORIES_ERROR = (By.XPATH, ".//div[contains(@id,'ategories_help')]/div")
AGE_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][3]")
MIN_AGE_INPUT_NODE = (By.XPATH, ".//span[contains(@class,'add-club-age')]"
                                "/descendant::div[contains(@class,'ant-form-item ')][1]")
MAX_AGE_INPUT_NODE = (By.XPATH, ".//span[contains(@class,'add-club-age')]"
                                "/descendant::div[contains(@class,'ant-form-item ')][2]")
CENTER_DROPDOWN = (By.XPATH, ".//div[contains(@class, 'add-club-select')]")


class AddClubStepOne(BaseComponent):
    def __init__(self, popup: 'AddClubPopUp', node: WebElement) -> None:
        super().__init__(node)
        self._popup = popup
        self._name_input_element = None
        self._popup_title = None
        self._next_button = None
        self._categories_title = None
        self._age_title = None
        self._min_age_input = None
        self._max_age_input = None
        self._center_title = None
        self._center_dropdown_element = None

    @property
    def popup_title(self) -> WebElement:
        if not self._popup_title:
            self._popup_title = self.node.find_element(*CLUB_POPUP_TITLE)
        return self._popup_title

    @property
    def name_input_element(self) -> InputWithLabelIconsErrors:
        if not self._name_input_element:
            self._name_input_element = InputWithLabelIconsErrors(self.node.find_element(*INPUT_NODE))
        return self._name_input_element

    @property
    def categories_title(self) -> WebElement:
        if not self._categories_title:
            self._categories_title = self.node.find_element(*CATEGORIES_TITLE)
        return self._categories_title

    @property
    def categories_node_list(self) -> list[WebElement]:
        return self.node.find_elements(*CATEGORIES_NODE_LIST)

    @property
    def categories_input_list(self) -> list[WebElement]:
        return self.node.find_elements(*CATEGORIES_INPUT_LIST)

    def click_on_category_by_name(self, value: str) -> Self:
        for category in self.categories_input_list:
            if category.get_attribute("value") == value:
                category.click()
        return self

    def get_category_texts_list(self) -> list[str]:
        return [category.get_attribute("value") for category in self.categories_input_list]

    @property
    def checked_categories_list(self) -> list[WebElement]:
        return self.node.find_elements(*CHECKED_CATEGORIES_LIST)

    def get_checked_category_texts_list(self) -> list[str]:
        return [category.get_attribute("value") for category in self.checked_categories_list]

    @property
    def categories_errors(self) -> list[WebElement]:
        return self.node.find_elements(*CATEGORIES_ERROR)

    def get_category_error_texts_list(self) -> list[str]:
        return [error.get_attribute("value") for error in self.categories_errors]

    @property
    def age_title(self) -> WebElement:
        if not self._age_title:
            self._age_title = self.node.find_element(*AGE_TITLE)
        return self._age_title

    @property
    def min_age_input(self) -> NumberInput:
        if not self._min_age_input:
            self._min_age_input = NumberInput(self.node.find_element(*MIN_AGE_INPUT_NODE))
        return self._min_age_input

    @property
    def max_age_input(self) -> NumberInput:
        if not self._max_age_input:
            self._max_age_input = NumberInput(self.node.find_element(*MAX_AGE_INPUT_NODE))
        return self._max_age_input

    @property
    def center_dropdown_element(self) -> Dropdown:
        if not self._center_dropdown_element:
            self._center_dropdown_element = Dropdown(self.node.find_element(*CENTER_DROPDOWN))
        return self._center_dropdown_element

    @property
    def next_button(self) -> WebElement:
        if not self._next_button:
            self._next_button = self.node.find_element(*NEXT_STEP_BUTTON)
        return self._next_button

    @property
    def popup(self) -> 'AddClubPopUp':
        return self._popup

    def click_next_step_button(self) -> AddClubStepTwo:
        self.next_button.click()
        return self.popup.step_two_container
