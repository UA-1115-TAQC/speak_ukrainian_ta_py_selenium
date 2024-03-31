from typing import Self

from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.add_center_step_four import AddCenterStepFour
from src.ui.components.base_component import BaseComponent
from src.ui.elements.uploaded_image_element import UploadedImageElement


class AddCenterStepThree(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "center_popup_title": ("xpath", ".//div[@class='modal-title']"),
            "logo_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][1]"),
            "photo_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][2]"),
            "description_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][3]"),
            "logo_download_input": ("xpath", ".//input[@id='basic_urlLogo']"),
            "logo_download_button": (
                "xpath", "./descendant::span[(@class='ant-upload') and (@role='button')][1]"),
            "uploaded_logo_img_container": (
                "xpath", "./descendant::div[@class='ant-upload-list ant-upload-list-text'][1]"),
            "photo_download_input": ("xpath", ".//input[@id='basic_urlBackground']"),
            "photo_download_button": (
                "xpath", "./descendant::span[(@class='ant-upload') and (@role='button')][2]"),
            "uploaded_photo_img_container": (
                "xpath", "./descendant::div[@class='ant-upload-list ant-upload-list-text'][2]"),
            "description_textarea": ("xpath", ".//textarea[@id='basic_description']"),
            "validation_circle_icon_textarea": ("xpath", ".//div[@class='ant-form-item-control-input']" +
                                                "//span[contains(@class,'anticon-close-circle') or contains(@class,'anticon-check-circle')]"),
            "complete_button": ("xpath", ".//button[contains(@class,'finish-btn')]"),
            "next_step_button": ("xpath", ".//button[contains(@class,'next-btn')]"),
            "previous_step_button": ("xpath", ".//button[contains(@class,'prev-btn')]")
        }

    def get_center_popup_title_text(self) -> str:
        return self.center_popup_title.text

    def get_logo_title_text(self) -> str:
        return self.logo_title.text

    def upload_logo(self, image_path) -> Self:
        self.node.find_element(*self.locators["logo_download_input"]).send_keys(image_path)
        self.uploaded_logo_img_container.visibility_of_element_located()
        return self

    @property
    def logo_uploaded_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.uploaded_logo_img_container)

    def get_photo_title_text(self) -> str:
        return self.photo_title.text

    def upload_photo(self, image_path) -> Self:
        self.node.find_element(*self.locators["photo_download_input"]).send_keys(image_path)
        self.uploaded_photo_img_container.visibility_of_element_located()
        return self

    @property
    def photo_uploaded_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.uploaded_photo_img_container)

    def get_description_title_text(self) -> str:
        return self.description_title.text

    def get_textarea_value(self) -> str:
        return self.description_textarea.getAttribute("value")

    def set_textarea_value(self, value: str) -> Self:
        self.description_textarea.send_keys(value)
        return self

    def clear_textarea(self) -> Self:
        self.description_textarea.visibility_of_element_located().click()
        self.get_actions().key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        self.get_actions().key_down(Keys.COMMAND) \
            .send_keys('a') \
            .key_up(Keys.COMMAND) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        return self

    @property
    def textarea_error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators[".//div[contains(@class,'ant-col')]"
                                                      "//div[@class='ant-form-item-explain-error']"])

    def textarea_errors_text_list(self) -> list[str]:
        return [error.text for error in self.textarea_error_messages_list]

    def click_next_step_button(self) -> AddCenterStepFour:
        self.next_step_button.click_button()
        return AddCenterStepFour(self.node)

    def click_previous_step_button(self) -> 'AddCenterStepTwo':
        self.previous_step_button.click_button()
        from src.ui.components.add_center_popup.add_center_step_two import AddCenterStepTwo
        return AddCenterStepTwo(self.node)
