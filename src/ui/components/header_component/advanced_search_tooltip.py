from selenium.webdriver.common.by import By

from src.ui.components.base_component import BaseComponent
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class AdvancedSearchToolTip(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(node)
        self._driver = driver
        self.locators = {
            "category_name_categories": ("xpath", "//div[contains(@title,\"Категорії\")]"),
            "category_name_clubs": ("xpath", "//div[contains(@title,\"Гуртки\")]"),
        }
        self._categories = None
        self._clubs = None

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

    def click_category_by_title(self, title: str):
        self.get_category_by_title(title).click()

    def click_club_by_title(self, title: str):
        self.get_club_by_title(title).click()
