from selenium import webdriver

from src.ui.components.footer_component.footer_component import FooterComponent
from src.ui.components.header_component.header_component import HeaderComponent
from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter


class BasePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "header_locator": ("xpath", "//header"),
            "footer_locator": ("xpath", "//footer"),
            "top_notice_message": ("xpath", "//div[@class='ant-message-notice-wrapper']/descendant::div[contains(@class, 'ant-message-error') " 
                                            "or contains(@class, 'ant-message-success')]")
        }

    @property
    def header(self) -> HeaderComponent:
        return HeaderComponent(self.header_locator)

    @property
    def footer(self) -> FooterComponent:
        return FooterComponent(self.footer_locator)

    def get_top_notice_message(self):
        return self.top_notice_message.get_text()
