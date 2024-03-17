from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch

CAROUSEL_IMG_COMPONENT_ELEMENT = (By.XPATH, '//div[contains(@class,"about-carousel-block")]')
CAROUSEL_CARD_COMPONENT_ELEMENT = (By.XPATH, '//div[contains(@class,"categories-carousel-block")]')
CHALLENGE_IMAGE = (By.XPATH, '//div[contains(@class,"about-challenge")]//img')
SPEAKING_CLUB_HEADING = (By.XPATH, '//div[contains(@class,"speakingclub-description")]//h2')
SPEAKING_CLUB_IMAGE = (By.XPATH, '//img[contains(@class,"banner-image")]')
CHALLENGE_DESCRIPTION_PATH = "//div[contains(@class,\"challenge-description\")]"
CHALLENGE_DESCRIPTION_HEADING = (By.XPATH, CHALLENGE_DESCRIPTION_PATH + "/h2")
CHALLENGE_DESCRIPTION_TEXT = (By.XPATH, CHALLENGE_DESCRIPTION_PATH + "/span")
CHALLENGE_FIND_OUT_MORE_BUTTON = (By.XPATH, CHALLENGE_DESCRIPTION_PATH + "//button")


class HomePage(BasePageWithAdvancedSearch):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._carousel_img_component = None # todo
        self._carousel_card_component = None # todo
        self._challenge_image = None
        self._speaking_club_heading = None
        self._speaking_club_image = None
        self._challenge_find_out_more_button = None
        self._challenge_description_heading = None
        self._challenge_description_text = None
        self._wait = WebDriverWait(self.driver, 30)
        self._jsExecutor = None

    @property
    def carousel_img_component(self):
        if not self._carousel_img_component:
            #todo  self._carousel_img_component = CarouselImgComponent(self.driver, self.carouselImgComponentWebElement)
        return self._carousel_img_component

    @property
    def carousel_card_component(self):
        if not self._carousel_card_component:
            #todo   self._carousel_card_component= CarouselCardComponent(self.driver, self.carouselCardComponentWebElement)
        return self._carousel_card_component

    @property
    def challenge_find_out_more_button(self):
        if not self._challenge_find_out_more_button:
            self._challenge_find_out_more_button = self._driver.find_element(*CHALLENGE_FIND_OUT_MORE_BUTTON)
        self._jsExecutor = self.driver.execute_script
        self._jsExecutor("arguments[0].scrollIntoView(true);", self._challenge_find_out_more_button)
        self._wait.until(EC.element_to_be_clickable(self._challenge_find_out_more_button))
        return self._challenge_find_out_more_button

    @property
    def challenge_description_heading(self):
        if not self._challenge_description_heading:
            self._challenge_description_heading = self._driver.find_element(*CHALLENGE_DESCRIPTION_HEADING)
        return self._challenge_description_heading

    @property
    def challenge_description_text(self):
        if not self._challenge_description_text:
            self._challenge_description_text = self._driver.find_element(*CHALLENGE_DESCRIPTION_TEXT)
        return self._challenge_description_text

    @property
    def challenge_image(self):
        if not self._challenge_image:
            self._challenge_image = self._driver.find_element(*CHALLENGE_IMAGE)
        return self._challenge_image
    @property
    def speaking_club_heading(self):
        if not self._speaking_club_heading:
            self._speaking_club_heading = self._driver.find_element(*SPEAKING_CLUB_HEADING)
        return self._speaking_club_heading

    @property
    def speaking_club_image(self):
        if not self._speaking_club_image:
            self._speaking_club_image = self._driver.find_element(*SPEAKING_CLUB_IMAGE)
        return self._speaking_club_image

    def click_challenge_find_out_more_button(self):
        self.challenge_find_out_more_button.click()
        #base_challenge_page = BaseChallengePage(self.driver) #todo
        #self._wait.until(EC.visibility_of(baseChallengePage.challengeImageText)) #todo
        #return base_challenge_page

    def clickSpeakingClubHeading(self):
        self.speaking_club_heading.click()
        # challenge_ukrainian_club_speak_page = ChallengeUkrainianClubSpeakPage(self.driver) #todo
        #self._wait.until(EC.visibility_of(challengeUkrainianClubSpeakPage.challengeImageText)) #todo
        #return challenge_ukrainian_club_speak_page

    def click_speaking_club_image(self):
        previous_tab_amount = len(self.driver.window_handles)
        self.speaking_club_image.click()
        self._wait.until(EC.number_of_windows_to_be(previous_tab_amount + 1))
        #self.switchToANewTabByItsIndex(previous_tab_amount) #todo
       # language_sphere_facebook_page = LanguageSphereFacebookPage(self.driver) #todo
        #self._wait.until(EC.visibility_of(language_sphere_facebook_page.facebookLogo)) #todo
        #return language_sphere_facebook_page

    def scroll_to_all_clubs_button(self):
        self._jsExecutor = self.driver.execute_script
        #self._jsExecutor("arguments[0].scrollIntoView();", self.carousel_card_component.carouselCardAllClubsButton) #todo
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
        initial_url = "http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/" #todo change with config home url
        self._wait.until(lambda driver: initial_url == driver.current_url)

    def wait_until_home_page_is_visible(self):
        self._wait.until(EC.visibility_of(self.carousel_card_component))