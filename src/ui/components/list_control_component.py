from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

SORT_BY_ALPHABET = (By.XPATH, ".//span[text()='за алфавітом']")
SORT_BY_RATING = (By.XPATH, ".//span[text()='за рейтингом']")
ARROW_UP = (By.XPATH, ".//span[contains(@aria-label, 'arrow-up')]")
ARROW_DOWN = (By.XPATH, ".//span[contains(@aria-label, 'arrow-down')]")
WRAPPER_LIST = (By.XPATH, ".//label[contains(@class, 'ant-radio-button-wrapper')][1]")
WRAPPER_BLOCK = (By.XPATH, ".//label[contains(@class, 'ant-radio-button-wrapper')][2]")


class ListControlComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._sort_by_alphabet = None
        self._sort_by_rating = None
        self._arrow_up = None
        self._arrow_down = None
        self._wrapper_list = None
        self._wrapper_block = None

    @property
    def sort_by_alphabet(self):
        if not self._sort_by_alphabet:
            self._sort_by_alphabet = self.node.find_element(*SORT_BY_ALPHABET)
        return self._sort_by_alphabet

    @property
    def sort_by_rating(self):
        if not self._sort_by_rating:
            self._sort_by_rating = self.node.find_element(*SORT_BY_RATING)
        return self._sort_by_rating

    @property
    def arrow_up(self):
        if not self._arrow_up:
            self._arrow_up = self.node.find_element(*ARROW_UP)
        return self._arrow_up

    @property
    def arrow_down(self):
        if not self._arrow_down:
            self._arrow_down = self.node.find_element(*ARROW_DOWN)
        return self._arrow_down

    @property
    def wrapper_list(self):
        if not self._wrapper_list:
            self._wrapper_list = self.node.find_element(*WRAPPER_LIST)
        return self._wrapper_list

    @property
    def wrapper_block(self):
        if not self._wrapper_block:
            self._wrapper_block = self.node.find_element(*WRAPPER_BLOCK)
        return self._wrapper_block

    def click_sort_by_alphabet(self):
        self.sort_by_alphabet.click()

    def click_sort_by_rating(self):
        self.sort_by_rating.click()

    def click_arrow_up(self):
        self.arrow_up.click()

    def click_arrow_down(self):
        self.arrow_down.click()

    def click_wrapper_list(self):
        self.wrapper_list.click()

    def click_wrapper_block(self):
        self.wrapper_block.click()
