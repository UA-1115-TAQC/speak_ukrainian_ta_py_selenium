import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.elements.base_element import BaseElement

DROPDOWN = (By.XPATH, ".//div[contains(@class,'ant-select-selector')]")
DROPDOWN_LABEL = (By.XPATH, "./ancestor::div[contains(@class,'ant-form-item')]"
                            "/preceding-sibling::span[contains(@class,'ant-typography')][1]")
ARROW_ICON = (By.XPATH, ".//span[contains(@class,'ant-select-arrow')]/span[@aria-label='down']")
PLACEHOLDER = (By.XPATH, ".//span[@class='ant-select-selection-placeholder']")
SELECTED_ITEM = (By.XPATH, ".//span[@class='ant-select-selection-item']")
DROPDOWN_CONTAINER = (By.XPATH, "//div[@class='rc-virtual-list-holder']")
DROPDOWN_ITEMS_LIST = (By.XPATH, "//div[@class='rc-virtual-list']"
                                 "/descendant::div[contains(@class,'ant-select-item ant-select-item-option')]")


class Dropdown(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._dropdown = None
        self._dropdown_label = None
        self._arrow_icon = None
        self._placeholder = None
        self._selected_item = None
        self._dropdown_container = None

    @property
    def dropdown(self) -> WebElement:
        if not self._dropdown:
            self._dropdown = self.node.find_element(*DROPDOWN)
        return self._dropdown

    def click_dropdown(self):
        self.dropdown.click()
        return self

    @property
    def dropdown_label(self) -> WebElement:
        if not self._dropdown_label:
            self._dropdown_label = self.node.find_element(*DROPDOWN_LABEL)
        return self._dropdown_label

    @property
    def arrow_icon(self) -> WebElement:
        if not self._arrow_icon:
            self._arrow_icon = self.node.find_element(*ARROW_ICON)
        return self._arrow_icon

    @property
    def placeholder(self) -> WebElement:
        if not self._placeholder:
            self._placeholder = self.node.find_element(*PLACEHOLDER)
        return self._placeholder

    @property
    def selected_item(self) -> WebElement:
        if not self._selected_item:
            self._selected_item = self.node.find_element(*SELECTED_ITEM)
        return self._selected_item

    @property
    def dropdown_container(self) -> WebElement:
        if not self._dropdown_container:
            self._dropdown_container = self.node.find_element(*DROPDOWN_CONTAINER)
        return self._dropdown_container

    def get_visible_dropdown_items_list(self) -> list[WebElement]:
        return self.node.find_elements(*DROPDOWN_ITEMS_LIST)

    @property
    def dropdown_options_list(self) -> set[WebElement]:
        driver = self.node.parent
        wait = WebDriverWait(driver, 5)
        wait.until(lambda d: self.dropdown_container.is_displayed())
        driver.execute_script("arguments[0].scrollTop = 0", self.dropdown_container)
        option_titles = set()
        while True:
            list_size = len(option_titles)
            for option in self.get_visible_dropdown_items_list():
                option_titles.add(option)
            if list_size == len(option_titles):
                break
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                  self.dropdown_container)
            time.sleep(0.5)
        return option_titles

    def get_text_dropdown_options_list(self) -> list[str]:
        return [item.get_attribute("title") for item in self.dropdown_options_list]

    def select_value(self, value: str) -> None:
        driver = self.node.parent
        wait = WebDriverWait(driver, 5)
        wait.until(lambda d: self.dropdown_container.is_displayed())
        driver.execute_script("arguments[0].scrollTop = 0", self.dropdown_container)
        while True:
            list = []
            for item in self.get_visible_dropdown_items_list():
                title = item.get_attribute("title")
                list.append(title)
                if title == value:
                    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", item)
                    return
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                  self.dropdown_container)
            time.sleep(0.5)
            new_list = [item.get_attribute("title") for item in self.get_visible_dropdown_items_list()]
            if list == new_list:
                break
