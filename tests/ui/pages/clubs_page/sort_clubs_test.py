# TUA-239
from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import BaseTestRunner


class AddClubPopUpWithAdminTest(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self.homepage.get_advanced_search_header_component.click_advanced_search_icon()
        self._clubs_page = ClubsPage(self.driver)

    def test_sort_clubs_alphabetically_ascending(self):
        club_name_list = self.get_club_name_list()
        sorted_list = sorted(club_name_list)
        self.assertListEqual(club_name_list, sorted_list)

    def test_sort_clubs_alphabetically_descending(self):
        self._clubs_page.list_control.click_arrow_up()
        club_name_list = self.get_club_name_list()
        sorted_list = sorted(club_name_list.sort, reverse=True)
        self.assertListEqual(club_name_list, sorted_list)

    def get_club_name_list(self):
        names = []
        while True:
            self._clubs_page = ClubsPage(self.driver)
            cards = self._clubs_page.card_list
            for card in cards:
                names.append(card.get_name_text())
            pagination = self._clubs_page.pagination
            if not pagination or pagination.is_next_disabled():
                break
            pagination.click_next()
        return names
