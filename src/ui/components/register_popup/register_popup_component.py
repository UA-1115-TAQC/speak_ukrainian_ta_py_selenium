from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors


class RegisterPopupComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "lastname_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][1]"),
            "firstname_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][2]"),
            "phone_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][3]"),
            "email_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][4]"),
            "password_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][5]"),
            "password_confirmation_input": ("xpath", ".//div[contains(@class, 'ant-form-item registration-input')][6]"),
            "user_type_button": ("xpath", "//input[@value='ROLE_USER']/../.."),
            "manager_type_button": ("xpath", "//input[@value='ROLE_MANAGER']/../.."),
            "google_button": ("xpath", "//a[contains(@href, 'google')]"),
            "facebook_button": ("xpath", "//a[contains(@href, 'facebook')]"),
            "registration_button": ("xpath", ".//button[contains(@class, 'registration-button')]"),
        }

    def click_user_type_button(self) -> 'RegisterPopupComponent':
        return self.user_type_button.click_button()

    def click_manager_type_button(self) -> 'RegisterPopupComponent':
        return self.manager_type_button.click_button()

    def click_google_button(self) -> 'RegisterPopupComponent':
        self.google_button.click_button()
        return self

    @property
    def click_facebook_button(self) -> 'RegisterPopupComponent':
        self.facebook_button.click_button()
        return self

    @property
    def lastname_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.lastname_input)

    @property
    def firstname_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.firstname_input)

    @property
    def phone_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.phone_input)

    @property
    def email_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.email_input)

    @property
    def password_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.password_input)

    @property
    def password_confirmation_input_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.password_confirmation_input)

    def click_user_button(self) -> 'RegisterPopupComponent':
        self.user_type_button.click_button()
        return self

    def click_manager_button(self) -> 'RegisterPopupComponent':
        self.manager_type_button.click_button()
        return self

    def register(self):
        self.registration_button.click_button()
