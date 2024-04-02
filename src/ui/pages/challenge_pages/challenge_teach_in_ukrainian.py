from selenium import webdriver

from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage

CHALLENGE_IMAGE_PATH = " //div[contains(@class,\"title\") and not(contains(@role,\"menuitem\"))]"


class ChallengeTeachInUkrainian(BaseChallengePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "challenge_image_text": ("xpath", CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"text\")]"),
            "challenge_image_text_content": ("xpath", CHALLENGE_IMAGE_PATH + "/span[contains(@class,\"content\")]"),
        }

