from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from .base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch
from ..components.pagination_component import PaginationComponent


class AllNewsPage(BasePageWithAdvancedSearch):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators = {
            "news_card_webelements": ("xpath", "//div[@id = 'newsContainer']"),
            "pagination_root": ("xpath", "//ul[contains(@class, 'ant-pagination')]"),
            "club_sider_title": ("xpath", "//div[@class = 'club-sider']//h2"),
            "club_card_webelements": ("xpath", "//div[contains(@class, 'ant-card ')]")
        }

    @property
    def news_card_webelements_list(self) -> list[WebElement]:
        return self.driver.find_elements(*self.locators["news_card_webelements"])

    def get_news_card_list(self) -> list['NewsCardComponent']:
        from ..components.news_card_component import NewsCardComponent
        return [NewsCardComponent(news) for news in self.news_card_webelements_list]

    @property
    def club_card_webelements_list(self) -> list[WebElement]:
        return self.driver.find_elements(*self.locators["club_card_webelements"])

    def get_club_card_list(self) -> list['ClubCardComponent']:
        from ..components.club_card_component import ClubCardComponent
        return [ClubCardComponent(club) for club in self.club_card_webelements_list]

    @property
    def get_pagination(self) -> PaginationComponent:
        return PaginationComponent(self.driver, self.pagination_root)

