from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.input import Input


class InputWithLabelIconsErrors(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            **self.locators,
            "input_label": ("xpath", "./preceding-sibling::span[contains(@class,'ant-typography')][1] | "
                                     ".//div[contains(@class, 'user-edit-input')]//label"),
            "validation_circle_icon": ("xpath", ".//div[@class='ant-form-item-control-input']"
                                                "//span[contains(@class,'anticon-close-circle') "
                                                "or contains(@class,'anticon-check-circle')]"),
            "static_icon": ("xpath", ".//div[@class='ant-form-item-control-input']"
                                     "//span[@class='ant-input-suffix']"
                                     "/div[@class='icon']"),
            "error_messages_list": ("xpath", ".//div[contains(@class,'ant-col')]"
                                             "//div[@class='ant-form-item-explain-error']")
        }

    @property
    def error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["error_messages_list"])

    def get_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.error_messages_list]
