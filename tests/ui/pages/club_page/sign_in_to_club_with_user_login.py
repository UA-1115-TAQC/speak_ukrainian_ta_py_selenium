from tests.base_test_runner import LogInWithUserTestRunner
from src.ui.components.header_component.advanced_search_header import AdvancedSearchHeaderComponent
from src.ui.pages.club_page import ClubPage


class SignInToClubTest(LogInWithUserTestRunner):
    CATEGORY_NAME = "хореографія"

    def setUp(self):
        super().setUp()

    def test_sign_in_to_club(self):
        self.homepage.advanced_search_header.set_text_selection_search_input_field(self.CATEGORY_NAME)
        self.clubs_page = self.advanced_search_header.click_search_icon()
