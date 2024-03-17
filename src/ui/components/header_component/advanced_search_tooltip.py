from selenium.webdriver.common.by import By

from src.ui.components.base_component import BaseComponent
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from src.ui.pages.clubs_page import ClubsPage
CATEGORY_NAME_CATEGORIES = (By.XPATH, "//div[contains(@title,\"Категорії\")]")
CATEGORY_NAME_CLUBS = (By.XPATH, "//div[contains(@title,\"Гуртки\")]")


class AdvancedSearchToolTip(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self._driver = driver
        self._category_name_categories = None
        self._category_name_clubs = None
        self._categories = None
        self._clubs = None

    @property
    def category_name_categories(self) -> WebElement:
        if not self._category_name_categories:
            self._category_name_categories = self.node.find_element(*CATEGORY_NAME_CATEGORIES)
        return self._category_name_categories

    @property
    def category_name_clubs(self) -> WebElement:
        if not self._category_name_clubs:
            self._category_name_clubs = self.node.find_element(*CATEGORY_NAME_CLUBS)
        return self._category_name_clubs

    @property
    def categories(self) -> dict[str, WebElement]:
        if not self._categories:
            self._categories = {}
            category_elements = self.node.find_elements(By.XPATH, "//div[@type='category']")
            for category_element in category_elements:
                title = category_element.get_attribute("title")
                self._categories[title] = category_element
        return self._categories

    @property
    def clubs(self) -> dict[str, WebElement]:
        if not self._clubs:
            self._clubs = {}
            club_elements = self.node.find_elements(By.XPATH, "//div[@type='club']")
            for club_element in club_elements:
                title = club_element.get_attribute("title")
                self._clubs[title] = club_element
        return self._clubs

    def get_club_by_title(self, title: str) -> WebElement:
        return self.get_clubs().get(title)

    def get_category_by_title(self, title: str) -> WebElement:
        return self.get_categories().get(title)

    def click_category_by_title(self, title: str) -> ClubsPage:
        self.get_category_by_title(title).click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def click_club_by_title(self, title: str) -> ClubsPage:
        self.get_club_by_title(title).click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()