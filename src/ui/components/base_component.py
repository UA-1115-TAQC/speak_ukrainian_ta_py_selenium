from selenium.webdriver.remote.webelement import WebElement
from src.ui.page_factory.custom_page_factory import CustomPageFactory


class BaseComponent(CustomPageFactory):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node.parent, node)

