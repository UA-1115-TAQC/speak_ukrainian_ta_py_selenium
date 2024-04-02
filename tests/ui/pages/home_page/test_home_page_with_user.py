from src.ui.pages.clubs_page import ClubsPage
from src.ui.pages.home_page.home_page import HomePage
from tests.base_test_runner import LogInWithUserTestRunner, BaseTestRunner
import time


# TODO
# class TestHomePageUserLogin(LogInWithUserTestRunner):
class TestHomePageUserLogin(BaseTestRunner):

    def test_right_arrow_get_direction_card_button(self):
        self.homepage.carousel_card_component.click_right_arrow_button()
        time.sleep(240)

        self.homepage = HomePage(self.driver)
        card = self.homepage.carousel_card_component.carousel_cards[3]
        # card = self.homepage.carousel_card_component.get_active_carousel_card_by_index(0)

        # card.wait_till_button_is_active()
        print(card.is_active_by_class())
        direction_name = card.club_card_heading.text
        print("name: " + direction_name)
        button = card.club_card_button.text
        print("button: " + button + "\n")


    # TUA-863
    def test_direction_carousel_clickable_block_and_button(self):
        self.homepage.scroll_to_carousel_card_component_web_element()
        cards_num = len(self.homepage.carousel_card_component.carousel_cards)
        for index in range(cards_num):
            self.homepage = HomePage(self.driver)
            card = self.get_direction_card(index)
            direction_name = card.club_card_heading.text
            card.click_card()
            clubs_page = ClubsPage(self.driver)
            print(clubs_page.search_sider.is_direction_checked(direction_name))
            self.get_back_to_home_page()

            time.sleep(20)

            card = self.homepage.carousel_card_component.carousel_cards[index]
            direction_name = card.club_card_heading.text
            card.click_club_card_button()
            clubs_page = ClubsPage(self.driver)
            print(clubs_page.search_sider.is_direction_checked(direction_name))
            self.homepage = self.get_back_to_home_page()

            time.sleep(20)

    def get_back_to_home_page(self):
        self.driver.back()
        self.homepage.wait_until_home_page_is_loaded()
        self.homepage.wait_until_home_page_is_visible()
        return HomePage(self.driver)

    def get_direction_card(self, index):
        carousel = self.homepage.carousel_card_component
        while not carousel.check_that_the_club_direction_card_obtained_by_index_is_active(index):
            carousel = self.homepage.carousel_card_component.click_right_arrow_button()

            time.sleep(20)

            self.homepage = HomePage(self.driver)
        return self.homepage.carousel_card_component.carousel_cards[index]
