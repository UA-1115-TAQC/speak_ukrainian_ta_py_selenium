from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_icon_element import InputWithIconElement

RESTORATION_TITLE = (By.XPATH, "./descendant::div[contains(@class, 'login-header')]")
SUBMIT_BUTTON = (By.XPATH, "./descendant::button[@type='submit']")
CLOSE_BUTTON = (By.XPATH, "./descendant::button[@type='button']")
EMAIL_INPUT = (By.XPATH, "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][1]")


class RestorationPasswordComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._email_input_element = None
        self._restoration_title = None
        self._submit_button = None
        self._close_button = None

    @property
    def email_input(self) -> InputWithIconElement:
        if not self._email_input_element:
            self._email_input_element = InputWithIconElement(self.node.find_element(*EMAIL_INPUT))
        return self._email_input_element

    @property
    def restoration_title(self) -> WebElement:
        if not self._restoration_title:
            self._restoration_title = self.node.find_element(*RESTORATION_TITLE)
        return self._restoration_title

    @property
    def submit_button(self) -> WebElement:
        if not self._submit_button:
            self._submit_button = self.node.find_element(*SUBMIT_BUTTON)
        return self._submit_button

    @property
    def close_button(self) -> WebElement:
        if not self._close_button:
            self._close_button = self.node.find_element(*CLOSE_BUTTON)
        return self.close_button

    def get_menu_header_text(self) -> str:
        return self.restoration_title.text

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def click_close_button(self) -> None:
        self.close_button.click()
