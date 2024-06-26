from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent


class ListControlComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "sort_by_alphabet": ("xpath", ".//span[text()='за алфавітом']"),
            "sort_by_rating": ("xpath", ".//span[text()='за рейтингом']"),
            "arrow_up": ("xpath", ".//span[contains(@aria-label, 'arrow-up')]"),
            "arrow_down": ("xpath", ".//span[contains(@aria-label, 'arrow-down')]"),
            "wrapper_list": ("xpath", ".//label[contains(@class, 'ant-radio-button-wrapper')][1]"),
            "wrapper_block": ("xpath", ".//label[contains(@class, 'ant-radio-button-wrapper')][2]"),
        }

    def click_sort_by_alphabet(self):
        self.sort_by_alphabet.click()
        return self

    def click_sort_by_rating(self):
        self.sort_by_rating.click()
        return self

    def click_arrow_up(self):
        self.arrow_up.click()
        self.wait_arrow_change(self.arrow_up)
        return self

    def click_arrow_down(self):
        self.arrow_down.click()
        self.wait_arrow_change(self.arrow_down)
        return self

    def click_wrapper_list(self):
        self.wrapper_list.click()
        return self

    def click_wrapper_block(self):
        self.wrapper_block.click()
        return self

    def wait_arrow_change(self, arrow_element):
        self.get_wait(20).until(lambda wd: arrow_element.get_attribute("style") == "color: rgb(255, 192, 105);")
