from src.ui.pages.base_pages.base_page import BasePage
from selenium import webdriver
from src.ui.components.sign_up_to_club_popup.sign_up_to_club import SignUpToClub


class ClubPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "club_rating": ("xpath", "./descendant::div[@class='page-rating']"),
            "sign_up_to_club": ("xpath", "./descendant::span[text()='Записатись на гурток']"),
            "write_to_manager": ("xpath", "./descendant::span[text()='Написати менеджеру']"),
            "club_description": ("xpath", "./descendant::div[@class='content']"),
            "club_name": ("xpath", "./descendant::span[@class='club-name']"),
            "club_cover": ("xpath", "/header[contains(@class,'page-header')]"),
            "leave_comment": ("xpath", "./descendant::button[contains(@class,'comment-button')][1]"),
            "sign_up_to_club_pop_up": ("xpath", ".//div[contains(@class,'SignUpForClub_signUpForClubModal')]"),
            "submit_button": ("xpath", ".//button[@type='submit']")
        }

    @property
    def sign_in_to_club(self) -> SignUpToClub:
        self.sign_up_to_club.click_button()
        return SignUpToClub(self.sign_up_to_club_pop_up)
