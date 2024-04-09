from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.dropdown import Dropdown


class DropdownWithIconErrors(Dropdown):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            **self.locators,
            "validation_circle_icon": ("xpath", ".//div[@class='ant-form-item-control-input']"
                                                "/descendant::span[contains(@class,'anticon-close-circle') "
                                                "or contains(@class,'anticon-check-circle')]"),
            "error_list": ("xpath", ".//div[contains(@class,'ant-col')]//div[@class='ant-form-item-explain-error']")
        }

    @property
    def error_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["error_list"])

    def get_list_of_error_texts(self) -> list[str]:
        return [error.text for error in self.error_list]


class AddLocationDropdown(DropdownWithIconErrors):
    def __init__(self, node, list_id):
        super().__init__(node)
        self._list_id = list_id

    def visible_items_list(self) -> list[WebElement]:
        xpath = ("//div[@id='"
                 +self._list_id+
                 "']/following-sibling::div/descendant::div[contains(@class,'ant-select-item ant-select-item-option')]")
        return self.node.find_elements(*("xpath", xpath))
