from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.ui.components.base_component import BaseComponent
from src.ui.pages.admin_generate_certificate_page import AdminGenerateCertificatePage


class CertificatesSubmenuPopup(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "generate_certificate": ("xpath", "//li[contains(@data-menu-id, 'generate_certificate')]"),
        }

    def click_generate_certificate(self) -> AdminGenerateCertificatePage:
        self.click_element(self.generate_certificate)
        admin_generate_certificate_page = AdminGenerateCertificatePage(self.driver)
        self.get_wait(40).until(EC.visibility_of(admin_generate_certificate_page.study_duration_label))
        return admin_generate_certificate_page
