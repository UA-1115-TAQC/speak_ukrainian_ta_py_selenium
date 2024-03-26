from selenium import webdriver

from src.ui.components.footer_component.footer_component import FooterComponent
from src.ui.components.header_component.header_component import HeaderComponent
from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter


class BasePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "header_locator": ("xpath", "//header"),
            "footer": ("xpath", "//footer")
        }

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.header_locator)

    @property
    def footer(self) -> FooterComponent:
        return FooterComponent(self.footer_locator)

    def scroll_to_footer(self) -> None:
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
