from selenium import webdriver

from src.ui.pages.base_pages.base_page import BasePage


class SearchCertificatePage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "search_certificate_title": ("xpath", "./descendant::div[@class='certificateSearchContent']/h3"),
            "result_searching_title": ("xpath", "./descendant::div[@class='certificateSearchContent']/h2"),
            "search_input_placeholder": ("xpath", "./descendant::div[@class='searchCertificateUser']"
                                                  "//input[@type='text']"),
            "search_icon": ("xpath", "./descendant::span[(@role='img') and (@aria-label='search')]"),
            "search_button": ("xpath", "./descendant::button[contains(@class, 'search-button')]"),
            "clear_searching_text_button": ("xpath", "./descendant::span[@class='ant-input-clear-icon']")
        }

    def search_certificate_title_text(self) -> str:
        return self.search_certificate_title.text

    def get_search_input_value(self) -> str:
        return self.search_input_placeholder.text

    def set_search_input_value(self, search_text: str) -> None:
        self.search_input_placeholder.visibility_of_element_located().send_keys(search_text)

    def clear_search_input(self) -> None:
        self.clear_searching_text_button.click_button()

    def search_certificate(self):  # TODO (functional of website don't show result of searching)
        return self.search_button.click_button()
