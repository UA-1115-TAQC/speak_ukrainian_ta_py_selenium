from selenium.common import NoSuchElementException
from src.ui.components.center_card_component import CenterCardComponent
from src.ui.components.club_card_component import ClubCardComponent
from src.ui.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from src.ui.components.list_control_component import ListControlComponent
from src.ui.components.pagination_component import PaginationComponent
from src.ui.components.search_sider_component import SearchSiderComponent
from src.ui.pages.base_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SEARCH_CLUBS_HEADER_WEB_ELEMENT = (By.XPATH, "//div[contains(@class, 'lower-header-box')]")
PAGINATION_WEB_ELEMENT = (By.XPATH, "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]")
SEARCH_SIDER_WEB_ELEMENT = (By.XPATH, "//div[contains(@class, 'sider')]")
LIST_CONTROL_WEB_ELEMENT = (By.XPATH, "//div[contains(@class, 'club-list-control')]")
CLUBS_CARD_WEB_ELEMENT = (By.XPATH, "//div[contains(@class,'content-clubs-list')]/child::div")
CENTER_CARD_WEB_ELEMENT = (By.XPATH, "//div[contains(@class,'content-center-list')]/child::div")


class ClubsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self.driver, 10)
        self._search_clubs_header = None
        self._pagination = None
        self._search_sider = None
        self._list_control = None
        self._club_card_list = None
        self._center_card_list = None
        self.select_what_cards_to_show()

    @property
    def search_clubs_header(self):
        if not self._search_clubs_header:
            self._search_clubs_header = AdvancedSearchClubsHeaderComponent(self.driver, self.driver.find_element(*SEARCH_CLUBS_HEADER_WEB_ELEMENT))
        return self._search_clubs_header

    @property
    def pagination(self):
        if not self._pagination:
            self._pagination = PaginationComponent(self.driver, self.driver.find_element(*PAGINATION_WEB_ELEMENT))
        return self._pagination

    @property
    def search_sider(self):
        if not self._search_sider:
            self._search_sider = SearchSiderComponent(self.driver, self.driver.find_element(*SEARCH_SIDER_WEB_ELEMENT))
        return self._search_sider

    @property
    def list_control(self):
        if not self._list_control:
            self._list_control = ListControlComponent(self.driver.find_element(*LIST_CONTROL_WEB_ELEMENT))
        return self._list_control

    @property
    def club_card_list(self):
        if not self._club_card_list:
            self._club_card_list = []
            club_elements_list = self.driver.find_elements(*CLUBS_CARD_WEB_ELEMENT)
            for club in club_elements_list:
                self._club_card_list.append(ClubCardComponent(self.driver, club))
        return self._club_card_list

    @property
    def center_card_list(self):
        if not self._center_card_list:
            self._center_card_list = []
            center_elements_list = self.driver.find_elements(*CENTER_CARD_WEB_ELEMENT)
            for center in center_elements_list:
                self._center_card_list.append(CenterCardComponent(center))
        return self._center_card_list

    def select_what_cards_to_show(self):
        if self.search_sider_is_opened() and self.search_sider.checked_radio_button.get_attribute("innerText") == "Центр":
            self.center_card_list
        else:
            self.club_card_list

    def search_sider_is_opened(self):
        try:
            self.driver.find_element(*SEARCH_SIDER_WEB_ELEMENT)
        except NoSuchElementException:
            return False
        return True

    def wait_until_clubs_page_is_loaded(self, timeout=30):
        self._wait.until(ec.url_contains("clubs"))
        self._wait.until(ec.visibility_of(self.search_clubs_header.show_on_map_button))

    def wait_until_sidebar_is_loaded(self, timeout=30):
        self._wait.until(lambda wd: self.search_sider_is_opened())
