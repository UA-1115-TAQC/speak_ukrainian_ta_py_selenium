from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.comments_component import CommentsClubComponent
from src.ui.pages.base_pages.base_page import BasePage
from selenium import webdriver
from src.ui.components.sign_up_to_club_popup.sign_up_to_club import SignUpToClub


class ClubPage(BasePage):

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            "club_rating": ("xpath", "./descendant::div[@class='page-rating']"),
            "sign_up_to_club": (
                "xpath", "//button[contains(@class, 'apply-button')]//span[contains(text(),'Записатись на гурток')]"),
            "write_to_manager": ("xpath", "./descendant::span[text()='Написати менеджеру']"),
            "club_description": ("xpath", "./descendant::div[@class='content']"),
            "club_name": ("xpath", "./descendant::span[@class='club-name']"),
            "club_cover": ("xpath", "/header[contains(@class,'page-header')]"),
            "leave_comment": ("xpath", "./descendant::button[contains(@class,'comment-button')][1]"),
            "sign_up_to_club_pop_up": ("xpath", "//div[contains(@class,'SignUpForClub_signUpForClubModal')]"),
            "submit_button": ("xpath", ".//button[@type='submit']"),
            "add_comment_pop_up": ("xpath", "//div[contains(@class,'comment-modal')]"),
            "comments_component": ("xpath", ".//div[@class='ant-comment-inner']"),
            "category_club_name": ("xpath", "//div[@class='tags ']//span[@class='name']")
        }

        self.wait = WebDriverWait(self.driver, 30)

    @property
    def sign_in_to_club(self) -> SignUpToClub:
        self.sign_up_to_club.click_button()
        self.wait.until(EC.visibility_of_element_located(self.locators["sign_up_to_club_pop_up"]))
        return SignUpToClub(self.sign_up_to_club_pop_up)

    def sign_up_to_club_popup(self) -> SignUpToClub:
        return SignUpToClub(self.sign_up_to_club_pop_up)

    def get_comments_list(self) -> list['CommentsClubComponent']:
        return [CommentsClubComponent(comments) for comments in self.comments_component]

    def get_category_club_text(self) -> str:
        return self.category_club_name.text
