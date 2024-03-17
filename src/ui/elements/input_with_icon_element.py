from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.input import Input


class InputWithIconElement(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
