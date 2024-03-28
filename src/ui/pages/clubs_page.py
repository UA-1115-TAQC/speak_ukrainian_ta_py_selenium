from selenium.common import NoSuchElementException
from src.ui.components.center_card_component import CenterCardComponent
from src.ui.components.club_card_component import ClubCardComponent
from src.ui.components.header_component.advanced_search_header import AdvancedSearchClubsHeaderComponent
from src.ui.components.list_control_component import ListControlComponent
from src.ui.components.pagination_component import PaginationComponent
from src.ui.components.search_sider_component import SearchSiderComponent
from src.ui.pages.base_pages.base_page import BasePage
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

    # TODO
    @property
    def search_clubs_header(self):
        # return AdvancedSearchClubsHeaderComponent(self.driver, self.search_clubs_header)
        return AdvancedSearchClubsHeaderComponent(self.driver, self.driver.find_element(*self.locators["search_clubs_header"]))

    # TODO
    @property
    def pagination(self):
        if self.is_element_present("pagination"):
            # return PaginationComponent(self.pagination)
            return PaginationComponent(self.driver.find_element(*self.locators["pagination"]))
        return None

    # TODO
    @property
    def search_sider(self):
        if self.is_element_present("search_sider"):
            return SearchSiderComponent(self.driver.find_element(*self.locators["search_sider"]))
        return None

    # TODO
    @property
    def list_control(self):
        if self.is_element_present("list_control"):
            return ListControlComponent(self.driver.find_element(*self.locators["list_control"]))
        return None

    @property
    def card_list(self):
        if self.is_element_present("search_sider") and self.search_sider.checked_radio_button.get_attribute("innerText") == "Центр":
            return self.get_center_card_list()
        else:
            return self.get_club_card_list()

    def get_club_card_list(self):
        if self.is_element_present("club_cards"):
            club_elements_list = self.driver.find_elements(*self.locators["club_cards"])
            return [ClubCardComponent(club) for club in club_elements_list]
        return []

    def get_center_card_list(self):
        if self.is_element_present("center_cards"):
            center_elements_list = self.driver.find_elements(*self.locators["center_cards"])
            return [CenterCardComponent(center) for center in center_elements_list]
        return []

    def is_element_present(self, element_name):
        try:
            self.driver.find_element(*self.locators[element_name])
        except NoSuchElementException:
            return False
        return True

    def is_card_list_empty(self):
        return len(self.card_list) == 0

    def wait_until_clubs_page_is_loaded(self):
        self.get_wait(30).until(ec.url_contains("clubs"))
        self.get_wait(30).until(ec.visibility_of(self.search_clubs_header.show_on_map_button))

    def wait_until_sidebar_is_loaded(self):
        self.get_wait(30).until(lambda wd: self.is_element_present("search_sider"))
