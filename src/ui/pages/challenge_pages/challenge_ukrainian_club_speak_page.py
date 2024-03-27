from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChallengeUkrainianClubSpeakPage(BaseChallengePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._driver = driver
