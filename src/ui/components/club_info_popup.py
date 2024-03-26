import re
from selenium.webdriver.common.by import By
from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.contact_element import ContactElement
from src.ui.elements.direction_element import DirectionElement

ROOT = (By.XPATH, "//div[contains(@class,'clubInfo')]")
TITLE = (By.XPATH, ".//div[contains(@class, 'title')]")
DIRECTIONS_WEB_ELEMENT = (By.XPATH, ".//span[contains(@class,'ant-tag')]")
RATING = (By.XPATH, ".//ul[contains(@class,'ant-rate')]")
ADDRESS = (By.XPATH, ".//div[@class = 'address']")
AGE_SIDER_LABEL = (By.XPATH, ".//div[@class = 'age']//span[contains(@class, 'sider-label')]")
AGE_YEARS = (By.XPATH, ".//span[@class = 'years']")
CONTACTS_WEB_ELEMENT = (By.XPATH, ".//div[contains(@class,'contact')]")
DETAILS_BUTTON = (By.XPATH, ".//button[contains(@class,'more-button')]")
DESCRIPTION = (By.XPATH, ".//div[contains(@class, 'about')]//div[@class = 'description']")
FEEDBACK = (By.XPATH, ".//span[contains(@class,'feedback')]")
DOWNLOAD_BUTTON = (By.XPATH, ".//button[contains(@class,'download-button')]")


class ClubInfoPopup(BasePopUp):

    def __init__(self, driver):
        super().__init__(driver.find_element(*ROOT))
        self._title = None
        self._direction_list = None
        self._rating = None
        self._address = None
        self._age_sider_label = None
        self._age_years = None
        self._contact_list = None
        self._details_button = None
        self._description = None
        self._feedback = None
        self._download_button = None

    @property
    def title(self):
        if not self._title:
            self._title = self.node.find_element(*TITLE)
        return self._title

    @property
    def direction_list(self):
        if not self._direction_list:
            self._direction_list = []
            directions = self.node.find_elements(*DIRECTIONS_WEB_ELEMENT)
            for direction in directions:
                self._direction_list.append(DirectionElement(direction))
        return self._direction_list

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
    def age_sider_label(self):
        if not self._age_sider_label:
            self._age_sider_label = self.node.find_element(*AGE_SIDER_LABEL)
        return self._age_sider_label

    @property
    def age_years(self):
        if not self._age_years:
            self._age_years = self.node.find_element(*AGE_YEARS)
        return self._age_years

    @property
    def contact_list(self):
        if not self._contact_list:
            self._contact_list = []
            contacts = self.node.find_elements(*DIRECTIONS_WEB_ELEMENT)
            for contact in contacts:
                self._contact_list.append(ContactElement(contact))
        return self._contact_list

    @property
    def details_button(self):
        if not self._details_button:
            self._details_button = self.node.find_element(*DETAILS_BUTTON)
        return self._details_button

    @property
    def description(self):
        if not self._description:
            self._description = self.node.find_element(*DESCRIPTION)
        return self._description

    @property
    def feedback(self):
        if not self._feedback:
            self._feedback = self.node.find_element(*FEEDBACK)
        return self._feedback

    @property
    def download_button(self):
        if not self._download_button:
            self._download_button = self.node.find_element(*DOWNLOAD_BUTTON)
        return self._download_button

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
