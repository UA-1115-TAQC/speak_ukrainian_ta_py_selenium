from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.carousel.basic_carousel_component import BasicCarouselComponent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.ui.components.carousel.carousel_img_card import CarouselImgCard


class CarouselImgComponent(BasicCarouselComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._wait = WebDriverWait(self.driver, 60)
        self._switching_carousel_img_cards: dict[int, WebElement] = {}
        self._active_carousel_img_card = None
        self._actions = ActionChains(self.driver)

    @property
    def switching_carousel_img_cards(self) -> dict[int, WebElement]:
        if not self._switching_carousel_img_cards:
            img_cards = self.slider_container.find_elements(By.XPATH, ".//div[contains(@class,\"slick-slide\")]")
            for img_card in img_cards:
                data_index = int(img_card.get_attribute("data-index"))
                if 0 <= data_index <= 2:
                    self._switching_carousel_img_cards[data_index] = img_card
        return self._switching_carousel_img_cards

    @property
    def active_carousel_img_card(self) -> CarouselImgCard:
        data_index = self.find_active_carousel_img_card_index()
        if not self._active_carousel_img_card:
            self._active_carousel_img_card = CarouselImgCard(self.driver,
                                                             self.switching_carousel_img_cards[data_index])
        else:
            old_card = self._active_carousel_img_card
            self._wait.until(EC.invisibility_of_element(old_card.card_heading))
            self._active_carousel_img_card = CarouselImgCard(self.driver,
                                                             self.switching_carousel_img_cards[data_index])
        return self._active_carousel_img_card

    def get_carousel_img_card_by_data_index(self, data_index: int) -> CarouselImgCard:
        if 0 <= data_index < len(self.switching_carousel_img_cards):
            img_card = self.switching_carousel_img_cards[data_index]
            self._wait.until(EC.visibility_of(img_card))
            return CarouselImgCard(self.driver, img_card)
        raise ValueError("The index must be in the range from 0 to "
                         + str(len(self.switching_carousel_img_cards) - 1) + ", inclusive.")

    def find_active_carousel_img_card_index(self) -> int:
        for i, card in self.switching_carousel_img_cards.items():
            if "active" in card.get_attribute("class"):
                return i
        return 0

    def wait_until_the_card_is_displayed_by_index(self, i: int):
        if not self.get_carousel_img_card_by_data_index(i).card_button.is_displayed():
            self._wait.until(EC.visibility_of(self.get_carousel_img_card_by_data_index(i).card_button))

    def hover_over_card_button(self, i: int):
        self._actions.move_to_element(self.get_carousel_img_card_by_data_index(i).card_button_text).perform()
