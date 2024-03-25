from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

LOGO = (By.XPATH, ".//div[contains(@class,'icon')]")
NAME = (By.XPATH, ".//span[contains(@class,'name')]")

class direction_component(BaseComponent):
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

    def get_name_text(self, text):
        self.name.text
