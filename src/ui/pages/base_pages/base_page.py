from selenium import webdriver
from selenium.webdriver.common.by import By

from src.ui.components.footer_component.footer_component import FooterComponent
from src.ui.components.header_component.header_component import HeaderComponent
from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter
HEADER = (By.XPATH, "//header")
FOOTER = (By.XPATH, "//footer")


class BasePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.driver = driver
        self.header = HeaderComponent(self.driver.find_element(*HEADER))
        self.footer = FooterComponent(self.driver.find_element(*FOOTER))

    def scroll_to_footer(self) -> None:
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
