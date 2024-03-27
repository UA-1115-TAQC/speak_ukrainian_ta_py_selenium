from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.input import Input


class NumberInput(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            **self.locators,
            "increase_button": ("xpath", "./descendant::span[@aria-label='increase value']"),
            "decrease_button": ("xpath", "./descendant::span[@aria-label='decrease value']"),
            "input_error": ("xpath", ".//div[contains(@id,'_help')]/div")
        }

    @property
    def errors_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["input_error"])

    def get_error_texts_list(self) -> list[str]:
        return [error.text for error in self.errors_list]
