from typing import Self

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_icon_element import InputWithIconElement
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors
from src.ui.elements.uploaded_image_element import UploadedImageElement


class EditUserPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "edit_user_popup_title": ("xpath", ".//div[@class='edit-header']"),
            "user_icon": ("xpath", "./descendant::div[@class='ellipse'][1]"),
            "user_type_button": ("xpath", "//input[@value='ROLE_USER']/../.."),
            "manager_icon": ("xpath", "./descendant::div[@class='ellipse'][2]"),
            "manager_type_button": ("xpath", "//input[@value='ROLE_MANAGER']/../.."),
            "last_name_input_element": ("xpath", "./descendant::div[contains(@class,'user-edit-input')][1]"),
            "first_name_input_element": ("xpath", "./descendant::div[contains(@class,'user-edit-input')][2]"),
            "phone_input_element": ("xpath", "./descendant::div[contains(@class,'user-edit-input')][3]"),
            "phone_country_code": ("xpath", ".//span[@class='ant-input-group-addon']"),
            "email_input_element": ("xpath", "./descendant::div[contains(@class,'user-edit-input')][4]"),
            "upload_user_photo_element": ("xpath", ".//span[contains(@class, 'ant-upload-wrapper')]"),
            "upload_user_photo_input": ("xpath", ".//input[@id='edit_urlLogo']"),
            "photo_title": ("xpath", ".//label[@for='edit_urlLogo']"),
            "question_circle_for_photo": ("xpath", ".//span[@aria-label='question-circle']"),
            "photo_tooltip_form": ("xpath", "//div[@class='ant-tooltip-inner']"),
            "checkbox_change_password_title": ("xpath", ".//div[contains(@class, 'align-checkbox')]/text"),
            "checkbox_change_password_input": ("xpath", ".//input[@name='checkbox']"),
            "current_password_input_element": ("xpath", "(//div[contains(@class,'item-control-input')]"
                                                        "/span[contains(@class,'ant-input-password')"
                                                        " and not (contains(@class,'login-box'))])[1]"),
            "new_password_input_element": ("xpath", "(//div[contains(@class,'item-control-input')]"
                                                    "/span[contains(@class,'ant-input-password')"
                                                    " and not (contains(@class,'login-box'))])[2]"),
            "confirm_password_input_element": ("xpath", "(//div[contains(@class,'item-control-input')]"
                                                        "/span[contains(@class,'ant-input-password')"
                                                        " and not (contains(@class,'login-box'))])[3]"),
            "submit_button": ("xpath", ".//button[contains(@class, 'submit-button')]")
        }

    def click_on_manager_type_button(self) -> Self:
        return self.manager_type_button.click_button()

    def click_on_user_type_button(self):
        return self.user_type_button.click_button()

    @property
    def last_name_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.last_name_input_element)

    @property
    def first_name_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.first_name_input_element)

    @property
    def phone_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.phone_input_element)

    @property
    def uploaded_photo_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.upload_user_photo_element)

    def upload_photo(self, img_path: str) -> Self:
        self.upload_user_photo_input.send_keys(img_path)
        WebDriverWait(self.node.parent, 10).until(lambda d: self.uploaded_photo_element.is_displayed())
        return self

    def click_on_checkbox_change_password(self) -> Self:
        return self.checkbox_change_password_input.click_button()

    @property
    def get_current_password_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.current_password_input_element)

    @property
    def get_new_password_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.new_password_input_element)

    @property
    def get_confirm_password_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.confirm_password_input_element)

    def click_on_submit_button(self):
        return self.submit_button.click_button()

    def get_tooltip_text(self) -> Self:
        self._actions.move_to_element(self.question_circle_for_photo).perform()
        tooltip = self._wait.until(EC.visibility_of(self.photo_tooltip_form))
        return tooltip.text

    def wait_until_element_is_visible(self, el: WebElement) -> None:
        self._wait.until(EC.visibility_of(el))

    def delete_user_avatar(self) -> Self:
        (self._actions
         .move_to_element(self.uploaded_photo_element.image_title)
         .pause(2)
         .move_to_element(self.uploaded_photo_element.delete_image_button)
         .click_button()
         .perform())
        self._wait.until(EC.invisibility_of_element(self.uploaded_photo_element.image_title))
        return self
