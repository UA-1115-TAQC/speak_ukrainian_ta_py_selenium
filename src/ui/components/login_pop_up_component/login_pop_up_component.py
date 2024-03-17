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
        self.initialize_web_elements()

    def initialize_web_elements(self):
        self._password_input_element = self.node.find_element(PASSWORD_INPUT)
        self._email_input_element = self.node.find_element(EMAIL_INPUT)
        self._login_popup_title = self.node.find_element(LOGIN_POPUP_TITLE)
        self._google_icon = self.node.find_element(GOOGLE_ICON)
        self._facebook_icon = self.node.find_element(FACEBOOK_ICON)
        self._authorization_by_google = self.node.find_element(AUTHORIZATION_BY_GOOGLE)
        self._authorization_by_facebook = self.node.find_element(AUTHORIZATION_BY_FACEBOOK)
        self._label_or = self.node.find_element(LABEL_OR)
        self._submit_button = self.node.find_element(SUBMIT_BUTTON)
        self._restore_password_button = self.node.find_element(RESTORE_PASSWORD_BUTTON)
        self._restore_password_popup = self.node.find_element(RESTORE_PASSWORD_POPUP)

    def login_pop_up_tittle(self) -> WebElement:
        return self._login_popup_title

    def get_menu_header_text(self) -> str:
        return self.login_popup_title.get_attribute("textContent")

    def get_authorization_label_text_or(self) -> str:
        return self._label_or.get_attribute("textContent")

    def password_input_element(self) -> InputWithIconElement:
        return self._password_input_element

    def email_input_element(self) -> InputWithIconElement:
        return self._email_input_element

    def enter_email(self, email):
        self._email_input_element.send_keys(email)
        return self

    def enter_password(self, password):
        self._password_input_element.send_keys(password)
        return self

    @property
    def login_popup_title(self) -> WebElement:
        return self._login_popup_title

    @property
    def google_icon(self) -> WebElement:
        return self._google_icon

    @property
    def facebook_icon(self) -> WebElement:
        return self._facebook_icon

    @property
    def authorization_by_google(self) -> WebElement:
        return self._authorization_by_google

    @property
    def authorization_by_facebook(self) -> WebElement:
        return self._authorization_by_facebook

    @property
    def label_or_text(self) -> WebElement:
        return self._label_or

    def click_submit_button(self) -> None:
        self._submit_button.click()

    def click_restore_password_button(self) -> None:
        self._restore_password_button.click()

    def get_restore_password_popup(self):  # TODO
        return self._restore_password_popup
