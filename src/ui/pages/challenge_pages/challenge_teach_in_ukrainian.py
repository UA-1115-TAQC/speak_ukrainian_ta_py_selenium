from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHALLENGE_IMAGE_PATH = " //div[contains(@class,\"title\") and not(contains(@role,\"menuitem\"))]"

CHALLENGE_IMAGE_TEXT = (By.XPATH, CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"text\")]")
CHALLENGE_IMAGE_TEXT_CONTENT = (By.XPATH, CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"content\")]")


class ChallengeTeachInUkrainian(BaseChallengePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self._challenge_image_text = None
        self._challenge_image_text_content = None

    @property
    def challenge_img_text(self) -> WebElement:
        if not self._challenge_image_text:
            self._challenge_image_text= self._driver.find_element(*CHALLENGE_IMAGE_TEXT)
        return self._challenge_image_text

    @property
    def challenge_img_text_content(self) -> WebElement:
        if not self._challenge_image_text_content:
            self._challenge_image_text_content = self._driver.find_element(*CHALLENGE_IMAGE_TEXT_CONTENT)
        return self._challenge_image_text_content
