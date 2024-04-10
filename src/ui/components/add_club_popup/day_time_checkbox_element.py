from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement


class DayTimeCheckboxElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "checkbox": ("xpath", ".//input[@class='ant-checkbox-input']"),
            "checkbox_title": ("xpath", ".//label[contains(@class,'ant-checkbox-wrapper')]"),
            "time_from_input": ("xpath", ".//div[contains(@class,'ant-form-item')]"
                                         "/descendant::input[@placeholder='HH:mm'][1]"),
            "time_to_input": ("xpath", ".//div[contains(@class,'ant-form-item')]"
                                       "/descendant::input[@placeholder='HH:mm'][2]"),
            "time_picker_container": ("xpath", "//div[@class='ant-picker-panel-container']"),
            "time_picker_button": ("xpath", "//div[@class='ant-picker-panel-container']//button"),
            "hours_picker": ("xpath", "//div[contains(@class,'ant-picker-dropdown')]"
                                      "/descendant::ul[contains(@class,'ant-picker-time-panel-column')][1]"
                                      "//div[@class='ant-picker-time-panel-cell-inner']"),
            "minutes_picker": ("xpath", "//div[contains(@class,'ant-picker-dropdown')]"
                                        "/descendant::ul[contains(@class,'ant-picker-time-panel-column')][2]"
                                        "//div[@class='ant-picker-time-panel-cell-inner']"),
            "clock_icon": ("xpath", "//div[contains(@class,'ant-picker-dropdown')]"
                                    "/descendant::span[@class='ant-picker-suffix']"
                                    "/span[@aria-label='clock-circle']")
        }

    def click_on_checkbox(self) -> Self:
        self.checkbox_title.click_button()
        return self

    def get_checkbox_title_text(self) -> str:
        return self.checkbox_title.text

    def set_time_from_input(self, value: str) -> Self:
        self.time_from_input.visibility_of_element_located().send_keys(value)
        self.click_time_picker_button()
        return self

    def set_time_to_input(self, value: str) -> Self:
        self.time_to_input.visibility_of_element_located().send_keys(value)
        self.click_time_picker_button()
        return self

    def click_time_picker_button(self) -> Self:
        self.time_picker_button.click_button()
        return self

    @property
    def hours_picker_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["hours_picker"])

    def hours_text_picker_list(self) -> list[str]:
        return [item.text for item in self.hours_picker_list]

    @property
    def minutes_picker_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["minutes_picker"])

    def minutes_text_picker_list(self) -> list[str]:
        return [item.text for item in self.hours_picker_list]
