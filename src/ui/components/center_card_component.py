from src.ui.components.base_component import BaseComponent


class CenterCardComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "title": ("xpath", ".//div[contains(@class,'center-title')]"),
            "description": ("xpath", ".//p[contains(@class,'center-description-in-block')]"),
            "rating": ("xpath", ".//ul[contains(@class,'center-rating')]"),
            "address": ("xpath", ".//div[contains(@class,'address')]"),
            "details_button": ("xpath", ".//a[contains(@class,'details-button')]"),
        }

    def get_name_text(self):
        return self.title.text

    def click_title(self):
        self.title.click()

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()
