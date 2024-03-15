from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

LOCATOR_INPUT = (By.Xpath, ".//input")


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._input = None
        self._label = None
        self._error_msg = None

    def get_input(self):
        if not self._input:
            self._input = self.node.find_element(*LOCATOR_INPUT)
        return self._input
    
    def clear(self):
        input = self.get_input()
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.DELETE)
