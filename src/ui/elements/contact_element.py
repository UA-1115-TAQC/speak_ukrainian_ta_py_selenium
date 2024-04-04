from src.ui.elements.base_element import BaseElement


class ContactElement(BaseElement):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "icon": ("xpath", ".//div[contains(@class,'icon')]"),
            "name": ("xpath", ".//span[contains(@class,'contact-name')]"),
            "href": ("xpath", ".//a"),
        }

    def click_contact(self):
        href = self.name.find_elements(*self.locators["href"])
        if len(href):
            href[0].click()
