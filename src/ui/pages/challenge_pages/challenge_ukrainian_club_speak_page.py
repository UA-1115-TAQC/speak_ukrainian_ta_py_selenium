from selenium import webdriver

from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage


class ChallengeUkrainianClubSpeakPage(BaseChallengePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
