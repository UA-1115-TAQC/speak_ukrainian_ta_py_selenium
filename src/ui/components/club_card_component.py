from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

from src.ui.components.club_info_popup import ClubInfoPopup
from src.ui.elements.direction_element import DirectionElement

LOGO = (By.XPATH, ".//div[@class='title']//img")
NAME = (By.XPATH, ".//div[contains(@class,'name')]")
DIRECTIONS_WEB_ELEMENT = (By.XPATH, ".//span[contains(@class,'ant-tag')]")
DESCRIPTION = (By.XPATH, ".//p[contains(@class,'description')]")
RATING = (By.XPATH, ".//ul[contains(@class,'rating')]")
ADDRESS = (By.XPATH, ".//div[contains(@class,'address')]")
ADDRESS_LOCATION_NAME = (By.XPATH, "//div[contains(@class,'address')]/span[contains(@class,'text')]")
ONLINE = (By.XPATH, "./descendant::div[@class='club-online']")
DETAILS_BUTTON = (By.XPATH, ".//*[contains(@class,'details-button')]")
POPUP_WEB_ELEMENT = (By.XPATH, "//div[@class='ant-modal-root css-1kvr9ql']")


class ClubCardComponent(BaseComponent):

    def __init__(self, driver, node):
        super().__init__(node)
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._logo = None
        self._name = None
        self._direction_list = None
        self._description = None
        self._rating = None
        self._address = None
        self._address_location_name = None
        self._online = None
        self._details_button = None

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

    @property
    def direction_list(self):
        if not self._direction_list:
            self._direction_list = []
            directions = self.node.find_elements(*DIRECTIONS_WEB_ELEMENT)
            for direction in directions:
                self._direction_list.append(DirectionElement(direction))
        return self._direction_list

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
    def address_location_name(self):
        if not self._address_location_name:
            self._address_location_name = self.node.find_element(*ADDRESS_LOCATION_NAME)
        return self._address_location_name

    @property
    def online(self):
        if not self._online:
            self._online = self.node.find_element(*ONLINE)
        return self._online

    @property
    def details_button(self):
        if not self._details_button:
            self._details_button = self.node.find_element(*DETAILS_BUTTON)
        return self._details_button

    def get_logo_src(self):
        self.logo.get_attribute("src")

    def get_name_text(self):
        return self.name.text

    def name_contains(self, text):
        return text.lower() in self.get_name_text().lower()

    def direction_contains(self, text):
        for direction in self._direction_list:
            if text.lower() in direction.get_name_text().lower():
                return True
        return False

    def description_contains(self, text):
        return text.lower() in self.description.text.lower()

    def click_title(self):
        self.name.click()
        self._wait.until(ec.presence_of_element_located(POPUP_WEB_ELEMENT))
        return ClubInfoPopup(self._driver)

    def click_address(self):
        self.address.click()

    def click_details_button(self):
        self.details_button.click()
