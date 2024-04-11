import re
from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.contact_element import ContactElement
from src.ui.elements.direction_element import DirectionElement


class ClubInfoPopup(BasePopUp):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            **self.locators,
            "title": ("xpath", ".//div[contains(@class, 'title')]"),
            "directions": ("xpath", ".//span[contains(@class,'ant-tag')]"),
            "rating": ("xpath", ".//ul[contains(@class,'ant-rate')]"),
            "address": ("xpath", ".//div[@class = 'address']"),
            "age_sider_label": ("xpath", ".//div[@class = 'age']//span[contains(@class, 'sider-label')]"),
            "age_years": ("xpath", ".//span[@class = 'years']"),
            "contacts": ("xpath", ".//div[contains(@class,'contact')]"),
            "details_button": ("xpath", ".//button[contains(@class,'more-button')]"),
            "description": ("xpath", ".//div[contains(@class, 'about')]//div[@class = 'description']"),
            "feedback": ("xpath", ".//span[contains(@class,'feedback')]"),
            "download_button": ("xpath", ".//button[contains(@class,'download-button')]"),
        }

    @property
    def direction_list(self):
        directions = self.node.find_elements(*self.locators["directions"])
        return [DirectionElement(direction) for direction in directions]

    @property
    def contact_list(self):
        contacts = self.node.find_elements(*self.locators["contacts"])
        return [ContactElement(contact) for contact in contacts]

    def directions_contains(self, text):
        for d in self.direction_list:
            if text.lower() in d.get_name_text().lower():
                return True
        return False

    def description_contains(self, text):
        return text.lower() in self.description.get_name_text().lower()

    def get_age_list(self):
        pattern = 'від\\s+(\\d+)\\s+до\\s+(\\d+)\\s+років'
        matcher = re.search(pattern, self.age_years.get_attribute("innerText"))
        if matcher:
            return [int(matcher.group(1)), int(matcher.group(2))]
        return []

    def click_details_button(self):
        self.details_button.click()

    def click_feedback(self):
        self.feedback.click()

    def click_download_button(self):
        self.download_button.click()
