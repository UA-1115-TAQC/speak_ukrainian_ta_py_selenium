from src.ui.pages.club_page import ClubPage
from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import LogInWithUserTestRunner


class SignInToClubTest(LogInWithUserTestRunner):
    CATEGORY_NAME = "хореографія"

    def setUp(self):
        super().setUp()

    def test_sign_in_to_club(self):
        self.homepage.get_advanced_search_header_component().set_text_selection_search_input_field(self.CATEGORY_NAME)
        self.homepage.get_advanced_search_header_component().click_search_icon()
        self._clubs_page = ClubsPage(self.driver)
        self._clubs_page.center_card_list[0].click_details_button()
        self.club_page = ClubPage(self.driver)
        self.club_page.sign_in_to_club.click_add_children()



