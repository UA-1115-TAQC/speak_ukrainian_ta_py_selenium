from selenium.webdriver.common.by import By
from src.ui.elements.base_element import BaseElement

ICON = (By.XPATH, ".//div[contains(@class,'icon')]")
NAME = (By.XPATH, ".//span[contains(@class,'contact-name')]")


class ContactElement(BaseElement):

    def __init__(self, node):
        super().__init__(node)
        self._icon = None
        self._name = None

    @property
    def icon(self):
        if not self._icon:
            self._icon = self.node.find_element(*ICON)
        return self._icon

    @property
    def name(self):
        if not self._name:
            self._name = self.node.find_element(*NAME)
        return self._name

    def click_contact(self):
        hrefs = self.name.find_elements(By.XPATH, ".//a")
        if len(hrefs) > 0:
            hrefs[0].click()

