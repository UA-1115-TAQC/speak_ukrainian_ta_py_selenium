from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent
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


class LoginPopUpComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.password_input_element = None
        self.email_input_element = None
        self.login_popup_title = None
        self.google_icon = None
        self.facebook_icon = None
        self.authorization_by_google = None
        self.authorization_by_facebook = None
        self.label_or = None
        self.submit_button = None
        self.restore_password_button = None
        self.restore_password_popup = None
        self.initialize_web_elements()

    def initialize_web_elements(self):
        self.password_input_element = self.node.find_element(PASSWORD_INPUT)
        self.email_input_element = self.node.find_element(EMAIL_INPUT)
        self.login_popup_title = self.node.find_element(LOGIN_POPUP_TITLE)
        self.google_icon = self.node.find_element(GOOGLE_ICON)
        self.facebook_icon = self.node.find_element(FACEBOOK_ICON)
        self.authorization_by_google = self.node.find_element(AUTHORIZATION_BY_GOOGLE)
        self.authorization_by_facebook = self.node.find_element(AUTHORIZATION_BY_FACEBOOK)
        self.label_or = self.node.find_element(LABEL_OR)
        self.submit_button = self.node.find_element(SUBMIT_BUTTON)
        self.restore_password_button = self.node.find_element(RESTORE_PASSWORD_BUTTON)
        self.restore_password_popup = self.node.find_element(RESTORE_PASSWORD_POPUP)

    def get_menu_header_text(self) -> str:
        return self.login_popup_title.get_attribute("textContent")

    def get_authorization_label_text_or(self) -> str:
        return self.label_or.get_attribute("textContent")

    @property
    def password_input_element(self) -> InputWithIconElement:
        return self.password_input_element

    @property
    def email_input_element(self) -> InputWithIconElement:
        return self.email_input_element

    @email_input_element.setter
    def enter_email(self, mail_input : InputWithIconElement):

        return self

    def enter_password(self, password):
        self.password_input_element.send_keys(password)
        return self

    @property
    def login_popup_title(self) -> WebElement:
        return self.login_popup_title

    @property
    def google_icon(self) -> WebElement:
        return self.google_icon

    @property
    def facebook_icon(self) -> WebElement:
        return self.facebook_icon

    @property
    def authorization_by_google(self) -> WebElement:
        return self.authorization_by_google

    @property
    def authorization_by_facebook(self) -> WebElement:
        return self.authorization_by_facebook

    @property
    def label_or_text(self) -> WebElement:
        return self.label_or

    def click_submit_button(self) -> None:
        self.submit_button.click()

    def click_restore_password_button(self) -> None:
        self.restore_password_button.click()

    def get_restore_password_popup(self):  # TODO
        return self.restore_password_popup
