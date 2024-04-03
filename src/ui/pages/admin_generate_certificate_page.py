
from src.ui.pages.base_pages.base_page_without_header_and_footer import BasePageWithoutHeaderAndFooter


class AdminGenerateCertificatePage(BasePageWithoutHeaderAndFooter):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "study_duration_label": ("xpath", "//label[@for=\"basic_hours\"]"),
            "study_duration_input": ("xpath", "//input[@name=\"hours\"]"),
        }