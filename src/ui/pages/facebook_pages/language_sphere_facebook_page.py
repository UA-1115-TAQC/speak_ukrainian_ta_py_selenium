from selenium import webdriver

from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter


class LanguageSphereFacebookPage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "facebook_logo": ("xpath", "//body//a[@aria-label=\"Facebook\"]"),
            "initiative_heading": ("xpath", "//body//span[contains(text(),'Сімейний фестиваль \"Мовосфера\"')]"),
        }
