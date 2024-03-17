from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.input import Input

INCREASE_BUTTON = (By.XPATH, "./descendant::span[@aria-label='Increase Value']")
DECREASE_BUTTON = (By.XPATH, "./descendant::span[@aria-label='Decrease Value']")
INPUT_ERROR = (By.XPATH, ".//div[contains(@id,'_help')]/div")


class NumberInput(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._increase_button = None
        self._decrease_button = None

    @property
    def increase_button(self) -> WebElement:
        if not self._increase_button:
            self._increase_button = self.node.find_element(*INCREASE_BUTTON)
        return self._increase_button

    @property
    def decrease_button(self) -> WebElement:
        if not self._decrease_button:
            self._decrease_button = self.node.find_element(*DECREASE_BUTTON)
        return self._decrease_button

    @property
    def errors_list(self) -> list[WebElement]:
        return self.node.find_elements(*INPUT_ERROR)

    def get_error_texts_list(self) -> list[str]:
        return [error.text for error in self.errors_list]
