from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import BaseTestRunner


class SearchFieldTest(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self._clubs_page = self.homepage.header.click_clubs_button()

    # TUA-825
    def test_clubs_change_with_entered_character(self):
        text = ["С", "п", "о", "р", "т"]
        self.assertTrue(self.is_text_present_on_cards(text))

    def is_text_present_on_cards(self, text):
        for c in text:
            self._clubs_page.search_clubs_header.set_text_selection_search_input_field(c)
            search_str = self._clubs_page.search_clubs_header.get_text_selection_search_input_field()
            self._clubs_page = ClubsPage(self.driver)
            if not self.check_text_on_cards(search_str):
                return False
        return True

    def check_text_on_cards(self, search):
        clubs = self._clubs_page.card_list
        for club in clubs:
            if club.name_contains(search) or club.direction_contains(search) or club.description_contains(search):
                continue
            popup = club.click_title()
            if not popup.directions_contains(search):
                return False
            popup.click_close_button()
        return True
