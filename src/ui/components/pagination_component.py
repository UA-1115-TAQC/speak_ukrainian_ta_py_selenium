from selenium.webdriver import ActionChains
from src.ui.components.base_component import BaseComponent


class PaginationComponent(BaseComponent):

    def __init__(self,node):
        super().__init__(node)
        self.locators = {
            "previous": ("xpath", ".//li[contains(@class,'ant-pagination-prev')]"),
            "next": ("xpath", ".//li[contains(@class,'ant-pagination-next')]"),
            "items": ("xpath", ".//li[contains(@class, 'ant-pagination-item') or contains(@class, 'ant-pagination-jump-')]"),
        }

    @property
    def items(self):
        return self.node.find_elements(*self.locators["items"])

    def is_next_disabled(self):
        return self.next.get_attribute("aria-disabled") == "true"

    def click_previous(self):
        self.previous.click()
        return self

    def click_next(self):
        self.next.click()
        return self

    def get_item_by_title(self, num):
        for e in self.items:
            if e.get_attribute("title") == num:
                return e
        return None

    def click_page_by_title(self, num):
        self.get_item_by_title(num).click()
        return self

    def get_last_page(self):
        while not self.is_next_disabled():
            self.click_next()
        return self

    def scroll_into_view(self):
        ActionChains(self.driver).move_to_element(self.next).perform()
        return self
