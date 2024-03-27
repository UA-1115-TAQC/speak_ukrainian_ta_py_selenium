from tests.base_test_runner import BaseTestRunner


class FooterComponentTest(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self.homepage = self.homepage.scroll_to_footer()
        self.homepage.wait_until_home_page_is_loaded()

    def test_check_UI_across_different_mobile(self):
        sizes = [(320, 667), (414, 896), (425, 915)]
        for width, height in sizes:
            self.driver.set_window_size(width, height)
            self.check_footer_elements()
            self.check_text_size_and_color_all_elements()

    def check_footer_elements(self):
        social_links_number = 3
        sponsor_links_number = 7
        footer = self.homepage.footer
        self.assertTrue(footer.logo.is_displayed())
        self.assertTrue(footer.motto_under_logo.is_displayed())
        self.assertEqual(social_links_number, len(footer.get_social_links()), "Number of social links is not equal to 3")
        self.assertTrue(footer.copyright_text.is_displayed())
        self.assertTrue(footer.sponsors_title.is_displayed())
        self.assertEqual(sponsor_links_number, len(footer.get_sponsors_links()), "Number of sponsors links is not equal to 7")
        self.assertTrue(footer.donate_title.is_displayed())
        self.assertTrue(footer.donate_explanation.is_displayed())
        self.assertTrue(footer.donate_button.is_displayed())

    def check_text_size_and_color_all_elements(self):
        footer = self.homepage.footer
        self.assertEqual("Наші партнери", footer.sponsors_title.text,
                         "Title for sponsors block mismatch in")
        self.assertEqual("rgba(45, 76, 104, 1)", footer.sponsors_title.value_of_css_property("color"),
                         "Colors are different for sponsors title")
        self.assertEqual("24px", footer.sponsors_title.value_of_css_property("font-size"),
                         "Font-size are different for sponsors title")

        self.assertEqual("Як допомогти проєкту?", footer.donate_title.text,
                         "Title for donate block mismatch in")
        self.assertEqual("rgba(45, 76, 104, 1)", footer.donate_title.value_of_css_property("color"),
                         "Colors are different for donate title")
        self.assertEqual("24px", footer.donate_title.value_of_css_property("font-size"),
                         "Font-size are different for donate title")

        self.assertEqual("Ініціатива потребує постійної фінансової підтримки, аби покривати щоденні витрати на роботу.",
                         footer.donate_explanation.text, "Explanation for donate mismatch in")
        self.assertEqual("rgba(45, 76, 104, 1)", footer.donate_explanation.value_of_css_property("color"),
                         "Colors are different for donate explanation")
        self.assertEqual("12px", footer.donate_explanation.value_of_css_property("font-size"),
                         "Font-size are different for donate explanation")

        self.assertEqual("Допомогти проєкту", footer.donate_button.text,
                         "Button for donate mismatch in")
        self.assertEqual("rgba(255, 255, 255, 1)", footer.donate_button.value_of_css_property("color"),
                         "Colors are different for donate button")
