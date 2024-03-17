from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.input import Input

INPUT_LABEL = (By.XPATH, "./preceding-sibling::span[contains(@class,'ant-typography')][1]")
VALIDATION_CIRCLE_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                                    "//span[contains(@class,'anticon-close-circle') "
                                    "or contains(@class,'anticon-check-circle')]")
STATIC_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                         "//span[@class='ant-input-suffix']"
                         "/div[@class='icon']")
ERROR_MESSAGES_LIST = (By.XPATH, ".//div[contains(@class,'ant-col')]//div[@class='ant-form-item-explain-error']")


class InputWithLabelIconsErrors(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._label = None
        self._static_icon = None

    @property
    def label(self) -> WebElement:
        if not self._label:
            self._label = self.node.find_element(*INPUT_LABEL)
        return self._label

    @property
    def validation_circle_icon(self) -> WebElement:
        return self.node.find_element(*VALIDATION_CIRCLE_ICON)

    @property
    def static_icon(self) -> WebElement:
        if not self._static_icon:
            self._static_icon = self.node.find_element(*STATIC_ICON)
        return self._static_icon

    @property
    def error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*ERROR_MESSAGES_LIST)

    def get_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.error_messages_list]
