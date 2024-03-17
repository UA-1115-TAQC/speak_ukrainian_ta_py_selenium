from selenium import webdriver
from selenium.webdriver.common.by import By

from src.ui.components.footer_component.footer_component import FooterComponent
from src.ui.components.header_component.header_component import HeaderComponent

HEADER = (By.XPATH, "//header")
FOOTER = (By.XPATH, "//footer")


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.header = HeaderComponent(self.driver.find_element(*HEADER))
        self.footer = FooterComponent(self.driver.find_element(*FOOTER))

    def scroll_to_footer(self) -> None:
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
