from typing import Self
from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.base_element import BaseElement


class Dropdown(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "dropdown": ("xpath", ".//div[contains(@class,'ant-select-selector')]"),
            "dropdown_label": ("xpath", "./ancestor::div[contains(@class,'ant-form-item')]"
                                        "/preceding-sibling::span[contains(@class,'ant-typography')][1]"),
            "arrow_icon": ("xpath", ".//span[contains(@class,'ant-select-arrow')]/span[@aria-label='down']"),
            "placeholder": ("xpath", ".//span[@class='ant-select-selection-placeholder']"),
            "selected_item": ("xpath", ".//span[@class='ant-select-selection-item']"),
            "dropdown_container": ("xpath", "//div[@class='rc-virtual-list-holder']"),
            "dropdown_items_list": ("xpath", "//div[@class='rc-virtual-list']"
                                             "/descendant::div[contains(@class,'ant-select-item ant-select-item-option')]")
        }

    def click_dropdown(self) -> Self:
        self.dropdown.click_button()
        return self

    def get_dropdown_label_text(self) -> str:
        return self.dropdown_label.text

    def visible_items_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["dropdown_items_list"])

    def scroll_to_top(self):
        while True:
            current_first_item = self.visible_items_list()[0]
            self.get_actions().move_to_element(current_first_item).perform()
            if current_first_item == self.visible_items_list()[0]:
                return

    def select_item(self, item_name) -> Self:
        self.scroll_to_top()
        while True:
            for item in self.visible_items_list():
                if item.get_attribute("title").strip() == item_name:
                    self.get_actions().move_to_element(item).click().perform()
                    return self
            current_last_element = self.visible_items_list()[-1]
            self.get_actions().move_to_element(current_last_element).perform()
            if current_last_element == self.visible_items_list()[-1]:
                break
        return self

    def get_dropdown_placeholder_text(self) -> str:
        return self.placeholder.text

    def get_dropdown_selected_item_text(self) -> str:
        return self.selected_item.text
