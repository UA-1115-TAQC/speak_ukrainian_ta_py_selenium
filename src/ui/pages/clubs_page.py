from selenium.common import NoSuchElementException
from src.ui.components.center_card_component import CenterCardComponent
from src.ui.components.club_card_component import ClubCardComponent
from src.ui.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from src.ui.components.list_control_component import ListControlComponent
from src.ui.components.pagination_component import PaginationComponent
from src.ui.components.search_sider_component import SearchSiderComponent
from src.ui.pages.base_pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ClubsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "search_clubs_header": ("xpath", "//div[contains(@class, 'lower-header-box')]"),
            "pagination": ("xpath", "//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]"),
            "search_sider": ("xpath", "//div[contains(@class, 'sider')]"),
            "list_control": ("xpath", "//div[contains(@class, 'club-list-control')]"),
            "club_cards": ("xpath", "//div[contains(@class,'content-clubs-list')]/child::div"),
            "center_cards": ("xpath", "//div[contains(@class,'content-center-list')]/child::div"),
        }
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 30)

    @property
    def search_clubs_header(self):
        return AdvancedSearchClubsHeaderComponent(self._driver, self._driver.find_element(*self.locators["search_clubs_header"]))

    @property
    def pagination(self):
        return PaginationComponent(self._driver, self._driver.find_element(*self.locators["pagination"]))

    @property
    def search_sider(self):
        return SearchSiderComponent(self.driver, self._driver.find_element(*self.locators["search_sider"]))

    @property
    def list_control(self):
        return ListControlComponent(self._driver.find_element(*self.locators["list_control"]))

    @property
    def card_list(self):
        if self.search_sider_is_opened() and self.search_sider.checked_radio_button.get_attribute("innerText") == "Центр":
            return self.get_center_card_list()
        else:
            return self.get_club_card_list()

    def get_club_card_list(self):
        club_card_list = []
        club_elements_list = self._driver.find_elements(*self.locators["club_cards"])
        for club in club_elements_list:
            club_card_list.append(ClubCardComponent(self._driver, club))
        return club_card_list

    def get_center_card_list(self):
        center_card_list = []
        center_elements_list = self._driver.find_elements(*self.locators["center_cards"])
        for center in center_elements_list:
            center_card_list.append(CenterCardComponent(center))
        return center_card_list

    def search_sider_is_opened(self):
        try:
            self._driver.find_element(*self.locators["search_sider"])
        except NoSuchElementException:
            return False
        return True

    def is_card_list_empty(self):
        return len(self.card_list) == 0

    def wait_until_clubs_page_is_loaded(self, timeout=30):
        self._wait.until(ec.url_contains("clubs"))
        self._wait.until(ec.visibility_of(self.search_clubs_header.show_on_map_button))

    def wait_until_sidebar_is_loaded(self, timeout=30):
        self._wait.until(lambda wd: self.search_sider_is_opened())
