from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
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
        self.club_card_heading.click_button()
        return ClubsPage(self.driver).wait_until_clubs_page_is_loaded()

    def is_active_by_class(self):
        return "slick-active" in self.node.get_attribute("class")

    def wait_till_button_is_active(self):
        self.get_wait(60).until(ec.element_to_be_clickable(self.locators["club_card_button"]))
