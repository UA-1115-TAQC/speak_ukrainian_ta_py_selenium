from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors

USER_TYPE_BUTTON = (By.XPATH, "//input[@value='ROLE_USER']/../..")
MANAGER_TYPE_BUTTON = (By.XPATH, "//input[@value='ROLE_MANAGER']/../..")
GOOGLE_BUTTON = (By.XPATH, "//a[contains(@href, 'google')]")
FACEBOOK_BUTTON = (By.XPATH, "//a[contains(@href, 'facebook')]")
LASTNAME_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][1]")
FIRSTNAME_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][2]")
PHONE_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][3]")
EMAIL_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][4]")
PASSWORD_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][5]")
PASSWORD_CONFIRMATION_INPUT = (By.XPATH, ".//div[contains(@class, 'ant-form-item registration-input')][6]")
REGISTRATION_BUTTON = (By.XPATH, ".//button[contains(@class, 'registration-button')]")


class RegisterPopupComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "email_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][4]")
        }

        self._user_type_button = None
        self._manager_type_button = None
        self._google_button = None
        self._facebook_button = None
        self._lastname_input = None
        self._firstname_input = None
        self._phone_input = None
        self._email_input = None
        self._password_input = None
        self._password_confirmation_input = None
        self._registration_button = None

    @property
    def user_type_button(self) -> WebElement:
        if not self._user_type_button:
            self._user_type_button = self.node.find_element(*USER_TYPE_BUTTON)
        return self._user_type_button

    @property
    def manager_type_button(self) -> WebElement:
        if not self._manager_type_button:
            self._manager_type_button = self.node.find_element(*MANAGER_TYPE_BUTTON)
        return self._manager_type_button
    @property
    def google_button(self) -> WebElement:
        if not self._google_button:
            self._google_button = self.node.find_element(*GOOGLE_BUTTON)
        return self._google_button

    @property
    def facebook_button(self) -> WebElement:
        if not self._facebook_button:
            self._facebook_button = self.node.find_element(*FACEBOOK_BUTTON)
        return self._facebook_button

    @property
    def lastname_input(self) -> InputWithLabelIconsErrors:
        if not self._lastname_input:
            self._lastname_input = InputWithLabelIconsErrors(self.node.find_element(*LASTNAME_INPUT))
        return self._lastname_input
    @property
    def first_input(self) -> InputWithLabelIconsErrors:
        if not self._firstname_input:
            self._firstname_input = InputWithLabelIconsErrors(self.node.find_element(*FIRSTNAME_INPUT))
        return self._firstname_input
    @property
    def phone_input(self) -> InputWithLabelIconsErrors:
        if not self._phone_input:
            self._phone_input = InputWithLabelIconsErrors(self.node.find_element(*PHONE_INPUT))
        return self._phone_input

    @property
    def email_input(self) -> InputWithLabelIconsErrors:
        # if not self._email_input:
        #     self._email_input = InputWithLabelIconsErrors(self.node.find_element(*EMAIL_INPUT))
        return InputWithLabelIconsErrors(self.node.find_element(*self.locators["email_input"]))

    @property
    def password_input(self) -> InputWithLabelIconsErrors:
        if not self._password_input:
            self._password_input = InputWithLabelIconsErrors(self.node.find_element(*PASSWORD_INPUT))
        return self._password_input

    @property
    def password_confirmation_input(self) -> InputWithLabelIconsErrors:
        if not self._password_confirmation_input:
            self._password_confirmation_input = InputWithLabelIconsErrors(self.node.find_element(*PASSWORD_CONFIRMATION_INPUT))
        return self._password_confirmation_input

    @property
    def registration_button(self) -> InputWithLabelIconsErrors:
        if not self._registration_button:
            self._registration_button = self.node.find_element(*REGISTRATION_BUTTON)
        return self._registration_button

    def click_user_button(self) -> 'RegisterPopupComponent':
        self.user_type_button.click()
        return self

    def click_manager_button(self) -> 'RegisterPopupComponent':
        self.manager_type_button.click()
        return self

    def register(self):
        self.registration_button.click()