from selenium import webdriver
from selenium.webdriver.common.by import By

from src.ui.components.header_component.header_component import HeaderComponent

HEADER = (By.XPATH, "//header")


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.header = HeaderComponent(self.driver.find_element(*HEADER))
