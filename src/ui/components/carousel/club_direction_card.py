from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.ui.pages.clubs_page import ClubsPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ClubDirectionCard(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver)
        self._driver = driver
        self._node = node
        self.locators = {
            "club_card_image": ("xpath", ".//div[contains(@class,\"icon-box\")]/img"),
            "club_card_heading": ("xpath", ".//div[contains(@class,\"name\")]"),
            "club_card_text": ("xpath", ".//div[contains(@class,\"description\")]"),
            "club_card_button": ("xpath", ".//div[contains(@class,\"details\")]"),
            "club_card_button_pointer": ("xpath", ".//span[@aria-label=\"arrow-right\"]"),
        }

    @property
    def club_card_image(self) -> WebElement:
        return self._node.find_element(*self.locators["club_card_image"])

    @property
    def club_card_heading(self) -> WebElement:
        return self._node.find_element(*self.locators["club_card_heading"])

    @property
    def club_card_text(self) -> WebElement:
        return self._node.find_element(*self.locators["club_card_text"])

    @property
    def club_card_button(self) -> WebElement:
        return self._node.find_element(*self.locators["club_card_button"])

    @property
    def club_card_button_pointer(self) -> WebElement:
        return self._node.find_element(*self.locators["club_card_button_pointer"])

    def click_club_card_button(self) -> ClubsPage:
        self.club_card_button.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def click_club_card_button_pointer(self) -> ClubsPage:
        self.club_card_button_pointer.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def click_card(self) -> ClubsPage:
        self.club_card_text.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()
