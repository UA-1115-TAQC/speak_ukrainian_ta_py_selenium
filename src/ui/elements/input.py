from typing import Self

from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.base_element import BaseElement
from selenium.webdriver import Keys, ActionChains


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "input": ("xpath", ".//input")
        }

    def get_input_value(self) -> str:
        return self.input.visibility_of_element_located().get_attribute("value")

    def set_input_value(self, value: str) -> None:
        self.input.visibility_of_element_located().send_keys(value)

    def clear_input(self) -> Self:
        self.input.visibility_of_element_located().click()
        self.get_actions().key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        self.get_actions().key_down(Keys.COMMAND) \
            .send_keys('a') \
            .key_up(Keys.COMMAND) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        return self
