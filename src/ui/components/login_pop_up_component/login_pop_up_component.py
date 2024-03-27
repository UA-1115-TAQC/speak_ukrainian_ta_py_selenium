from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.components.login_pop_up_component.restoration_password_component import RestorationPasswordComponent
from src.ui.elements.input_with_icon_element import InputWithIconElement


class LoginPopUpComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "login_popup_title": ("xpath", "./descendant::div[@class='login-header']"),
            "google_icon": ("xpath", "./descendant::img[contains(@src, 'google')]"),
            "facebook_icon": ("xpath", "./descendant::img[contains(@src, 'facebook')]"),
            "authorization_by_google": ("xpath", "./descendant::a[contains(@href, 'authorize/google')]"),
            "authorization_by_facebook": ("xpath", "./descendant::a[contains(@href, 'authorize/facebook')]"),
            "label_or_title": ("xpath", "./descendant::span[contains(@class, 'label-or')]"),
            "email_title": ("xpath", "./descendant::label[@title='Емейл']"),
            "password_title": ("xpath", "./descendant::label[@title='Пароль']"),
            "submit_button": ("xpath", "./descendant::button[@type='submit']"),
            "restore_password_button": ("xpath", "./descendant::a[contains(@class, 'restore-password-button')]"),
            "restore_password_popup": ("xpath", "//body/descendant::div[contains(@class, 'modal-login')][2]"),
            "email_input": ("xpath", "./descendant::div[contains(@class,"
                                     " 'ant-form-item login-input css-13m256z')][1]"),
            "password_input": ("xpath", "./descendant::div[contains(@class,"
                                        " 'ant-form-item login-input css-13m256z')][2]")
        }

    @property
    def password_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.password_input)

    @property
    def email_input_element(self) -> InputWithIconElement:
        return InputWithIconElement(self.email_input)

    def enter_email(self, email: str) -> None:
        self.email_input_element.set_input_value(email)

    def enter_password(self, password) -> None:
        self.password_input_element.set_input_value(password)

    def get_email_title(self) -> str:
        return self.email_title.text

    def get_password_title(self) -> str:
        return self.password_title.text

    def get_label_or_title(self) -> str:
        return self.label_or_title.text

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def open_restoration_password_pop_up(self) -> 'RestorationPasswordComponent':
        self.restore_password_button.click()
        from src.ui.components.login_pop_up_component.restoration_password_component import RestorationPasswordComponent
        return RestorationPasswordComponent(self.restore_password_popup)
