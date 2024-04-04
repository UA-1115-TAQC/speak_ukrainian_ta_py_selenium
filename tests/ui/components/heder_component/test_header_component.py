from tests.base_test_runner import BaseTestRunner


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

        home_page = self.header.click_teach_in_ukr_logo()
        self.assertTrue(home_page.advanced_search_header_component.node.is_displayed())
        self.header = home_page.header
