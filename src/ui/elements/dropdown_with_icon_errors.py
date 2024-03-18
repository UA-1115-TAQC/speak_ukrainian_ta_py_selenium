from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.dropdown import Dropdown

VALIDATION_CIRCLE_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                                    "/descendant::span[contains(@class,'anticon-close-circle') "
                                    "or contains(@class,'anticon-check-circle')]")
ERROR_LIST = (By.XPATH, ".//div[contains(@class,'ant-col')]/descendant::div[@class='ant-form-item-explain-error']")


class DropdownWithIconErrors(Dropdown):
    def __init__(self, node: WebElement):
        super().__init__(node)

    @property
    def validation_icon(self) -> WebElement:
        return self.node.find_element(*VALIDATION_CIRCLE_ICON)

    @property
    def error_list(self) -> list[WebElement]:
        return self.node.find_elements(*ERROR_LIST)

    def get_list_of_error_texts(self) -> list[str]:
        return [error.text for error in self.error_list]
