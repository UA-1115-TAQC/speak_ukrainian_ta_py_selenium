from selenium.webdriver import ActionChains
from src.ui.elements.base_element import BaseElement
from selenium.webdriver.common.by import By

SELECT_CLEAR = (By.XPATH, ".//span[contains(@class,'ant-select-clear')]")
INPUT_CONTENT = (By.XPATH, ".//span[contains(@class,'ant-select-selection-placeholder') or contains(@class, 'ant-select-selection-item')]")
INPUT_BOX = (By.XPATH, ".//input[@type='search']")
ITEMS_LIST = (By.XPATH, ".//div[@class ='rc-virtual-list-holder-inner']/div[contains(@class, 'ant-select-item')]")


class LocationSearchSiderElement(BaseElement):

    def __init__(self, driver, node):
        super().__init__(node)
        self._driver = driver
        self._node = node
        self._select_clear = None
        self._input_content = None
        self._input_box = None

    @property
    def select_clear(self):
        if not self._select_clear:
            self._select_clear = self.node.find_element(*SELECT_CLEAR)
        return self._select_clear

    @property
    def input_content(self):
        if not self._input_content:
            self._input_content = self.node.find_element(*INPUT_CONTENT)
        return self._input_content

    @property
    def input_box(self):
        if not self._input_box:
            box = self.node.find_element(*INPUT_BOX)
            xpath = "//div[@id='" + box.get_attribute("aria-owns") + "']/following-sibling::div"
            self._input_box = LocationSearchSiderDropdownElement(self._driver, self.node.find_element(By.XPATH, xpath))
        return self._input_box

    def click_clear(self):
        self.select_clear.click()
        return self

    def click_dropdown(self):
        self._node.click()
        return self

    def select_item(self, item_name):
        self.click_dropdown().input_box.select_item(item_name)
        return self


class LocationSearchSiderDropdownElement(BaseElement):

    def __init__(self, driver, node):
        super().__init__(node)
        self._driver = driver
        self._item_list = None

    @property
    def item_list(self):
        return self.node.find_elements(*ITEMS_LIST)

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
