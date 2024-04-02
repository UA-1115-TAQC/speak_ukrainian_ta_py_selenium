from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_club_popup.add_club_step_three import AddClubStepThree
from src.ui.components.add_club_popup.day_time_checkbox_element import DayTimeCheckboxElement
from src.ui.components.add_club_popup.location_list_element import LocationListElement
from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.components.base_component import BaseComponent
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors


class AddClubStepTwo(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "club_popup_title": ("xpath", ".//div[contains(@class,'add-club-header')]"),
            "next_step_button": ("xpath", ".//button[contains(@class,'add-club-content-next')]"),
            "previous_step_button": ("xpath", ".//button[contains(@class,'add-club-content-prev')]"),
            "locations_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][1]"),
            "available_online_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][2]"),
            "work_hours_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][3]"),
            "contacts_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][4]"),
            "no_data_location_element": ("xpath", ".//div[contains(@class,'ant-empty-normal')]"),
            "add_location_button": ("xpath", ".//span[contains(@class,'add-club-location')]"),
            "switch_button": ("xpath", ".//button[contains(@class,'ant-switch')]"),
            "info_hint_icon": ("xpath", ".//span[contains(@class,'anticon-info-circle')]"),
            "info_hint_container": ("xpath", "//descendant::div[contains(@class,'ant-tooltip-inner')]"),
            "work_days_list": ("xpath", ".//div[contains(@class,'checkbox-item')]"),
            "checked_work_days_list": ("xpath", ".//span[contains(@class,'ant-checkbox-checked')]"
                                                "/ancestor::div[@class='checkbox-item']"),
            "telephone_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                         "/descendant::div[contains(@class,'add-club-contact')][1]"),
            "facebook_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                        "/descendant::div[contains(@class,'add-club-contact')][2]"),
            "whatsapp_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                        "/descendant::div[contains(@class,'add-club-contact')][3]"),
            "email_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                     "/descendant::div[contains(@class,'add-club-contact')][4]"),
            "skype_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                     "/descendant::div[contains(@class,'add-club-contact')][5]"),
            "site_input": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                    "/descendant::div[contains(@class,'add-club-contact')][6]"),
            "locations_list": ("xpath", ".//ul[@class='ant-list-items']/li[@class='ant-list-item']"),
            "location_popup": ("xpath", "//descendant::div[contains(@class,'modal-add-club')][2]"),
            "step_container": ("xpath", ".//main[contains(@class,'add-club-container')]")
        }

    def click_add_location_button(self) -> AddLocationPopUp:
        self.add_location_button.click_button()
        return AddLocationPopUp(self.location_popup)

    @property
    def location_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["locations_list"])

    def get_locations_name_list(self) -> list[str]:
        return [location.text for location in self.location_list] if self.location_list else []

    def get_list_of_location_elements(self) -> list[LocationListElement]:
        return [LocationListElement(location) for location in self.location_list] if self.location_list else []

    def click_switch_button(self):
        self.switch_button.click_button()

    def is_switch_button_checked(self) -> bool:
        return self.switch_button.get_attribute("aria-checked") == "true"

    def click_info_hint_icon(self) -> WebElement:
        self.info_hint_icon.click_button()
        return self.info_hint_container

    def info_hint_text(self) -> str:
        return self.info_hint_container.text

    @property
    def work_days_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["work_days_list"])

    def work_days_texts_list(self) -> list[str]:
        return [day.get_attribute("innerText") for day in self.work_days_list]

    def get_day_time_checkbox_elements_collection(self) -> dict[str, DayTimeCheckboxElement]:
        day_time_checkbox_elements_collection = {}
        for day in self.work_days_list:
            checkbox_value = day.find_element(By.XPATH, ".//input[@class='ant-checkbox-input']").get_attribute("value")
            day_time_checkbox_elements_collection[checkbox_value] = DayTimeCheckboxElement(day)
        return day_time_checkbox_elements_collection

    def click_on_checkbox_by_day(self, day: str):
        self.get_day_time_checkbox_elements_collection().get(day.upper()).click_on_checkbox()
        return self

    def set_time_checkbox_by_day(self, day: str, time_from: str, time_to: str):
        self.get_day_time_checkbox_elements_collection().get(day.upper()).set_time_from_input(time_from)
        self.get_day_time_checkbox_elements_collection().get(day.upper()).set_time_to_input(time_to)
        return self

    @property
    def checked_work_days_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["checked_work_days_list"])

    def checked_work_days_texts_list(self) -> list[str]:
        return [day.get_attribute("innerText") for day in self.checked_work_days_list]

    @property
    def telephone_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.telephone_input)

    @property
    def facebook_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.facebook_input)

    @property
    def whatsapp_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.whatsapp_input)

    @property
    def email_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.email_input)

    @property
    def skype_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.skype_input)

    @property
    def site_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.site_input)

    def click_next_step_button(self) -> AddClubStepThree:
        self.next_step_button.click_button()
        return AddClubStepThree(self.node)

    def click_previous_step_button(self) -> 'AddClubStepOne':
        self.previous_step_button.click_button()
        from src.ui.components.add_club_popup.add_club_step_one import AddClubStepOne
        return AddClubStepOne(self.step_container)
