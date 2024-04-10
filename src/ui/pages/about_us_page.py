from src.ui.pages.base_pages.base_page_with_advanced_search import BasePageWithAdvancedSearch


class AboutUsPage(BasePageWithAdvancedSearch):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            **self.locators,
            "banner": ("xpath", ".//div[@class='title']"),
            "help_project_button": ("xpath", ".//div[@class ='social-info']/descendant::button"),
            "social_info": ("xpath", ".//div[@class='social-info']/div[@class='social-media']"),
        }
