from selenium.webdriver.common.by import By
from src.ui.elements.base_element import BaseElement

LOGO = (By.XPATH, ".//div[contains(@class,'icon')]")
NAME = (By.XPATH, ".//span[contains(@class,'name')]")


class DirectionElement(BaseElement):
    def __init__(self, node):
        super().__init__(node)
        self._logo = None
        self._name = None

    @property
    def logo(self):
        if not self._logo:
            self._logo = self.node.find_element(*LOGO)
        return self._logo

    @property
    def name(self):
        if not self._name:
            self._name = self.node.find_element(*NAME)
        return self._name

    def get_name_text(self):
        return self.name.text
