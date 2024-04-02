from selenium.webdriver.support import expected_conditions as ec

from src.ui.components.base_component import BaseComponent
from src.ui.components.club_info_popup import ClubInfoPopup
from src.ui.elements.direction_element import DirectionElement


class ClubCardComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "logo": ("xpath", ".//div[@class='title']//img"),
            "name": ("xpath", ".//div[contains(@class,'name')]"),
            "directions": ("xpath", ".//span[contains(@class,'ant-tag')]"),
            "description": ("xpath", ".//p[contains(@class,'description')]"),
            "rating": ("xpath", ".//ul[contains(@class,'rating')]"),
            "address": ("xpath", ".//div[contains(@class,'address')]"),
            "address_location_name": ("xpath", "//div[contains(@class,'address')]/span[contains(@class,'text')]"),
            "online": ("xpath", "./descendant::div[@class='club-online']"),
            "details_button": ("xpath", ".//*[contains(@class,'details-button')]"),
            "popup": ("xpath", "//div[@class='ant-modal-root css-1kvr9ql']"),
            "club_info_popup_root": ("xpath", "//div[contains(@class,'clubInfo')]"),
        }

    @property
    def direction_list(self):
        directions = self.node.find_elements(*self.locators["directions"])
        return [DirectionElement(direction) for direction in directions]

    def get_logo_src(self):
        self.logo.get_attribute("src")

    def get_name_text(self):
        return self.name.text

    def name_contains(self, text):
        return text.lower() in self.get_name_text().lower()

    def direction_contains(self, text):
        for direction in self.direction_list:
            if text.lower() in direction.get_name_text().lower():
                return True
        return False

    def description_contains(self, text):
        return text.lower() in self.description.text.lower()

    def click_title(self):
        self.name.click()
        self.get_wait(30).until(ec.presence_of_element_located(self.locators["popup"]))
        return ClubInfoPopup(self.club_info_popup_root)

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()
