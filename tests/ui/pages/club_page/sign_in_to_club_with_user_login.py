from src.ui.pages.club_page import ClubPage
from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import LogInWithUserTestRunner


class SignInToClubTest(LogInWithUserTestRunner):
    CATEGORY_NAME = "хореографія"
    FIRST_NAME = "Володимир"
    LAST_NAME = "Івахненко"
    AGE = "12"
    SUCCESS_REGISTRATION = "Запит на реєстрацію в гурток надіслано"
    COMMENT = "Зателефонуйте - маю питання"

    def setUp(self):
        super().setUp()
        self.homepage.get_advanced_search_header_component().set_text_selection_search_input_field(self.CATEGORY_NAME)
        self.homepage.get_advanced_search_header_component().click_search_icon()
        self.clubs_page = ClubsPage(self.driver)
        self.clubs_page.get_club_card_list()[0].click_details_button()

    def test_sign_up_child_to_club(self):
        self.club_page = ClubPage(self.driver)
        sign_in_popup = self.club_page.sign_in_to_club
        sign_in_popup.click_child_checkbox_by_index(0)
        sign_in_popup.set_comment(self.COMMENT)
        sign_in_popup.click_submit_button()

        self.assertIn(self.homepage.get_top_notice_message(), self.SUCCESS_REGISTRATION,
                      "After registration popup with the following text should appear " + self.SUCCESS_REGISTRATION)

    def test_add_child_to_list_for_sign_up_to_club(self):
        self.club_page = ClubPage(self.driver)
        add_child = self.club_page.sign_in_to_club.click_add_children()
        add_child.set_first_name(self.FIRST_NAME)
        add_child.set_last_name(self.LAST_NAME)
        add_child.set_age(self.AGE)
        add_child.click_male_gender()
        add_child.click_submit_button()
        children_list = self.club_page.sign_up_to_club_popup().get_children_list_names()

        full_name = f"{self.FIRST_NAME} {self.LAST_NAME}, {self.AGE}"

        self.assertTrue(full_name in children_list, "Full name of added child should be on a list")
