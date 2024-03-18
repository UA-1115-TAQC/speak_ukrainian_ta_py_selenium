from src.ui.pages.base_page import BasePage
from selenium import webdriver
from src.ui.components.rating_component import RatingComponent
from selenium.webdriver.common.by import By

RATING = (By.XPATH, "./descendant::ul[@role='radiogroup']")

class ClubPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)



