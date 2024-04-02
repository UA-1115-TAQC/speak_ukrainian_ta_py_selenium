from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_icon_element import InputWithIconElement


class RestorationPasswordComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "restoration_title": ("xpath", "./descendant::div[contains(@class, 'login-header')]"),
            "submit_button": ("xpath", "./descendant::button[@type='submit']"),
            "close_button": ("xpath", "./descendant::button[@type='button']"),
            "email_input": ("xpath", "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][1]")
        }

    @property
    def email_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.email_input)

    def enter_email(self, email: str) -> None:
        self.email_input_element.set_input_value(email)

    def restoration_pop_up_title(self) -> str:
        return self.restoration_title.text

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def click_close_button(self) -> None:
        self.close_button.click()
