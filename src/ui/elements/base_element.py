from selenium.webdriver.remote.webelement import WebElement
from src.ui.page_factory.custom_page_factory import CustomPageFactory


class BaseElement(CustomPageFactory):
    def __init__(self, node: WebElement):
        super().__init__()
        self.node = node
        self.driver = node.parent

    def is_displayed(self) -> bool:
        return self.node.is_displayed()

    def get_value_css_property(self, property_name) -> str:
        return self.node.value_of_css_property(property_name)
