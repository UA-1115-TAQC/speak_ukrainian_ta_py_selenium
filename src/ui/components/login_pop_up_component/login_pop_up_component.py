from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.input_with_icon_element import InputWithIconElement

LOGIN_POPUP_TITLE = "./descendant::div[@class='login-header']"
GOOGLE_ICON = "./descendant::img[contains(@src, 'google')]"
FACEBOOK_ICON = "./descendant::img[contains(@src, 'facebook')]"
AUTHORIZATION_BY_GOOGLE = "./descendant::a[contains(@href, 'authorize/google')]"
AUTHORIZATION_BY_FACEBOOK = "./descendant::a[contains(@href, 'authorize/facebook')]"
LABEL_OR = "./descendant::span[contains(@class, 'label-or')]"
SUBMIT_BUTTON = "./descendant::button[@type='submit']"
RESTORE_PASSWORD_BUTTON = "./descendant::a[contains(@class, 'restore-password-button')]"
RESTORE_PASSWORD_POPUP = "//body/descendant::div[contains(@class, 'modal-login')][2]"
EMAIL_INPUT = "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][1]"
PASSWORD_INPUT = "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][2]"


class LoginPopUpComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._password_input_element = None
        self._email_input_element = None
        self._login_popup_title = None
        self._google_icon = None
        self._facebook_icon = None
        self._authorization_by_google = None
        self._authorization_by_facebook = None
        self._label_or = None
        self._submit_button = None
        self._restore_password_button = None
        self._restore_password_popup = None

    def password_input_element(self) -> InputWithIconElement:  # TODO
        return self._password_input_element

    def email_input_element(self) -> InputWithIconElement:  # TODO
        return self._email_input_element

    def enter_email(self, email):  # TODO
        self._email_input_element.send_keys(email)
        return self

    def enter_password(self, password):  # TODO
        self._password_input_element.send_keys(password)
        return self

    @property
    def login_pop_up_tittle(self) -> WebElement:
        if not self._login_popup_title:
            self._login_popup_title = self.node.find_element(LOGIN_POPUP_TITLE)
        return self._login_popup_title

    @property
    def google_icon(self) -> WebElement:
        if not self._google_icon:
            self._google_icon = self.node.find_element(GOOGLE_ICON)
        return self._google_icon

    @property
    def facebook_icon(self) -> WebElement:
        if not self._facebook_icon:
            self._facebook_icon = self.node.find_element(FACEBOOK_ICON)
        return self._facebook_icon

    @property
    def authorization_by_google(self) -> WebElement:
        if not self._authorization_by_google:
            self._authorization_by_google = self.node.find_element(AUTHORIZATION_BY_GOOGLE)
        return self._authorization_by_google

    @property
    def authorization_by_facebook(self) -> WebElement:
        if not self._authorization_by_facebook:
            self._authorization_by_facebook = self.node.find_element(AUTHORIZATION_BY_FACEBOOK)
        return self._authorization_by_facebook

    @property
    def label_or_title(self) -> WebElement:
        if not self._label_or:
            self._label_or = self.node.find_element(LABEL_OR)
        return self._label_or

    def click_submit_button(self) -> None:
        self._submit_button.click()

    def click_restore_password_button(self) -> None:
        self._restore_password_button.click()

    def get_restore_password_popup(self):  # TODO
        return self._restore_password_popup
