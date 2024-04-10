from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch


class ServicePage(BasePageWithAdvancedSearch):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "banner": ("xpath", ".//div[@class='title']"),
            "help_project_button": ("xpath", ".//div[@class ='social-info']/descendant::button"),
            "social_info": ("xpath", ".//div[@class='social-info']/div[@class='social-media']"),
            "content_title": ("xpath", ".//div[@class ='content-title']"),
            "content_text": ("xpath", ".//div[@class ='content-text']"),
            "faq_title": ("xpath", ".//div[@class ='faq-title']"),
            "collapse_element_list": ("xpath", ".//div[contains(@class,'ant-collapse-icon-position-start')]"),
        }
