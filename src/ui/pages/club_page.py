from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.ui.components.rating_component import RatingComponent
from src.ui.pages.base_pages import base_page

RATING = (By.XPATH, "./descendant::ul[@role='radiogroup']")
SIGN_UP_TO_CLUB = (By.XPATH, "./descendant::span[text()='Записатись на гурток']")
WRITE_TO_MANAGER = (By.XPATH, "./descendant::span[text()='Написати менеджеру']")
CLUB_DESCRIPTION = (By.XPATH, "./descendant::div[@class='content']")
CLUB_NAME = (By.XPATH, "./descendant::span[@class='club-name']")
CLUB_COVER = (By.XPATH, ".//header[contains(@class,'page-header')]")



class ClubPage(base_page):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.rating_elements = driver.find_elements(*RATING)

    def get_rating(self):
        return [RatingComponent(web_element) for web_element in self.rating_elements]
