from src.ui.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.ui.components.rating_component import RatingComponent


RATING = (By.XPATH, "./descendant::ul[@role='radiogroup']")


class ClubPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.rating_elements = driver.find_elements(*RATING)

    def get_rating(self):
        return [RatingComponent(web_element) for web_element in self.rating_elements]
