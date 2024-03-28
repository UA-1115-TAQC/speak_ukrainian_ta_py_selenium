from src.ui.components.carousel.carousel_card_component import CarouselCardComponent
from src.ui.pages.home_page.home_page import HomePage
from tests.base_test_runner import BaseTestRunner


class TestHomePageWithoutLogin(BaseTestRunner):

    def setUp(self):
        super().setUp()

    def test_button_all_clubs(self):
        self.homepage.scroll_to_all_clubs_button()
        #carousel_card = CarouselCardComponent(self.driver, self.homepage)
        # carousel_card.click_carousel_card_all_clubs_button()
