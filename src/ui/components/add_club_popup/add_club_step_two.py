from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.components.base_component import BaseComponent
from src.ui.elements.day_time_checkbox_element import DayTimeCheckboxElement
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors
from src.ui.elements.location_list_element import LocationListElement

CLUB_POPUP_TITLE = (By.XPATH, ".//div[contains(@class,'add-club-header')]")
NEXT_STEP_BUTTON = (By.XPATH, "//button[contains(@class,'add-club-content-next')]")
PREVIOUS_STEP_BUTTON = (By.XPATH, "//button[contains(@class,'add-club-content-prev')]")
STEP_CONTAINER = (By.XPATH, ".//main[contains(@class,'add-club-container')]")
LOCATIONS_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][1]")
AVAILABLE_ONLINE_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][2]")
WORK_HOURS_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][3]")
CONTACTS_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][4]")
NO_DATA_LOCATION_ELEMENT = (By.XPATH, ".//div[contains(@class,'ant-empty-normal')]")
ADD_LOCATION_BUTTON = (By.XPATH, ".//span[contains(@class,'add-club-location')]")
SWITCH_BUTTON = (By.XPATH, ".//button[contains(@class,'ant-switch')]")
INFO_HINT_ICON = (By.XPATH, ".//span[contains(@class,'anticon-info-circle')]")
INFO_HINT_CONTAINER = (By.XPATH, "//descendant::div[contains(@class,'ant-tooltip-inner')]")
WORK_DAYS_LIST = (By.XPATH, ".//div[contains(@class,'ant-col')]//label[contains(@class,'ant-checkbox')]")
CHECKED_WORK_DAYS_LIST = (By.XPATH, ".//span[contains(@class,'ant-checkbox-checked')]"
                                    "/ancestor::div[@class='checkbox-item']")

TELEPHONE_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                             "/descendant::div[contains(@class,'add-club-contact')][1]")
FACEBOOK_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                            "/descendant::div[contains(@class,'add-club-contact')][2]")
WHATSAPP_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                            "/descendant::div[contains(@class,'add-club-contact')][3]")
EMAIL_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                         "/descendant::div[contains(@class,'add-club-contact')][4]")
SKYPE_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                         "/descendant::div[contains(@class,'add-club-contact')][5]")
SITE_INPUT = (By.XPATH, ".//div[contains(@class,'add-club-contacts')]"
                        "/descendant::div[contains(@class,'add-club-contact')][6]")
LOCATIONS_LIST = (By.XPATH, ".//ul[@class='ant-list-items']/li[@class='ant-list-item']")
LOCATION_POPUP = (By.XPATH, "//descendant::div[contains(@class,'modal-add-club')][2]")
STEP_CONTAINER = (By.XPATH, ".//main[contains(@class,'add-club-container')]")


class AddClubStepTwo(BaseComponent):
    def __init__(self, popup: 'AddClubPopUp', node: WebElement) -> None:
        super().__init__(node)
        self._popup = popup
        self._popup_title = None
        self._locations_title = None
        self._no_data_location = None
        self._add_location_button = None
        self._available_online_title = None
        self._switch_button = None
        self._info_hint_icon = None
        self._work_hours_title = None
        self._work_days_list = None
        self._contacts_title = None
        self._telephone_input_element = None
        self._facebook_input_element = None
        self._whatsapp_input_element = None
        self._email_input_element = None
        self._skype_input_element = None
        self._site_input_element = None
        self._next_button = None
        self._previous_button = None

    @property
    def popup_title(self) -> WebElement:
        if not self._popup_title:
            self._popup_title = self.node.find_element(*CLUB_POPUP_TITLE)
        return self._popup_title

    @property
    def locations_title(self) -> WebElement:
        if not self._locations_title:
            self._locations_title = self.node.find_element(*LOCATIONS_TITLE)
        return self._locations_title

    @property
    def no_data_location(self) -> WebElement:
        if not self._no_data_location:
            self._no_data_location = self.node.find_element(*NO_DATA_LOCATION_ELEMENT)
        return self._no_data_location

    @property
    def add_location_button(self) -> WebElement:
        if not self._add_location_button:
            self._add_location_button = self.node.find_element(*ADD_LOCATION_BUTTON)
        return self._add_location_button

    def click_add_location_button(self) -> AddLocationPopUp:
        self.add_location_button.click()
        return AddLocationPopUp(self.node.find_element(*LOCATION_POPUP))

    @property
    def location_list(self) -> list[WebElement]:
        return self.node.find_elements(*LOCATIONS_LIST)

    def get_locations_name_list(self) -> list[str]:
        return [location.text for location in self.location_list] if self.location_list else []

    def get_list_of_location_elements(self) -> list[LocationListElement]:
        return [LocationListElement(location) for location in self.location_list] if self.location_list else []

    @property
    def available_online_title(self) -> WebElement:
        if not self._available_online_title:
            self._available_online_title = self.node.find_element(*AVAILABLE_ONLINE_TITLE)
        return self._available_online_title

    @property
    def switch_button(self) -> WebElement:
        if not self._switch_button:
            self._switch_button = self.node.find_element(*SWITCH_BUTTON)
        return self._switch_button

    def click_switch_button(self) -> Self:
        self.switch_button.click()
        return self

    def is_switch_button_checked(self) -> bool:
        return self.switch_button.get_attribute("aria-checked") == "true"

    @property
    def info_hint_icon(self) -> WebElement:
        if not self._info_hint_icon:
            self._info_hint_icon = self.node.find_element(*INFO_HINT_ICON)
        return self._info_hint_icon

    def click_info_hint_icon(self) -> WebElement:
        self.info_hint_icon.click()
        return self.info_hint_container

    @property
    def info_hint_container(self) -> WebElement:
        return self.node.find_element(*INFO_HINT_CONTAINER)

    def info_hint_text(self) -> str:
        return self.info_hint_container.text

    @property
    def work_hours_title(self) -> WebElement:
        if not self._work_hours_title:
            self._work_hours_title = self.node.find_element(*WORK_HOURS_TITLE)
        return self._work_hours_title

    @property
    def work_days_list(self) -> list[WebElement]:
        if not self._work_days_list:
            self._work_days_list = self.node.find_elements(*WORK_DAYS_LIST)
        return self._work_days_list

    def work_days_texts_list(self) -> list[str]:
        return [day.get_attribute("innerText") for day in self.work_days_list]

    def get_day_time_checkbox_elements_collection(self) -> dict[str, DayTimeCheckboxElement]:
        day_time_checkbox_elements_collection = {}
        for day in self.work_days_list:
            checkbox_value = day.find_element(By.XPATH, ".//input").get_attribute("value")
            day_time_checkbox_elements_collection[checkbox_value] = DayTimeCheckboxElement(day)
        return day_time_checkbox_elements_collection

    def click_on_checkbox_by_day(self, value: str):
        self.get_day_time_checkbox_elements_collection().get(value.upper()).checkbox.click()
        return self

    @property
    def checked_work_days_list(self) -> list[WebElement]:
        return self.node.find_elements(*CHECKED_WORK_DAYS_LIST)

    def checked_work_days_texts_list(self) -> list[str]:
        return [day.get_attribute("innerText") for day in self.checked_work_days_list]

    @property
    def contacts_title(self) -> WebElement:
        if not self._contacts_title:
            self._contacts_title = self.node.find_element(*CONTACTS_TITLE)
        return self._contacts_title

    @property
    def telephone_input_element(self) -> InputWithLabelIconsErrors:
        if not self._telephone_input_element:
            self._telephone_input_element = InputWithLabelIconsErrors(self.node.find_element(*TELEPHONE_INPUT))
        return self._telephone_input_element

    @property
    def facebook_input_element(self) -> InputWithLabelIconsErrors:
        if not self._facebook_input_element:
            self._facebook_input_element = InputWithLabelIconsErrors(self.node.find_element(*FACEBOOK_INPUT))
        return self._facebook_input_element

    @property
    def whatsapp_input_element(self) -> InputWithLabelIconsErrors:
        if not self._whatsapp_input_element:
            self._whatsapp_input_element = InputWithLabelIconsErrors(self.node.find_element(*WHATSAPP_INPUT))
        return self._whatsapp_input_element

    @property
    def email_input_element(self) -> InputWithLabelIconsErrors:
        if not self._email_input_element:
            self._email_input_element = InputWithLabelIconsErrors(self.node.find_element(*EMAIL_INPUT))
        return self._email_input_element

    @property
    def skype_input_element(self) -> InputWithLabelIconsErrors:
        if not self._skype_input_element:
            self._skype_input_element = InputWithLabelIconsErrors(self.node.find_element(*SKYPE_INPUT))
        return self._skype_input_element

    @property
    def site_input_element(self) -> InputWithLabelIconsErrors:
        if not self._site_input_element:
            self._site_input_element = InputWithLabelIconsErrors(self.node.find_element(SITE_INPUT))
        return self._site_input_element

    @property
    def next_button(self) -> WebElement:
        if not self._next_button:
            self._next_button = self.node.find_element(*NEXT_STEP_BUTTON)
        return self._next_button

    def click_next_step_button(self) -> None:
        self.next_button.click()

    @property
    def previous_button(self) -> WebElement:
        if not self._previous_button:
            self._previous_button = self.node.find_element(*PREVIOUS_STEP_BUTTON)
        return self._previous_button

    @property
    def popup(self) -> 'AddClubPopUp':
        return self._popup

    def click_previous_step_button(self) -> 'AddClubStepOne':
        self.previous_button.click()
        return self.popup.step_one_container
