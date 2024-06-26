from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement


class Dropdown(BaseElement):
    def __init__(self, node: WebElement, dropdown_list_id: str):
        super().__init__(node)
        self._dropdown_list_id = dropdown_list_id
        self.locators = {
            "dropdown": ("xpath", ".//div[contains(@class,'ant-select-selector')]"),
            "dropdown_label": ("xpath", "./ancestor::div[contains(@class,'ant-form-item')]"
                                        "/preceding-sibling::span[contains(@class,'ant-typography')][1]"),
            "arrow_icon": ("xpath", ".//span[contains(@class,'ant-select-arrow')]/span[@aria-label='down']"),
            "placeholder": ("xpath", ".//span[@class='ant-select-selection-placeholder']"),
            "selected_item": ("xpath", ".//span[@class='ant-select-selection-item']"),
            "dropdown_container": ("xpath", "//div[@class='rc-virtual-list-holder']")
        }

    def click_dropdown(self) -> Self:
        self.dropdown.click_button()
        return self

    def get_dropdown_label_text(self) -> str:
        return self.dropdown_label.text

    @property
    def visible_items_list(self) -> list[WebElement]:
        xpath = ("//div[@id='"
                 + self._dropdown_list_id
                 + "']/following-sibling::div//div[contains(@class,'ant-select-item ant-select-item-option')]")
        return self.node.find_elements(*("xpath", xpath))

    def scroll_to_top(self):
        while True:
            current_first_item = self.visible_items_list[0]
            self.get_actions().move_to_element(current_first_item).perform()
            if current_first_item == self.visible_items_list[0]:
                return

    def select_item(self, item_name) -> Self:
        self.scroll_to_top()
        while True:
            for item in self.visible_items_list:
                if item.get_attribute("title").strip() == item_name:
                    self.get_actions().move_to_element(item).click().perform()
                    return self
            current_last_element = self.visible_items_list[-1]
            self.get_actions().move_to_element(current_last_element).perform()
            if current_last_element == self.visible_items_list[-1]:
                break
        return self

    def get_dropdown_placeholder_text(self) -> str:
        return self.placeholder.text

    def get_dropdown_selected_item_text(self) -> str:
        return self.selected_item.text


class DropdownWithIconError(Dropdown):
    def __init__(self, node: WebElement, dropdown_list_id: str):
        super().__init__(node, dropdown_list_id)
        self.locators = {
            **self.locators,
            "validation_circle_icon": ("xpath", ".//span[contains(@class,'anticon-close-circle') "
                                                "or contains(@class,'anticon-check-circle')]"),
            "error_message": ("xpath", ".//div[@class='ant-form-item-explain-error']")
        }

    def get_list_of_error_text(self) -> str:
        return self.error_message.text
