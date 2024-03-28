from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory


class CustomPageFactory(PageFactory):

    def __init__(self, driver=None, node=None):
        super().__init__()
        self.node = node
        self.driver = driver

    def get_web_element(self, *loc):
        element = self.driver.find_element(*loc) if self.node is None else self.node.find_element(*loc)
        self.highlight_web_element(element)
        return element

    def get_wait(self, timeout: int):
        return WebDriverWait(self.driver, timeout)

    def get_actions(self):
        return ActionChains(self.driver)
