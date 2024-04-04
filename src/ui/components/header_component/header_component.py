from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubPopUp
from src.ui.components.base_component import BaseComponent
from src.ui.components.header_component.menu.guest_menu import GuestMenu
from src.ui.components.header_component.menu.user_menu import UserMenu, AdminMenu


class HeaderComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "add_club_button": ("xpath", ".//button[contains(@class,'add-club-button')]"),
            "add_club_popup": ("xpath", "//div[contains(@class,'modal-add-club')]"),
            "profile_menu_button": ("xpath", ".//div[contains(@class, 'user-profile')]"),
            "profile_menu_node": ("xpath", "//ul[contains(@class, 'ant-dropdown-menu')]"),
            "clubs_button": ("xpath", ".//a[contains(@href,'clubs')]"),
            "news_button": ("xpath", "//a[contains(@href, '/news')]"),
            "teach_in_ukr_logo": ("xpath", "//div[contains(@class, 'logo')]"),
            "challenge_button": ("xpath", "//span[contains(@class, 'challenge-text')]"),
            "challenge_dropdown_node": ("xpath", "//ul[contains(@id,'challenge_ONE-popup')]"),
            "about_us_button": ("xpath", ".//a[contains(@href,'about')]"),
            "service_page_button": ("xpath", ".//a[contains(@href,'service')]"),
        }

    def add_club_click(self) -> AddClubPopUp:
        self.add_club_button.click_button()
        return AddClubPopUp(self.add_club_popup)

    def click_profile_button(self) -> GuestMenu:
        self.profile_menu_button.click()
        return GuestMenu(self.profile_menu_node)

    def click_teach_in_ukr_logo(self):
        self.teach_in_ukr_logo.click_button()
        from src.ui.pages.home_page.home_page import HomePage
        return HomePage(self.driver)

    def click_clubs_button(self):
        from src.ui.pages.clubs_page import ClubsPage
        self.clubs_button.click_button()
        return ClubsPage(self.driver)

    def click_about_us_button(self):
        self.about_us_button.click_button()
        from src.ui.pages.about_us_page import AboutUsPage
        return AboutUsPage(self.driver)

    def click_service_page_button(self):
        self.service_page_button.click_button()
        from src.ui.pages.service_page import ServicePage
        return ServicePage(self.driver)

    def click_news_button(self) -> 'AllNewsPage':
        self.news_button.click_button()
        from ...pages.all_news_page import AllNewsPage
        return AllNewsPage(self.driver)

    def click_challenge_button(self):
        self.challenge_button.click_button()
        return HeaderChallengesDropdown(self.challenge_dropdown_node)

    def open_user_menu(self) -> UserMenu:
        self.profile_menu_button.click()
        return UserMenu(self.profile_menu_node)

    def open_admin_menu(self) -> AdminMenu:
        self.click_profile_button()
        return AdminMenu(self.profile_menu_node)


class HeaderChallengesDropdown(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "challenge_button": ("xpath", "//span[contains(@class, 'challenge-text')]"),
            "dropdown_items": ("xpath", ".//li[@role='menuitem']//a"),
        }

    @property
    def dropdown_items(self):
        return self.node.find_elements(*self.locators["dropdown_items"])

    def click_item_by_index(self, index):
        self.challenge_button.click_button()
        self.dropdown_items[index].click()
        from src.ui.pages.challenge_pages.base_challenge_page import BaseChallengePage
        return BaseChallengePage(self.driver)

