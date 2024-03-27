from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.ui.pages.clubs_page import ClubsPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

CLUB_CARD_IMAGE = (By.XPATH, ".//div[contains(@class,\"icon-box\")]/img")
CLUB_CARD_HEADING = (By.XPATH, ".//div[contains(@class,\"name\")]")
CLUB_CARD_TEXT = (By.XPATH, ".//div[contains(@class,\"description\")]")
CLUB_CARD_BUTTON = (By.XPATH, ".//div[contains(@class,\"details\")]")
CLUB_CARD_BUTTON_POINTER = (By.XPATH, ".//span[@aria-label=\"arrow-right\"]")


class ClubDirectionCard(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver)
        self._driver = driver
        self._node = node
        self._club_card_image = None
        self._club_card_heading = None
        self._club_card_text = None
        self._club_card_button = None
        self._club_card_button_pointer = None

    @property
    def club_card_image(self) -> WebElement:
        if not self._club_card_image:
            self._club_card_image = self._node.find_element(*CLUB_CARD_IMAGE)
        return self._club_card_image

    @property
    def club_card_heading(self) -> WebElement:
        if not self._club_card_heading:
            self._club_card_heading = self._node.find_element(*CLUB_CARD_HEADING)
        return self._club_card_heading

    @property
    def club_card_text(self) -> WebElement:
        if not self._club_card_text:
            self._club_card_text = self._node.find_element(*CLUB_CARD_TEXT)
        return self._club_card_text

    @property
    def club_card_button(self) -> WebElement:
        if not self._club_card_button:
            self._club_card_button = self._node.find_element(*CLUB_CARD_BUTTON)
        return self._club_card_button

    @property
    def club_card_button_pointer(self) -> WebElement:
        if not self._club_card_button_pointer:
            self._club_card_button_pointer = self._node.find_element(*CLUB_CARD_BUTTON_POINTER)
        return self._club_card_button_pointer

    def click_club_card_button(self) -> ClubsPage:
        self.club_card_button.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def click_club_card_button_pointer(self) -> ClubsPage:
        self.club_card_button_pointer.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def click_card(self) -> ClubsPage:
        self.club_card_text.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()
