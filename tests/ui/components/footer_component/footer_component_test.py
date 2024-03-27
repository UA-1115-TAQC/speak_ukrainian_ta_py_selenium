from tests.base_test_runner import BaseTestRunner
from selenium.webdriver import Chrome, ChromeOptions


class FooterComponentTest(BaseTestRunner):

    def setUp(self):
        super().setUp()
        self.homepage = self.homepage.scroll_to_footer()

    def test_check_UI_across_different_mobile(self):
        # opts = ChromeOptions()
        # opts.add_argument("--window-size = 320, 667")
        # driver = Chrome(options=opts)
        footer = self.homepage.footer
       # self.assertEqual("Наші партнери", footer.get_sponsors_title_text,  "Title mismatch in")
        self.assertEqual(footer.get_sponsors_title_attribute("color"),
                         "rgba(45, 76, 104, 1)",
                         "Colors are different")
