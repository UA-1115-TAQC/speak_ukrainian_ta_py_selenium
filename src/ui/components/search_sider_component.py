from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

CENTER_OR_CLUB_RADIO_BUTTON = (By.XPATH, ".//label[contains(@class,'ant-radio-wrapper')]")
CHECKED_RADIO_BUTTON = (By.XPATH, ".//span[contains(@class,'ant-radio-checked')]/following-sibling::span")

class search_sider_component(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._center_or_club = None
        self._checked_radio_button = None


    @property
    def center_or_club(self):
        if not self._center_or_club:
            self._center_or_club = self.node.find_elements(*CENTER_OR_CLUB_RADIO_BUTTON)
        return self._center_or_club

    @property
    def checked_radio_button(self):
        if not self._checked_radio_button:
            self._checked_radio_button = self.node.find_element(*CHECKED_RADIO_BUTTON)
        return self._checked_radio_button

    def choose_club_radio_button(self):
        for e in self.center_or_club:
            if e.text == "Гурток":
                e.click()

    def choose_center_radio_button(self):
        for e in self.center_or_club:
            if e.text == "Центр":
                e.click()
