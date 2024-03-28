from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.ui.elements.base_element import BaseElement


class LocationSearchSiderElement(BaseElement):

    def __init__(self, driver, node):
        super().__init__(node)
        self.locators = {
            "select_clear": ("xpath", ".//span[contains(@class,'ant-select-clear')]"),
            "input_content": ("xpath", ".//span[contains(@class,'ant-select-selection-placeholder') or contains(@class, 'ant-select-selection-item')]"),
            "input_box": ("xpath", ".//input[@type='search']"),
        }
        self._driver = driver
        self._node = node

    @property
    def dropdown_box(self):
        xpath = "//div[@id='" + self.input_box.get_attribute("aria-owns") + "']/following-sibling::div"
        return LocationSearchSiderDropdownElement(self._driver, self.node.find_element(By.XPATH, xpath))

    def click_clear(self):
        ActionChains(self._driver).move_to_element(self._node).perform()
        self.select_clear.click()
        return self

    def click_dropdown(self):
        self._node.click()
        return self

    def select_item(self, item_name):
        self.click_dropdown().dropdown_box.select_item(item_name)
        return self


class LocationSearchSiderDropdownElement(BaseElement):

    def __init__(self, driver, node):
        super().__init__(node)
        self.locators = {
            "item_list": ("xpath", ".//div[@class ='rc-virtual-list-holder-inner']/div[contains(@class, 'ant-select-item')]"),
        }
        self._driver = driver

    @property
    def item_list(self):
        return self.node.find_elements(*self.locators["item_list"])

    def select_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            ActionChains(self._driver).move_to_element(item).perform()
            item.click()

    def find_item(self, item_name):
        self.go_to_the_list_top()
        while True:
            goal_item = self.find_in_list(item_name)
            if goal_item:
                return goal_item
            current_last_element = self.item_list[len(self.item_list) - 1]
            ActionChains(self._driver).move_to_element(current_last_element).perform()
            new_last_element = self.item_list[len(self.item_list) - 1]
            if current_last_element == new_last_element:
                break
        return None

    def find_in_list(self, item_name):
        for item in self.item_list:
            title = item.get_attribute("title")
            if title == item_name:
                return item
        return None

    def go_to_the_list_top(self):
        while True:
            current_first_element = self.item_list[0]
            ActionChains(self._driver).move_to_element(current_first_element).perform()
            new_first_element = self.item_list[0]
            if current_first_element == new_first_element:
                return
