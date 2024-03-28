from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_icon_element import InputWithIconElement
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors
from src.ui.elements.uploaded_image_element import UploadedImageElement

EDIT_USER_POPUP_TITLE = (By.XPATH, ".//div[@class='edit-header']")
USER_ICON = (By.XPATH, "./descendant::div[@class='ellipse'][1]")
USER_TYPE_BUTTON = (By.XPATH, "//input[@value='ROLE_USER']/../..")
MANAGER_ICON = (By.XPATH, "./descendant::div[@class='ellipse'][2]")
MANAGER_TYPE_BUTTON = (By.XPATH, "//input[@value='ROLE_MANAGER']/../..")
LAST_NAME_INPUT_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'user-edit-input')][1]")
FIRST_NAME_INPUT_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'user-edit-input')][2]")
PHONE_INPUT_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'user-edit-input')][3]")
PHONE_COUNTRY_CODE = (By.XPATH, ".//span[@class='ant-input-group-addon']")
EMAIL_INPUT_ELEMENT = (By.XPATH, "./descendant::div[contains(@class,'user-edit-input')][4]")
UPLOAD_USER_PHOTO_ELEMENT = (By.XPATH, ".//span[contains(@class, 'ant-upload-wrapper')]")
UPLOAD_USER_PHOTO_INPUT = (By.XPATH, ".//input[@id='edit_urlLogo']")
PHOTO_TITLE = (By.XPATH, ".//label[@for='edit_urlLogo']")

CHECKBOX_CHANGE_PASSWORD_TITLE = (By.XPATH, ".//div[contains(@class, 'align-checkbox')]/text")
CHECKBOX_CHANGE_PASSWORD_INPUT = (By.XPATH, ".//input[@name='checkbox']")
CURRENT_PASSWORD_INPUT_ELEMENT = (By.XPATH, "(//div[contains(@class,'item-control-input')]"
                                            "/span[contains(@class,'ant-input-password')"
                                            " and not (contains(@class,'login-box'))])[1]")
NEW_PASSWORD_INPUT_ELEMENT = (By.XPATH, "(//div[contains(@class,'item-control-input')]"
                                        "/span[contains(@class,'ant-input-password')"
                                        " and not (contains(@class,'login-box'))])[2]")
CONFIRM_PASSWORD_INPUT_ELEMENT = (By.XPATH, "(//div[contains(@class,'item-control-input')]"
                                            "/span[contains(@class,'ant-input-password')"
                                            " and not (contains(@class,'login-box'))])[3]")
SUBMIT_BUTTON = (By.XPATH, ".//button[contains(@class, 'submit-button')]")


class EditUserPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super(self).__init__(node)
        self._pop_up_title = None
        self._manager_icon = None
        self._user_icon = None
        self._last_name_input_element = None
        self._first_name_input_element = None
        self._phone_input_element = None
        self._phone_country_code = None
        self._email_input_element = None
        self._photo_title = None
        self._checkbox_title = None
        self._current_password_input_element = None
        self._new_password_input_element = None
        self._confirm_password_input_element = None

    @property
    def edit_user_pop_up_title(self) -> WebElement:
        if not self._pop_up_title:
            self._pop_up_title = (self.node.find_element(*EDIT_USER_POPUP_TITLE))
        return self._pop_up_title

    @property
    def manager_type_button(self) -> WebElement:
        return self.node.find_element(*MANAGER_TYPE_BUTTON)

    def click_on_manager_type_button(self):
        return self.manager_type_button.click()

    @property
    def manager_icon(self) -> WebElement:
        if not self._manager_icon:
            self._manager_icon = self.node.find_element(*MANAGER_ICON)
        return self._manager_icon

    @property
    def user_type_button(self) -> WebElement:
        return self.node.find_element(*USER_TYPE_BUTTON)

    def click_on_user_type_button(self):
        return self.user_type_button.click()

    @property
    def user_icon(self) -> WebElement:
        if not self._user_icon:
            self._user_icon = self.node.find_element(*USER_ICON)
        return self._user_icon

    @property
    def last_name_element(self) -> InputWithLabelIconsErrors:
        if not self._last_name_input_element:
            self._last_name_input_element = InputWithLabelIconsErrors(self.node.find_element(*LAST_NAME_INPUT_ELEMENT))
        return self._last_name_input_element

    @property
    def first_name_element(self) -> InputWithLabelIconsErrors:
        if not self._first_name_input_element:
            self._first_name_input_element = InputWithLabelIconsErrors(
                self.node.find_element(*FIRST_NAME_INPUT_ELEMENT))
        return self._first_name_input_element

    @property
    def phone_element(self) -> InputWithLabelIconsErrors:
        if not self._phone_input_element:
            self._phone_input_element = InputWithLabelIconsErrors(self.node.find_element(*PHONE_INPUT_ELEMENT))
        return self._phone_input_element

    @property
    def phone_country_code_element(self) -> WebElement:
        if not self._phone_country_code:
            self._phone_country_code = self.node.find_element(*PHONE_COUNTRY_CODE)
        return self._phone_country_code

    @property
    def photo_title(self) -> WebElement:
        if not self._photo_title:
            self._photo_title = (self.node.find_element(*PHOTO_TITLE))
        return self._photo_title

    @property
    def uploaded_photo_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.node.find_element(*UPLOAD_USER_PHOTO_ELEMENT))

    @property
    def upload_photo_input(self) -> WebElement:
        return self.node.find_element(*UPLOAD_USER_PHOTO_INPUT)

    def upload_photo(self, img_path: str) -> Self:
        self.upload_photo_input.send_keys(img_path)
        WebDriverWait(self.node.parent, 10).until(lambda d: self.uploaded_photo_element.is_displayed())
        return self

    @property
    def checkbox_title(self) -> WebElement:
        if not self._checkbox_title:
            self._checkbox_title = self.node.find_element(*CHECKBOX_CHANGE_PASSWORD_TITLE)
        return self._checkbox_title

    @property
    def checkbox_element(self) -> WebElement:
        return self.node.find_element(*CHECKBOX_CHANGE_PASSWORD_INPUT)

    def click_on_checkbox_change_password(self) -> Self:
        return self.checkbox_element.click()

    @property
    def current_password_input_element(self) -> InputWithIconElement:
        if not self._current_password_input_element:
            self._current_password_input_element = InputWithIconElement(
                self.node.find_element(*CURRENT_PASSWORD_INPUT_ELEMENT))
        return self._current_password_input_element

    @property
    def new_password_input_element(self) -> InputWithIconElement:
        if not self._new_password_input_element:
            self._new_password_input_element = InputWithIconElement(self.node.find_element(*NEW_PASSWORD_INPUT_ELEMENT))
        return self._new_password_input_element

    @property
    def confirm_password_input_element(self) -> InputWithIconElement:
        if not self._confirm_password_input_element:
            self._confirm_password_input_element = InputWithIconElement(
                self.node.find_element(*CONFIRM_PASSWORD_INPUT_ELEMENT))
        return self._confirm_password_input_element

    @property
    def submit_button(self) -> WebElement:
        return self.node.find_element(*SUBMIT_BUTTON)

    def click_on_submit_button(self):
        return self.submit_button.click()
