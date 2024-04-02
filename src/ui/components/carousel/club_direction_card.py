from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent
from src.ui.pages.clubs_page import ClubsPage


class ClubDirectionCard(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "club_card_image": ("xpath", ".//div[contains(@class,\"icon-box\")]/img"),
            "club_card_heading": ("xpath", ".//div[contains(@class,\"name\")]"),
            "club_card_text": ("xpath", ".//div[contains(@class,\"description\")]"),
            "club_card_button": ("xpath", ".//div[contains(@class,\"details\")]"),
            "club_card_button_pointer": ("xpath", ".//span[@aria-label=\"arrow-right\"]"),
        }


    def click_club_card_button(self) -> ClubsPage:
        self.club_card_button.click()
        return ClubsPage(self.driver).wait_until_clubs_page_is_loaded()

    def click_club_card_button_pointer(self) -> ClubsPage:
        self.club_card_button_pointer.click()
        return ClubsPage(self.driver).wait_until_clubs_page_is_loaded()

    def click_card(self) -> ClubsPage:
        self.club_card_text.click()
        return ClubsPage(self.driver).wait_until_clubs_page_is_loaded()
