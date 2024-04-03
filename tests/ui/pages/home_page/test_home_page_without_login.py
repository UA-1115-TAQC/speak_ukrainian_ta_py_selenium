from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.ui.pages.clubs_page import ClubsPage
from tests.base_test_runner import BaseTestRunner
from tests.utils.credentials import Credentials

class TestHomePageWithoutLogin(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self.clubs_page = None

    def test_button_all_clubs(self):
        self.homepage.scroll_to_all_clubs_button().carousel_card_component.click_carousel_card_all_clubs_button()
        self.assertTrue(self.driver.current_url.__contains__("clubs"), "URL for clubs page are different")

    def test_check_that_slick_dots_container_on_img_carousel_is_centered(self):
        self.assertIn("center",
                      self.homepage.carousel_img_component.slick_dots_container.value_of_css_property("justify-content"))

    #TUA-44
    #Verify that user can perform basic search by whole words
    def test_basic_search_in_advanced_search_header(self):
        self.check_that_user_can_do_basic_search_by_string("American Gymnastics Club")
        self.check_that_user_can_do_basic_search_by_string("Сфера")
        # +Check the search result with DB #todo

    def check_that_user_can_do_basic_search_by_string(self, string):
        string = string.strip().lower()
        self.homepage.advanced_search_header_component.set_text_selection_search_input_field(string)
        self.clubs_page = ClubsPage(self.driver)
        self.clubs_page.wait_until_clubs_page_is_loaded()
        for card in self.clubs_page.get_club_card_list():
            for tag in card.direction_list:
                self.assertTrue(string in card.get_name_text().strip().lower() or
                                             string in card.description.text.strip().lower() or
                                             string in tag.name.text.strip().lower(),
                                             "The title of the shown card " + card.get_name_text() +
                                             " or the description " + card.description.text +
                                             " or the tags" + str(card.direction_list) +
                                             " doesn't contain the search query " + string)
        # +Check the search result with DB #todo
        self.old_url = self.driver.current_url
        self.driver.get(Credentials.get_url())
        WebDriverWait(self.driver, 10).until(EC.url_changes(self.old_url))

