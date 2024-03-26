from selenium.webdriver import Keys
from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

from src.ui.elements.location_search_sider_element import LocationSearchSiderElement

CENTER_OR_CLUB_RADIO_BUTTON = (By.XPATH, ".//label[contains(@class,'ant-radio-wrapper')]")
CHECKED_RADIO_BUTTON = (By.XPATH, ".//span[contains(@class,'ant-radio-checked')]/following-sibling::span")
CITY_WEB_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'ant-select-in-form-item')][1]")
DISTRICT_WEB_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'ant-select-in-form-item')][2]")
METRO_WEB_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'ant-select-in-form-item')][3]")
ONLINE_CHECKBOX_FIELD = (By.XPATH, ".//div[@id='basic_isOnline']")
ONLINE_CHECKBOX_INPUT = (By.XPATH, ".//div[@id='basic_isOnline']//span[contains(@class, 'ant-wave-target')]")
DIRECTION_CHECKBOX_FIELD_LIST = (By.XPATH, ".//div[@id='basic_categoriesName']//label[contains(@class,'ant-checkbox-wrapper')]")
DIRECTION_CHECKBOX_INPUT_LIST = (By.XPATH, ".//div[@id='basic_categoriesName']//input")
AGE_INPUT = (By.XPATH, ".//span[@id='basic_age']//input[contains(@class,'ant-input-number-input')]")


class SearchSiderComponent(BaseComponent):

    def __init__(self, driver, node):
        super().__init__(node)
        self._driver = driver
        self._center_or_club = None
        self._checked_radio_button = None
        self._search_city_box = None
        self._search_district_box = None
        self._search_metro_box = None
        self._online_checkbox_field = None
        self._online_checkbox_input = None
        self._direction_checkbox_field_list = None
        self._direction_checkbox_input_list = None
        self._age_input = None

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

    @property
    def search_city_box(self):
        if not self._search_city_box:
            self._search_city_box = LocationSearchSiderElement(self._driver, self.node.find_element(*CITY_WEB_ELEMENT))
        return self._search_city_box

    @property
    def search_district_box(self):
        if not self._search_district_box:
            self._search_district_box = LocationSearchSiderElement(self._driver, self.node.find_element(*DISTRICT_WEB_ELEMENT))
        return self._search_district_box

    @property
    def search_metro_box(self):
        if not self._search_metro_box:
            self._search_metro_box = LocationSearchSiderElement(self._driver, self.node.find_element(*METRO_WEB_ELEMENT))
        return self._search_metro_box

    @property
    def online_checkbox_field(self):
        if not self._online_checkbox_field:
            self._online_checkbox_field = self.node.find_element(*ONLINE_CHECKBOX_FIELD)
        return self._online_checkbox_field

    @property
    def online_checkbox_input(self):
        if not self._online_checkbox_input:
            self._online_checkbox_input = self.node.find_element(*ONLINE_CHECKBOX_INPUT)
        return self._online_checkbox_input

    @property
    def direction_checkbox_field_list(self):
        if not self._direction_checkbox_field_list:
            self._direction_checkbox_field_list = self.node.find_elements(*DIRECTION_CHECKBOX_FIELD_LIST)
        return self._direction_checkbox_field_list

    @property
    def direction_checkbox_input_list(self):
        if not self._direction_checkbox_input_list:
            self._direction_checkbox_input_list = self.node.find_elements(*DIRECTION_CHECKBOX_INPUT_LIST)
        return self._direction_checkbox_input_list

    @property
    def age_input(self):
        if not self._age_input:
            self._age_input = self.node.find_element(*AGE_INPUT)
        return self._age_input

    def choose_club_radio_button(self):
        for e in self.center_or_club:
            if e.text == "Гурток":
                e.click()

    def choose_center_radio_button(self):
        for e in self.center_or_club:
            if e.text == "Центр":
                e.click()

    def click_clear_city(self):
        self.search_city_box.click_clear()

    def click_dropdown_city(self):
        self.search_city_box.click_dropdown()

    def select_city(self, city):
        self.search_city_box.select_item(city)

    def click_clear_district(self):
        self.search_district_box.click_clear()

    def click_dropdown_district(self):
        self.search_district_box.click_dropdown()

    def select_district(self, district):
        self.search_district_box.select_item(district)

    def click_clear_metro(self):
        self.search_metro_box.click_clear()

    def click_dropdown_metro(self):
        self.search_metro_box.click_dropdown()

    def select_metro(self, metro):
        self.search_metro_box.select_item(metro)

    def check_online_checkbox(self):
        self.online_checkbox_input.click()

    def check_direction_checkbox(self, direction):
        for d in self.direction_checkbox_field_list:
            if d.text == direction:
                d.click()

    def is_direction_checked(self, direction):
        for d in self.direction_checkbox_field_list:
            if d.text == direction:
                return "checked" in d.get_attribute("class")
        return False

    def enter_age(self, age):
        self.age_input.send_keys(age)

    def get_age_value(self):
        return self.age_input.get_attribute("value")

    def clear_age(self):
        current_platform = self.node.parent.capabilities['platformName'].lower()
        if current_platform == 'mac':
            self.age_input.send_keys(Keys.COMMAND + 'a')
            self.age_input.send_keys(Keys.DELETE)
        else:
            self.age_input.send_keys(Keys.CONTROL + 'a')
            self.age_input.send_keys(Keys.BACK_SPACE)
