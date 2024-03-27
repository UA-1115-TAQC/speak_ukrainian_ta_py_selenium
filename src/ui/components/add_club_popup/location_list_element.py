from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.add_location_popup.add_location_popup_component import AddLocationPopUp
from src.ui.elements.base_element import BaseElement


class LocationListElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "location_title": ("xpath", ".//h4[@class='ant-list-item-meta-title']"),
            "location_description": ("xpath", ".//div[@class='ant-list-item-meta-description']"),
            "edit_icon": ("xpath", "//ul[@class='ant-list-item-action']//span[@aria-label='edit']"),
            "delete_icon": ("xpath", "//ul[@class='ant-list-item-action']//span[@aria-label='delete']"),
            "pop_confirm_container": ("xpath", "//div[@class='ant-popover-inner-content']"),
            "pop_confirm_icon": ("xpath", "//div[@class='ant-popover-inner-content']"
                                          "/descendant::span[@aria-label='exclamation-circle']"),
            "pop_confirm_title": ("xpath", "//div[@class='ant-popover-inner-content']"),
            "pop_confirm_ok_button": ("xpath", "//div[@class='ant-popover-inner-content']"
                                               "/descendant::button[contains(@class,'popconfirm-ok-button')]"),
            "pop_confirm_cancel_button": ("xpath", "//div[@class='ant-popover-inner-content']"
                                                   "/descendant::button[contains(@class,'popconfirm-cancel-button')]"),
            "location_popup": ("xpath", "//descendant::div[contains(@class,'modal-add-club')][2]")
        }

    def click_edit_icon(self) -> AddLocationPopUp:
        self.edit_icon.click_button()
        return AddLocationPopUp(self.location_popup)

    def click_delete_icon(self) -> WebElement:
        self.delete_icon.click_button()
        return self.pop_confirm_container

    def click_pop_confirm_ok_button(self) -> None:
        self.pop_confirm_ok_button.click_button()

    def click_pop_confirm_cancel_button(self) -> None:
        self.pop_confirm_cancel_button.click_button()
