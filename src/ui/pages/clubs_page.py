from src.ui.pages.base_pages.base_page import BasePage


class ClubsPage(BasePage):
    def __init__(self, driver):
        super().__init__()
        self._driver = driver

    def wait_until_clubs_page_is_loaded(self, timeout=30):
        #WebDriverWait(self._driver, timeout).until() //todo - add clubspage wait
        pass