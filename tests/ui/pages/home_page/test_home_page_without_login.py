from tests.base_test_runner import BaseTestRunner


class TestHomePageWithoutLogin(BaseTestRunner):

    def setUp(self):
        super().setUp()

    def test_button_all_clubs(self):
        self.homepage.scroll_to_all_clubs_button().carousel_card_component.click_carousel_card_all_clubs_button()
        self.assertTrue(self.driver.current_url.__contains__("clubs"), "URL for clubs page are different")

    def test_check_that_slick_dots_container_on_img_carousel_is_centered(self):
        self.assertIn("center",
                      self.homepage.carousel_img_component.slick_dots_container.value_of_css_property("justify-content"))
