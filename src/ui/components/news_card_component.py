from .base_component import BaseComponent
from selenium.webdriver.remote.webelement import WebElement


class NewsCardComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "news_card_image": ("xpath", "//div[@id = 'newsImage']"),
            "news_card_date": ("xpath", "//div[@id = 'newsDate']"),
            "news_card_title": ("xpath", "//div[@id = 'newsTitle']"),
            "news_card_link": ("xpath", ".//a[contains(@href, '/news/')]")
        }

    def get_news_card_title(self) -> str:
        return self.news_card_title.text

    def get_news_card_date(self) -> str:
        return self.news_card_date.text
