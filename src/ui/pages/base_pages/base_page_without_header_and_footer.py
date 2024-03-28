from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from seleniumpagefactory import PageFactory

from src.ui.page_factory.custom_page_factory import CustomPageFactory


class BasePageWithoutHeaderAndFooter(CustomPageFactory):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._current_tab_handle = None
        self._tab_handles = None

    def get_current_tab_handle(self) -> str:
        self._current_tab_handle = self._driver.get_current_window_handle()
        return self._current_tab_handle

    def get_tab_handles(self) -> list:
        self._tab_handles = self._driver.get_window_handles()
        return self._tab_handles

    def check_that_a_page_is_opened_in_a_new_tab(self, previous_handle, new_handle) -> bool:
        return previous_handle == new_handle and (len(self.get_tab_handles()) == 2)

    def switch_to_a_new_tab_by_its_index(self, index):
        if 0 <= index < len(self.get_tab_handles()):
            self._driver.switchTo().window(self.get_tab_handles()[index])
        else:
            raise ValueError("The index must be in the range from 0 to "
                             + str((len(self.get_tab_handles()) - 1)) + ", inclusive")
