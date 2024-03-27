from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHALLENGE_IMAGE_PATH = " //div[contains(@class,\"title\") and not(contains(@role,\"menuitem\"))]"


class ChallengeTeachInUkrainian(BaseChallengePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
        self.locators = {
            "challenge_image_text": ("xpath", CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"text\")]"),
            "challenge_image_text_content": ("xpath", CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"content\")]"),
        }

    @property
    def challenge_img_text(self) -> WebElement:
        return self._driver.find_element(*self.locators["challenge_img_text"])

    @property
    def challenge_img_text_content(self) -> WebElement:
        return self._driver.find_element(*self.locators["challenge_img_text_content"])
