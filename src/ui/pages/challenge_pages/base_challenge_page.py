from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch
from src.ui.pages.payment_pages.payment import Payment

CHALLENGE_IMAGE_PATH = "//div[contains(@class,\"banner\")]"
HELP_BUTTON_PATH = "//div[contains(@class,\"help-button\")]"
SOCIAL_MEDIA_PATH = "//div[contains(@class,\"social-info\")]"


class BaseChallengePage(BasePageWithAdvancedSearch):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "challenge_image": ("xpath", CHALLENGE_IMAGE_PATH),
            "challenge_image_text": ("xpath", CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"title\")]"),
            "challenge_description_container": ("xpath", "//div[contains(@class,\"challenge-description\")]"),
            "help_project_button": ("xpath", HELP_BUTTON_PATH + "//button"),
            "contacts_text": ("xpath", SOCIAL_MEDIA_PATH + "//span[contains(@class,\"text\")]"),
            "contacts_social_media_icons": ("xpath", SOCIAL_MEDIA_PATH + "//div[contains(@class,\"links\")]/a"),
            "signup_for_a_challenge_button": ("xpath", "//div[contains(@class,\"button-box\")]//button"),
            "signup_for_a_challenge_button_tooltip": ("xpath", "//div[contains(@class,\"ant-tooltip-inner\")]"),
        }
        self._wait = WebDriverWait(self.driver, 30)

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
        payment_page = Payment(self.driver)
        self._wait.until(EC.visibility_of(payment_page.large_logo_image))
        return payment_page

    def click_sign_up_for_a_challenge_button(self):
        self.signup_for_a_challenge_button.click()
