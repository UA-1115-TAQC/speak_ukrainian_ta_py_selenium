from selenium import webdriver
from src.ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
