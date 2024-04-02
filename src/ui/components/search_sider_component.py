from selenium.webdriver import Keys

from src.ui.components.base_component import BaseComponent
from src.ui.elements.location_search_sider_element import LocationSearchSiderElement


class SearchSiderComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "center_or_club_radio_button": ("xpath", ".//label[contains(@class,'ant-radio-wrapper')]"),
            "checked_radio_button": ("xpath", ".//span[contains(@class,'ant-radio-checked')]/following-sibling::span"),
            "search_city_element": ("xpath", "./descendant::div[contains(@class,'ant-select-in-form-item')][1]"),
            "search_district_element": ("xpath", "./descendant::div[contains(@class,'ant-select-in-form-item')][2]"),
            "search_metro_element": ("xpath", "./descendant::div[contains(@class,'ant-select-in-form-item')][3]"),
            "online_checkbox_field": ("xpath", ".//div[@id='basic_isOnline']"),
            "online_checkbox_input": ("xpath", ".//div[@id='basic_isOnline']//span[contains(@class, 'ant-wave-target')]"),
            "direction_checkbox_field_list": ("xpath", ".//div[@id='basic_categoriesName']//label[contains(@class,'ant-checkbox-wrapper')]"),
            "direction_checkbox_input_list": ("xpath", ".//div[@id='basic_categoriesName']//input"),
            "age_input": ("xpath", ".//span[@id='basic_age']//input[contains(@class,'ant-input-number-input')]"),
        }

    @property
    def center_or_club_radio_button(self):
        return self.node.find_elements(*self.locators["center_or_club_radio_button"])

    @property
    def search_city_box(self):
        return LocationSearchSiderElement(self.search_city_element)

    @property
    def search_district_box(self):
        return LocationSearchSiderElement(self.search_district_element)

    @property
    def search_metro_box(self):
        return LocationSearchSiderElement(self.search_metro_element)

    @property
    def direction_checkbox_field_list(self):
        return self.node.find_elements(*self.locators["direction_checkbox_field_list"])

    @property
    def direction_checkbox_input_list(self):
        return self.node.find_elements(*self.locators["direction_checkbox_input_list"])

    def choose_club_radio_button(self):
        for e in self.center_or_club_radio_button:
            if e.text == "Гурток":
                e.click()

    def choose_center_radio_button(self):
        for e in self.center_or_club_radio_button:
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
        return self
