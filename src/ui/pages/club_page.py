from src.ui.pages.base_pages.base_page import BasePage
from selenium import webdriver
from src.ui.components.sign_in_to_club_component.sign_up_to_club_pop_up_component import SignUpToClubPopUpComponent


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
        }

    def click_on_sign_up_to_club_button(self) -> SignUpToClubPopUpComponent:
        self.sign_up_to_club.click_button()
        return SignUpToClubPopUpComponent(self.node)


