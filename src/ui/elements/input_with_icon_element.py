from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.input import Input

VALIDATION_CIRCLE_ICON = (By.XPATH, "./descendant::span[contains(@class,'anticon-close-circle') "
                                    "or contains(@class,'anticon-check-circle')]")
STATIC_ICON = (By.XPATH, "./descendant::span[@class='ant-input-suffix']/span[@aria-label='mail']")
PASSWORD_VISIBILITY_ICON = (By.XPATH, "./descendant::span[@class='ant-input-suffix']"
                                      "/span[contains(@aria-label, 'eye-invisible') or contains(@aria-label, 'eye')]")
ERROR_MESSAGES = (By.XPATH, ".//div[contains(@class,'ant-col')]/descendant::div[@class='ant-form-item-explain-error']")
WHOLE_INPUT_ELEMENT = (By.XPATH, ".//span[contains(@class, 'registration-box')]")


class InputWithIconElement(Input):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._validation_circle_icon = None
        self._static_icon = None
        self._password_visibility_icon = None
        self._email_title = None
        self._password_title = None
        self._error_messages = None
        self._whole_input_element = None

    @property
    def validation_circle_icon(self) -> WebElement:
        if not self._validation_circle_icon:
            self._validation_circle_icon = self.node.find_element(*VALIDATION_CIRCLE_ICON)
        return self._validation_circle_icon

    @property
    def static_icon(self) -> WebElement:
        if not self._static_icon:
            self._static_icon = self.node.find_element(*STATIC_ICON)
        return self._static_icon

    @property
    def password_visibility_icon(self) -> WebElement:
        if not self._password_visibility_icon:
            self._password_visibility_icon = self.node.find_element(*PASSWORD_VISIBILITY_ICON)
        return self._password_visibility_icon

    @property
    def error_messages(self) -> list[WebElement]:
        if not self._error_messages:
            self._error_messages = self.node.find_elements(*ERROR_MESSAGES)
        return self._error_messages

    @property
    def whole_input_element(self) -> WebElement:
        if not self._whole_input_element:
            self._whole_input_element = self.node.find_element(*WHOLE_INPUT_ELEMENT)
        return self._whole_input_element

    def click_password_visibility_icon(self) -> None:
        self.password_visibility_icon.click()

    def get_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.error_messages]
