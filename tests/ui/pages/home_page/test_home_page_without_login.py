from tests.base_test_runner import BaseTestRunner
from src.ui.pages.clubs_page import ClubsPage
from src.ui.pages.home_page.home_page import HomePage
from tests.base_test_runner import BaseTestRunner, LogInWithUserTestRunner
import time


class TestHomePageWithoutLogin(BaseTestRunner):

    def setUp(self):
        super().setUp()

    def test_button_all_clubs(self):
        self.homepage.scroll_to_all_clubs_button().carousel_card_component.click_carousel_card_all_clubs_button()
        self.assertTrue(self.driver.current_url.__contains__("clubs"), "URL for clubs page are different")
