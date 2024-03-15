from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver:webdriver ) -> None:
        self.driver = driver

class BaseComponent:
    def __init__(self, node:WebElement) -> None:
        self.node = node