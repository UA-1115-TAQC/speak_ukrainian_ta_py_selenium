from selenium.webdriver import ActionChains

from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

PREVIOUS = (By.XPATH, ".//li[contains(@class,'ant-pagination-prev')]")
NEXT = (By.XPATH, ".//li[contains(@class,'ant-pagination-next')]")
PAGINTION_ITEMS = (By.XPATH, ".//li[contains(@class, 'ant-pagination-item') or contains(@class, 'ant-pagination-jump-')]")


class PaginationComponent(BaseComponent):

    def __init__(self, driver, node):
        super().__init__(node)
        self._driver = driver
        self._previous = None
        self._next = None
        self._items = None

    @property
    def previous(self):
        if not self._previous:
            self._previous = self.node.find_element(*PREVIOUS)
        return self._previous

    @property
    def next(self):
        if not self._next:
            self._next = self.node.find_element(*NEXT)
        return self._next

    @property
    def items(self):
        if not self._items:
            self._items = self.node.find_elements(*PAGINTION_ITEMS)
        return self._items

    def is_next_disabled(self):
        disabled = self.next.get_attribute("aria-disabled")
        return disabled == "true"

    def click_previous(self):
        self.previous.click()

    def click_next(self):
        self.next.click()

    def get_item_by_title(self, num):
        for e in self.items:
            if e.get_attribute("title") == num:
                return e
        return None

    def click_page_by_title(self, num):
        self.get_item_by_title(num).click()

    def get_last_page(self):
        while not self.is_next_disabled():
            self.click_next()

    def scroll_into_view(self):
        ActionChains(self._driver).move_to_element(self.next).perform()
