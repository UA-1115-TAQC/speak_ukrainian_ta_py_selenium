from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.carousel.basic_carousel_component import BasicCarouselComponent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.ui.components.carousel.club_direction_card import ClubDirectionCard
from src.ui.pages.clubs_page import ClubsPage


class CarouselCardComponent(BasicCarouselComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver, node)
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 30)
        self._node = node
        self.locators = {
            "carousel_card_heading": ("xpath", "//div[contains(@class,\"categories-header\")]/h2"),
            "carousel_card_all_clubs_button": ("xpath", "//div[contains(@class,\"categories-header\")]/a/button"),
        }

        self._carousel_cards = None
        self._active_carousel_cards = None

    @property
    def carousel_card_heading(self) -> WebElement:
        return self._node.find_element(*self.locators["carousel_card_heading"])

    @property
    def carousel_card_all_clubs_button(self) -> WebElement:
        return self._node.find_element(*self.locators["carousel_card_all_clubs_button"])

    @property
    def carousel_cards(self) -> list[ClubDirectionCard]:
        if not self._carousel_cards:
            cards = self.slider_container.find_elements(By.XPATH, ".//div[contains(@class,\"slick-slide\")]")
            for card in cards:
                self._carousel_cards.append(ClubDirectionCard(self._driver, card))
        return self._carousel_cards

    def click_carousel_card_all_clubs_button(self) -> ClubsPage:
        self.carousel_card_all_clubs_button.click()
        return ClubsPage(self._driver).wait_until_clubs_page_is_loaded()

    def get_club_direction_card_by_index(self, index) -> ClubDirectionCard:
        if 0 <= index <= (len(self.carousel_cards) - 1):
            return self.carousel_cards[index]
        raise ValueError("The index must be in the range between 0 and "
                         + str((len(self.carousel_cards) - 1)) + ", inclusive")

    def check_that_the_club_direction_card_obtained_by_index_is_active(self, index) -> bool:
        return self.get_club_direction_card_by_index(index).club_card_heading.is_displayed()

    def get_active_carousel_cards(self) -> list[ClubDirectionCard]:
        if not self._active_carousel_cards:
            self._active_carousel_cards = self.__filter_displayed_cards__(self.carousel_cards)
        old_cards = self._active_carousel_cards
        try:
            self._wait.until(EC.invisibility_of_element(old_cards[(len(old_cards) - 1)].club_card_heading))
            self._active_carousel_cards = self.__filter_displayed_cards__(self.carousel_cards)
        except Exception:
            print("You are already at the beginning/end of the cards list")
        return self._active_carousel_cards

    def __filter_displayed_cards__(self, cards) -> list[ClubDirectionCard]:
        return [card for card in cards if card.club_card_heading.is_displayed()]

    def get_active_carousel_card_by_index(self, index) -> ClubDirectionCard:
        if 0 <= index <= (len(self.get_active_carousel_cards()) - 1):
            return self.get_active_carousel_cards()[index]
        raise ValueError("The index must be in the range between 0 and "
                         + str((len(self.get_active_carousel_cards()) - 1)) + ", inclusive")
