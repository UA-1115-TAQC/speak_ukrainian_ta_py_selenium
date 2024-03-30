from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubPopUp
from src.ui.components.base_component import BaseComponent
from src.ui.components.header_component.menu.guest_menu import GuestMenu
from src.ui.components.header_component.menu.user_menu import UserMenu


class HeaderComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "add_club_button": ("xpath", ".//button[contains(@class,'add-club-button')]"),
            "add_club_popup": ("xpath", "//div[contains(@class,'modal-add-club')]"),
            "profile_menu_button": ("xpath", ".//div[contains(@class, 'user-profile')]"),
            "profile_menu_node": ("xpath", "//ul[contains(@class, 'ant-dropdown-menu')]")
        }

    def add_club_click(self) -> AddClubPopUp:
        self.add_club_button.click_button()
        return AddClubPopUp(self.add_club_popup)

    def click_profile_button(self) -> GuestMenu:
        self.profile_menu_button.click()
        return GuestMenu(self.profile_menu_node)

    def open_user_menu(self) -> UserMenu:
        self.profile_menu_button.click()
        return UserMenu(self.profile_menu_node)
