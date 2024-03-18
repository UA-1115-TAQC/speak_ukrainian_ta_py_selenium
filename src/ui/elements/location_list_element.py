from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.elements.base_element import BaseElement

LOCATION_TITLE = (By.XPATH, ".//h4[@class='ant-list-item-meta-title']")
LOCATION_DESCRIPTION = (By.XPATH, ".//div[@class='ant-list-item-meta-description']")
EDIT_ICON = (By.XPATH, "//ul[@class='ant-list-item-action']//span[@aria-label='edit']")
DELETE_ICON = (By.XPATH, "//ul[@class='ant-list-item-action']//span[@aria-label='delete']")
POP_CONFIRM_CONTAINER = (By.XPATH, "//div[@class='ant-popover-inner-content']")
POP_CONFIRM_ICON = (By.XPATH, "//div[@class='ant-popover-inner-content']"
                              "/descendant::span[@aria-label='exclamation-circle']")
POP_CONFIRM_TITLE = (By.XPATH, "//div[@class='ant-popover-inner-content']")
POP_CONFIRM_OK_BUTTON = (By.XPATH, "//div[@class='ant-popover-inner-content']"
                                   "/descendant::button[contains(@class,'popConfirm-ok-button')]")
POP_CONFIRM_CANCEL_BUTTON = (By.XPATH, "//div[@class='ant-popover-inner-content']"
                                       "/descendant::button[contains(@class,'popConfirm-cancel-button')]")
LOCATION_POPUP = (By.XPATH, "//descendant::div[contains(@class,'modal-add-club')][2]")


class LocationListElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._location_title = None
        self._location_description = None
        self._edit_icon = None
        self._delete_icon = None
        self._pop_confirm_container = None
        self._pop_confirm_icon = None
        self._pop_confirm_title = None
        self._pop_confirm_ok_button = None
        self._pop_confirm_cancel_button = None

    @property
    def location_title(self) -> WebElement:
        if not self._location_title:
            self._location_title = self.node.find_element(*LOCATION_TITLE)
        return self._location_title

    @property
    def location_description(self) -> WebElement:
        if not self._location_description:
            self._location_description = self.node.find_element(*LOCATION_DESCRIPTION)
        return self._location_description

    @property
    def edit_icon(self) -> WebElement:
        if not self._edit_icon:
            self._edit_icon = self.node.find_element(*EDIT_ICON)
        return self._edit_icon

    def click_edit_icon(self) -> AddLocationPopUp:
        self.edit_icon.click()
        return AddLocationPopUp(self.node.find_element(*LOCATION_POPUP))

    @property
    def delete_icon(self) -> WebElement:
        if not self._delete_icon:
            self._delete_icon = self.node.find_element(*DELETE_ICON)
        return self._delete_icon

    def click_delete_icon(self) -> WebElement:
        self.delete_icon.click()
        return self.pop_confirm_container

    @property
    def pop_confirm_container(self) -> WebElement:
        if not self._pop_confirm_container:
            self._pop_confirm_container = self.node.find_element(*POP_CONFIRM_CONTAINER)
        return self._pop_confirm_container

    @property
    def pop_confirm_icon(self) -> WebElement:
        if not self._pop_confirm_icon:
            self._pop_confirm_icon = self.node.find_element(*POP_CONFIRM_ICON)
        return self._pop_confirm_icon

    @property
    def pop_confirm_title(self) -> WebElement:
        if not self._pop_confirm_title:
            self._pop_confirm_title = self.node.find_element(*POP_CONFIRM_TITLE)
        return self._pop_confirm_title

    @property
    def pop_confirm_ok_button(self) -> WebElement:
        if not self._pop_confirm_ok_button:
            self._pop_confirm_ok_button = self.node.find_element(*POP_CONFIRM_OK_BUTTON)
        return self._pop_confirm_ok_button

    def click_pop_confirm_ok_button(self) -> None:
        self.pop_confirm_ok_button.click()

    @property
    def pop_confirm_cancel_button(self) -> WebElement:
        if not self._pop_confirm_cancel_button:
            self._pop_confirm_cancel_button = self.node.find_element(*POP_CONFIRM_CANCEL_BUTTON)
        return self._pop_confirm_cancel_button

    def click_pop_confirm_cancel_button(self) -> None:
        self.pop_confirm_cancel_button.click()
