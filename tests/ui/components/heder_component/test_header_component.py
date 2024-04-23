from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as ec


class TestHeaderComponent(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self.header = self.homepage.header

    # TUA-972
    def test_lower_part_of_header_on_pages(self):
        clubs_page = self.header.click_clubs_button()
        self.assertTrue(clubs_page.search_clubs_header.node.is_displayed())
        self.header = clubs_page.header

        dropdown_item_num = len(self.header.click_challenge_button().dropdown_items)
        for index in range(dropdown_item_num):
            challenge_page = self.header.click_challenge_button().click_item_by_index(index)
            self.assertTrue(challenge_page.advanced_search_header_component.node.is_displayed())
            self.header = challenge_page.header

        all_news_page = self.header.click_news_button()
        self.assertTrue(all_news_page.advanced_search_header_component.node.is_displayed())
        self.header = all_news_page.header

        about_us_page = self.header.click_about_us_button()
        self.assertTrue(about_us_page.advanced_search_header_component.node.is_displayed())
        self.header = about_us_page.header

        service_page = self.header.click_service_page_button()
        self.assertTrue(service_page.advanced_search_header_component.node.is_displayed())
        self.header = service_page.header

        home_page = self.header.click_teach_in_ukr_logo()
        self.assertTrue(home_page.advanced_search_header_component.node.is_displayed())
        self.header = home_page.header

    # TUA-851
    # Verify that the search for clubs is conducted within the selected city
    def test_search_clubs_is_conducted_to_selected_city(self):
        self.homepage.advanced_search_header_component.set_text_selection_search_input_field("Спортивні секції")
        clubs_page = ClubsPage(self.driver)
        club_cards = clubs_page.get_club_card_list()
        for card in club_cards:
            self.assertTrue(card.address_contains("Київ"))

        self.header.select_city_by_name("Харків")

        WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element((By.TAG_NAME, "body"), "Харків, ")
        )

        clubs_page = ClubsPage(self.driver)
        club_cards = clubs_page.get_club_card_list()
        for card in club_cards:
            self.assertTrue(card.address_contains("Харків"))