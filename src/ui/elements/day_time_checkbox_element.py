from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.elements.base_element import BaseElement

CHECKBOX = (By.XPATH, ".//input[@class='ant-checkbox-input']")
CHECKBOX_TITLE = (By.XPATH, "./descendant::label[contains(@class,'ant-checkbox-wrapper')]/span[2]/div")
TIME_FROM_INPUT = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item')]"
                             "/descendant::input[@placeholder='HH:mm'][1]")
TIME_TO_INPUT = (By.XPATH, "./descendant::div[contains(@class,'ant-form-item')]"
                           "/descendant::input[@placeholder='HH:mm'][2]")
TIME_PICKER_CONTAINER = (By.XPATH, "//div[@class='ant-picker-panel-container']")
TIME_PICKER_BUTTON = (By.XPATH, "//div[@class='ant-picker-panel-container']//button")
TIME_FROM_PICKER_LIST = (By.XPATH, "//div[contains(@class,'ant-picker-dropdown')]"
                                   "/descendant::ul[contains(@class,'ant-picker-time-panel-column')][1]"
                                   "//div[@class='ant-picker-time-panel-cell-inner']")
TIME_TO_PICKER_LIST = (By.XPATH, "//div[contains(@class,'ant-picker-dropdown')]"
                                 "/descendant::ul[contains(@class,'ant-picker-time-panel-column')][2]"
                                 "//div[@class='ant-picker-time-panel-cell-inner']")
CLOCK_ICON = (By.XPATH, "//div[contains(@class,'ant-picker-dropdown')]"
                        "/descendant::span[@class='ant-picker-suffix']"
                        "/span[@aria-label='clock-circle']")


class DayTimeCheckboxElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._checkbox_title = None
        self._time_from_input = None
        self._time_to_input = None
        self._clock_icon = None

    @property
    def checkbox_title(self) -> WebElement:
        if not self._checkbox_title:
            self._checkbox_title = self.node.find_element(*CHECKBOX_TITLE)
        return self._checkbox_title

    @property
    def checkbox(self) -> WebElement:
        return self.node.find_element(*CHECKBOX)

    @property
    def time_from_input(self) -> WebElement:
        if not self._time_from_input:
            self._time_from_input = self.node.find_element(*TIME_FROM_INPUT)
        return self._time_from_input

    def set_time_from_input(self, value: str) -> Self:
        self.time_from_input.send_keys(value)
        return self

    @property
    def time_to_input(self) -> WebElement:
        if not self._time_to_input:
            self._time_to_input = self.node.find_element(*TIME_TO_INPUT)
        return self._time_to_input

    def set_time_to_input(self, value: str) -> Self:
        self.time_to_input.send_keys(value)
        return self

    @property
    def time_picker_container(self) -> WebElement:
        return self.node.find_element(*TIME_PICKER_CONTAINER)

    @property
    def time_picker_button(self) -> WebElement:
        return self.node.find_element(*TIME_PICKER_BUTTON)

    def click_time_picker_button(self) -> Self:
        wait = WebDriverWait(self.node.parent, 5)
        wait.until(lambda e: self.time_picker_button.is_displayed())
        self.time_picker_button.click()
        return self

    @property
    def time_from_picker_list(self) -> list[WebElement]:
        return self.node.find_elements(*TIME_FROM_PICKER_LIST)

    @property
    def time_to_picker_list(self) -> list[WebElement]:
        return self.node.find_elements(*TIME_TO_PICKER_LIST)

    @property
    def clock_icon(self) -> WebElement:
        if not self._clock_icon:
            self._clock_icon = self.node.find_element(*CLOCK_ICON)
        return self._clock_icon
