from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch
from src.ui.pages.payment_pages.payment import Payment
CHALLENGE_IMAGE_PATH = "//div[contains(@class,\"banner\")]"
HELP_BUTTON_PATH = "//div[contains(@class,\"help-button\")]"
SOCIAL_MEDIA_PATH = "//div[contains(@class,\"social-info\")]"

CHALLENGE_IMAGE = (By.XPATH, CHALLENGE_IMAGE_PATH)
CHALLENGE_IMAGE_TEXT = (By.XPATH, CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"title\")]")
HELP_PROJECT_BUTTON = (By.XPATH, HELP_BUTTON_PATH + "//button")
HELP_PROJECT_LINK = (By.XPATH, HELP_BUTTON_PATH + "/a")
CONTACTS_TEXT = (By.XPATH, SOCIAL_MEDIA_PATH + "//span[contains(@class,\"text\")]")
CONTACTS_SOCIAL_MEDIA_ICONS = (By.XPATH, SOCIAL_MEDIA_PATH + "//div[contains(@class,\"links\")]/a")
CHALLENGE_DESCRIPTION_CONTAINER = (By.XPATH, "//div[contains(@class,\"challenge-description\")]")
SIGN_UP_FOR_A_CHALLENGE_BUTTON = (By.XPATH, "//div[contains(@class,\"button-box\")]//button")
SIGN_UP_FOR_A_CHALLENGE_BUTTON_TOOLTIP = (By.XPATH, "//div[contains(@class,\"ant-tooltip-inner\")]")


class BaseChallengePage(BasePageWithAdvancedSearch):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self._challenge_image = None
        self._challenge_image_text = None
        self._challenge_description_container = None
        self._help_project_button = None
        self._help_project_link = None
        self._contacts_text = None
        self._contacts_social_media_icons = None
        self._signup_for_a_challenge_button = None
        self._signup_for_a_challenge_button_tooltip = None
        self._wait = WebDriverWait(self.driver, 30)

    @property
    def challenge_image(self) -> WebElement:
        if not self._challenge_image:
            self._challenge_image = self._driver.find_element(*CHALLENGE_IMAGE)
        return self._challenge_image

    @property
    def challenge_image_text(self) -> WebElement:
        if not self._challenge_image_text:
            self._challenge_image_text = self._driver.find_element(*CHALLENGE_IMAGE_TEXT)
        return self._challenge_image_text

    @property
    def challenge_description_container(self) -> WebElement:
        if not self._challenge_description_container:
            self._challenge_description_container = self._driver.find_element(*CHALLENGE_DESCRIPTION_CONTAINER)
        return self._challenge_description_container

    @property
    def help_project_button(self) -> WebElement:
        if not self._help_project_button:
            self._help_project_button = self._driver.find_element(*HELP_PROJECT_BUTTON)
        return self._help_project_button

    @property
    def help_project_link(self) -> WebElement:
        if not self._help_project_link:
            self._help_project_link = self._driver.find_element(*HELP_PROJECT_LINK)
        return self._help_project_link

    @property
    def contacts_text(self) -> WebElement:
        if not self._contacts_text:
            self._contacts_text = self._driver.find_element(*CONTACTS_TEXT)
        return self._contacts_text

    @property
    def contacts_social_media_icons(self) -> list[WebElement]:
        if not self._contacts_social_media_icons:
            self._contacts_social_media_icons = self._driver.find_elements(*CONTACTS_SOCIAL_MEDIA_ICONS)
        return self._contacts_social_media_icons

    @property
    def signup_for_a_challenge_button(self) -> WebElement:
        if not self._signup_for_a_challenge_button:
            self._signup_for_a_challenge_button = self._driver.find_element(*SIGN_UP_FOR_A_CHALLENGE_BUTTON)
        return self._signup_for_a_challenge_button

    @property
    def signup_for_a_challenge_button_tooltip(self) -> WebElement:
        if not self._signup_for_a_challenge_button_tooltip:
            self._signup_for_a_challenge_button_tooltip = (self._driver
                                                           .find_element(*SIGN_UP_FOR_A_CHALLENGE_BUTTON_TOOLTIP))
        return self._signup_for_a_challenge_button_tooltip

    def get_social_media_icon_by_index(self, index) -> WebElement:
        if 0 <= index < len(self.contacts_social_media_icons):
            return self.contacts_social_media_icons[index]
        raise ValueError("The index must be between 0 and "
                         + str(len(self.contacts_social_media_icons) - 1) + ", inclusive.")

    def click_social_media_icon_by_index(self, index):
        previous_tab_amount = len(self.get_tab_handles())
        self.get_social_media_icon_by_index(index).click()
        self._wait.until(EC.number_of_windows_to_be(previous_tab_amount + 1))
        self.switch_to_a_new_tab_by_its_index(previous_tab_amount)

    def click_help_project_button(self) -> Payment:
        previous_tab_amount = len(self.get_tab_handles())
        self.help_project_button.click()
        self._wait.until(EC.number_of_windows_to_be(previous_tab_amount + 1))
        self.switch_to_a_new_tab_by_its_index(previous_tab_amount)
        payment_page = Payment(self._driver)
        self._wait.until(EC.visibility_of(payment_page.large_logo_image))
        return payment_page

    def click_sign_up_for_a_challenge_button(self):
        self.signup_for_a_challenge_button.click()
