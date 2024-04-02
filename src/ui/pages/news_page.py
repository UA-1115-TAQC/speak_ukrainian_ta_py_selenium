from selenium import webdriver
from .base_pages.base_page import BasePage


class NewsPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "news_image": ("xpath", "//div[@class = 'image']"),
            "news_date": ("xpath", "//div[@id= 'date']"),
            "news_text": ("xpath", "//div[@id = 'description']"),
            "help_project_button": ("xpath", "//div[@class = 'social-info']/descendant::button"),
            "news_carousel_title": ("xpath", "//div[@class = 'other-news']/div[@class = 'title']"),
            "news_page_carousel_root": ("xpath", "//div[@class = 'news-carousel-block']"),
            "social_info_root": ("xpath", "//div[@class='social-info']")
        }
        self.social_info_component = None

    def click_help_project_button(self) -> None:
        self.help_project_button.click_button()
