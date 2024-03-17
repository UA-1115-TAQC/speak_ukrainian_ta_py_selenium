from src.ui.components.base_component import BaseComponent
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class AdvancedSearchToolTip(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self.driver = driver
