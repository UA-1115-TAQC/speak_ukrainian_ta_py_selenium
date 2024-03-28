from typing import Self

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.ui.components.carousel.carousel_card_component import CarouselCardComponent
from src.ui.components.carousel.carousel_img_component import CarouselImgComponent
from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch
from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage
from src.ui.pages.challenge_pages.challenge_ukrainian_club_speak_page import ChallengeUkrainianClubSpeakPage
from src.ui.pages.facebook_pages.language_sphere_facebook_page import LanguageSphereFacebookPage

CHALLENGE_DESCRIPTION_PATH = "//div[contains(@class,\"challenge-description\")]"


class HomePage(BasePageWithAdvancedSearch):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "carousel_img_component_element": ("xpath", '//div[contains(@class,"about-carousel-block")]'),
            "carousel_card_component_element": ("xpath", '//div[contains(@class,"categories-carousel-block")]'),
            "challenge_find_out_more_button": ("xpath", CHALLENGE_DESCRIPTION_PATH + "//button"),
            "challenge_description_heading": ("xpath", CHALLENGE_DESCRIPTION_PATH + "/h2"),
            "challenge_description_text": ("xpath", CHALLENGE_DESCRIPTION_PATH + "/span"),
            "challenge_image": ("xpath", '//div[contains(@class,"about-challenge")]//img'),
            "speaking_club_heading": ("xpath", '//div[contains(@class,"speakingclub-description")]//h2'),
            "speaking_club_image": ("xpath", '//img[contains(@class,"banner-image")]'),
        }
        # self._carousel_img_component = None
        # self._carousel_card_component = None
        self._wait = WebDriverWait(self.driver, 30)
        self._jsExecutor = None

    @property
    def carousel_img_component(self):
        # if not self._carousel_img_component:
        #     self._carousel_img_component = CarouselImgComponent(self.driver,
        #                                                         self.carousel_img_component_element)
        return CarouselImgComponent(self.carousel_img_component_element)

    def get_carousel_card_component(self):
        # if not self._carousel_card_component:
        #     self._carousel_card_component =
        return CarouselCardComponent(self.carousel_card_component_element)

    @property
    def challenge_find_out_more_button(self):
        find_out_more_button = self.driver.find_element(self.locators["challenge_find_out_more_button"])
        self._jsExecutor = self.driver.execute_script
        self._jsExecutor("arguments[0].scrollIntoView(true);", find_out_more_button)
        self._wait.until(EC.element_to_be_clickable(find_out_more_button))
        return find_out_more_button


    def click_challenge_find_out_more_button(self) -> BaseChallengePage:
        self.challenge_find_out_more_button.click()
        base_challenge_page = BaseChallengePage(self.driver)
        self._wait.until(EC.visibility_of(base_challenge_page.challenge_image_text))
        return base_challenge_page

    def click_speaking_club_heading(self) -> ChallengeUkrainianClubSpeakPage:
        self.speaking_club_heading.click()
        challenge_ukrainian_club_speak_page = ChallengeUkrainianClubSpeakPage(self.driver)
        self._wait.until(EC.visibility_of(challenge_ukrainian_club_speak_page.challenge_image_text))
        return challenge_ukrainian_club_speak_page

    def click_speaking_club_image(self) -> LanguageSphereFacebookPage:
        previous_tab_amount = len(self.driver.window_handles)
        self.speaking_club_image.click()
        self._wait.until(EC.number_of_windows_to_be(previous_tab_amount + 1))
        self.switch_to_a_new_tab_by_its_index(previous_tab_amount)
        language_sphere_facebook_page = LanguageSphereFacebookPage(self.driver)
        self._wait.until(EC.visibility_of(language_sphere_facebook_page.facebook_logo))
        return language_sphere_facebook_page

    def scroll_to_all_clubs_button(self) -> Self:
        self._jsExecutor = self.driver.execute_script
        self._jsExecutor("arguments[0].scrollIntoView();", self.get_carousel_card_component().carousel_card_all_clubs_button)
        return self

    def scroll_to_footer(self):
        self._jsExecutor = self.driver.execute_script
        self._jsExecutor("window.scrollBy(0,document.body.scrollHeight)")
        return self

    def scroll_to_carousel_card_component_web_element(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.carousel_card_component).perform()
        action.send_keys(Keys.PAGE_DOWN).perform()
        return self

    def wait_until_home_page_is_loaded(self):
        # todo change with config home url
        initial_url = "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/"  # todo change with config home url
        self._wait.until(lambda driver: initial_url == driver.current_url)

    def wait_until_home_page_is_visible(self):
        self._wait.until(EC.visibility_of(self.carousel_card_component))
