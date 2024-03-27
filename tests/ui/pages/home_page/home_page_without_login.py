from src.ui.pages.home_page.home_page import HomePage
from tests.base_test_runner import BaseTestRunner


class TestHomePageWithoutLogin(BaseTestRunner):

    def setUp(self):
        super().setUp()

    def test_button_all_clubs(self):
        self.homepage.scroll_to_all_clubs_button()

