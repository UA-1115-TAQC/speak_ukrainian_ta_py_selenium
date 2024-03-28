import unittest
from selenium import webdriver
from src.ui.pages.home_page.home_page import HomePage
from tests.utils.credentials import Credentials


class BaseTestRunner(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(Credentials.get_url())
        self.driver.maximize_window()
        self.homepage = HomePage(self.driver)

    def login(self, email: str, password: str):
        login = self.homepage.header.click_profile_button().open_login_form()
        login.enter_email(email)
        login.enter_password(password)
        login.click_submit_button()

    def tearDown(self) -> None:
        self.driver.quit()


class LogInWithAdminTestRunner(BaseTestRunner):
    def setUp(self):
        super().setUp()
        self.login(Credentials.get_admin_email(), Credentials.get_admin_password())


class LogInWithManagerTestRunner(BaseTestRunner):
    def setUp(self):
        super().setUp()
        self.login(Credentials.get_manager_email(), Credentials.get_manager_password())


class LogInWithUserTestRunner(BaseTestRunner):
    def setUp(self):
        super().setUp()
        self.login(Credentials.get_user_email(), Credentials.get_user_password())


if __name__ == "__main__":
    unittest.main()
