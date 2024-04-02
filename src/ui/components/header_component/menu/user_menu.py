from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.add_center_popup_component import AddCenterPopUp
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubPopUp
from src.ui.components.base_component import BaseComponent


class UserMenu(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "add_club": ("xpath", ".//li[contains(@data-menu-id, 'add_club')]"),
            "add_center": ("xpath", ".//li[contains(@data-menu-id, 'add_centre')]"),
            "search_certificates": ("xpath", ".//li[contains(@data-menu-id, 'search_certificates')]"),
            "profile": ("xpath", ".//li[contains(@data-menu-id, 'profile')]"),
            "logout": ("xpath", ".//li[contains(@data-menu-id, 'logout')]"),
            "add_club_popup": ("xpath", "//div[contains(@class,'modal-add-club')]"),
            "add_center_popup": ("xpath", "//div[contains(@class,'addCenter')]")
        }

    @property
    def click_add_club_pop_up(self) -> AddClubPopUp:
        self.add_club.click_button()
        return AddClubPopUp(self.add_club_popup)

    @property
    def click_add_center_pop_up(self) -> AddCenterPopUp:
        self.add_center.click_button()
        return AddCenterPopUp(self.add_center_popup)

    @property
    def click_search_certificate(self) -> 'SearchCertificatePage':
        self.search_certificates.click_button()
        from src.ui.pages.search_certificate.search_certificate_page import SearchCertificatePage
        return SearchCertificatePage(self.driver)

    def click_profile(self):  # TODO (add page and finish method)
        pass

    @property
    def click_logout(self) -> None:
        return self.logout.click_button()
