from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

LOCATOR_INPUT = (By.XPATH, ".//input")


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._input = None
        self._input_value = None

    @property
    def input(self) -> WebElement:
        if not self._input:
            self._input = self.node.find_element(*LOCATOR_INPUT)
        return self._input

    @property
    def input_value(self) -> str:
        return self.input.get_attribute("value")

    @input_value.setter
    def input_value(self, value: str) -> None:
        self.input.send_keys(value)

    def clear_input(self) -> None:
        input = self.input
        current_platform = self.node.parent.capabilities['platformName']
        if current_platform.lower() == 'mac':
            input.send_keys(Keys.COMMAND + 'a')
            input.send_keys(Keys.DELETE)
        else:
            input.send_keys(Keys.CONTROL + 'a')
            input.send_keys(Keys.BACK_SPACE)
