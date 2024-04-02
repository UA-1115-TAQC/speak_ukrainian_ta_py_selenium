from selenium.webdriver.remote.webelement import WebElement

from .base_component import BaseComponent


class NewsCardComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "news_card_image": ("xpath", "//div[@id = 'newsImage']"),
            "news_card_date": ("xpath", "//div[@id = 'newsDate']"),
            "news_card_title": ("xpath", "//div[@id = 'newsTitle']"),
            "news_card_link": ("xpath", ".//a[contains(@href, '/news/')]")
        }

    def click_news_card_link(self) -> 'NewsPage':
        self.news_card_link.click_button()
        from ..pages.news_page import NewsPage
        return NewsPage(self.driver)

    def get_news_card_title(self) -> str:
        return self.news_card_title.text

    def get_news_card_date(self) -> str:
        return self.news_card_date.text
