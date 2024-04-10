import time

from src.ui.pages.profile_page import ProfilePage
from tests.base_test_runner import LogInWithUserTestRunner


class TestProfilePage(LogInWithUserTestRunner):
    def setUp(self):
        super().setUp()
        self.profile_page = ProfilePage(self.driver)
        self.homepage.header.click_profile_button()
        self.homepage.header.click_personal_cabinet_button()

    def test_is_all_elements_displayed(self):
        self.assertEqual(self.profile_page.my_profile_title.text, "Мій профіль")
        self.assertTrue(self.profile_page.user_name.is_displayed())
        self.assertTrue(self.profile_page.user_avatar.is_displayed())
        self.assertTrue(self.profile_page.user_role.is_displayed())
        self.assertTrue(self.profile_page.user_phone.is_displayed())
        self.assertTrue(self.profile_page.user_email.is_displayed())
        self.assertTrue(self.profile_page.edit_profile_button.is_displayed())
        self.assertTrue(self.profile_page.my_lessons_or_centers_dropdown.is_displayed())
        self.assertTrue(self.profile_page.add_button.is_displayed())
        self.profile_page.click_add_button()
        self.assertTrue(self.profile_page.add_club_button.is_displayed())
        self.assertTrue(self.profile_page.add_center_button.is_displayed())

    def test_add_button(self):
        self.assertEqual("Додати", self.profile_page.add_button.text)
        self.assertEqual("rgba(250, 140, 22, 1)", self.profile_page.add_button.value_of_css_property("background-color"))
