from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

TITLE = (By.XPATH, ".//div[contains(@class,'center-title')]")
DESCRIPTION = (By.XPATH,".//p[contains(@class,'center-description-in-block')]")
RATING = (By.XPATH, ".//ul[contains(@class,'center-rating')]")
ADDRESS = (By.XPATH, ".//div[contains(@class,'address')]")
DETAILS_BUTTON = (By.XPATH, ".//a[contains(@class,'details-button')]")

class center_card_component(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._title = None
        self._description = None
        self._rating = None
        self._address = None
        self._details_button = None

    @property
    def title(self):
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title

    @property
    def description(self):
        if not self._description:
            self._description = self.node.find_element(*DESCRIPTION)
        return self._description

    @property
    def rating(self):
        if not self._rating:
            self._rating = self.node.find_element(*RATING)
        return self._rating

    @property
    def address(self):
        if not self._address:
            self._address = self.node.find_element(*ADDRESS)
        return self._address

    @property
    def details_button(self):
        if not self._details_button:
            self._details_button = self.node.find_element(*DETAILS_BUTTON)
        return self._details_button

    def click_title(self):
        self.name.click()

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()

