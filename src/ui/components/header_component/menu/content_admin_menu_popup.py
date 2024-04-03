from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent
from src.ui.components.header_component.menu.certificates_submenu_popup import CertificatesSubmenuPopup


class ContentAdminMenuPopup(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "certificates_submenu_popup": ("xpath", "//div[contains(@aria-controls, 'certificates-popup')]"),
            "challenges_submenu_popup": ("xpath", "//div[contains(@aria-controls, 'challenges-submenu-popup')]"),
        }

    def open_certificates_submenu_popup(self) -> CertificatesSubmenuPopup:
        self.click_element(self.certificates_submenu_popup)
        return CertificatesSubmenuPopup(self.challenges_submenu_popup)
