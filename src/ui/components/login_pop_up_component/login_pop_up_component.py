from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp
from src.ui.components.login_pop_up_component.restoration_password_component import RestorationPasswordComponent
from src.ui.elements.input import Input
from src.ui.elements.input_with_icon_element import InputWithIconElement

LOGIN_POPUP_TITLE = (By.XPATH, "./descendant::div[@class='login-header']")
GOOGLE_ICON = (By.XPATH, "./descendant::img[contains(@src, 'google')]")
FACEBOOK_ICON = (By.XPATH, "./descendant::img[contains(@src, 'facebook')]")
AUTHORIZATION_BY_GOOGLE = (By.XPATH, "./descendant::a[contains(@href, 'authorize/google')]")
AUTHORIZATION_BY_FACEBOOK = (By.XPATH, "./descendant::a[contains(@href, 'authorize/facebook')]")
LABEL_OR = (By.XPATH, "./descendant::span[contains(@class, 'label-or')]")
EMAIL_TITLE = (By.XPATH, "./descendant::label[@title='Емейл']")
PASSWORD_TITLE = (By.XPATH, "./descendant::label[@title='Пароль']")
SUBMIT_BUTTON = (By.XPATH, "./descendant::button[@type='submit']")
RESTORE_PASSWORD_BUTTON = (By.XPATH, "./descendant::a[contains(@class, 'restore-password-button')]")
RESTORE_PASSWORD_POPUP = (By.XPATH, "//body/descendant::div[contains(@class, 'modal-login')][2]")
EMAIL_INPUT = (By.XPATH, "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][1]")
PASSWORD_INPUT = (By.XPATH, "./descendant::div[contains(@class, 'ant-form-item login-input css-13m256z')][2]")


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
        self._email_title = None
        self._password_title = None
        self._submit_button = None
        self._restore_password_button = None
        self._restore_password_popup = None

    def password_input_element(self) -> InputWithIconElement:
        if not self._password_input_element:
            self._password_input_element = InputWithIconElement(self.node.find_element(*PASSWORD_INPUT))
        return self._password_input_element

    def email_input_element(self) -> InputWithIconElement:
        if not self._email_input_element:
            self._email_input_element = InputWithIconElement(self.node.find_element(*EMAIL_INPUT))
        return self._email_input_element

    def enter_email(self, email) -> Input:
        return self._email_input_element.send_keys(email)

    def enter_password(self, password) -> Input:
        return self._password_input_element.send_keys(password)

    @property
    def login_pop_up_tittle(self) -> WebElement:
        if not self._login_popup_title:
            self._login_popup_title = self.node.find_element(*LOGIN_POPUP_TITLE)
        return self._login_popup_title

    @property
    def google_icon(self) -> WebElement:
        if not self._google_icon:
            self._google_icon = self.node.find_element(*GOOGLE_ICON)
        return self._google_icon

    @property
    def facebook_icon(self) -> WebElement:
        if not self._facebook_icon:
            self._facebook_icon = self.node.find_element(*FACEBOOK_ICON)
        return self._facebook_icon

    @property
    def authorization_by_google(self) -> WebElement:
        if not self._authorization_by_google:
            self._authorization_by_google = self.node.find_element(*AUTHORIZATION_BY_GOOGLE)
        return self._authorization_by_google

    @property
    def authorization_by_facebook(self) -> WebElement:
        if not self._authorization_by_facebook:
            self._authorization_by_facebook = self.node.find_element(*AUTHORIZATION_BY_FACEBOOK)
        return self._authorization_by_facebook

    @property
    def label_or_title(self) -> WebElement:
        if not self._label_or:
            self._label_or = self.node.find_element(*LABEL_OR)
        return self._label_or

    @property
    def email_title(self) -> WebElement:
        if not self._email_title:
            self._email_title = self.node.find_element(*EMAIL_TITLE)
        return self._email_title

    @property
    def password_title(self) -> WebElement:
        if not self._password_title:
            self._password_title = self.node.find_element(*PASSWORD_TITLE)
        return self._password_title

    def get_email_text(self) -> str:
        return self.email_title.text

    def get_password_text(self) -> str:
        return self.password_title.text

    def click_submit_button(self) -> None:
        self.node.find_element(*SUBMIT_BUTTON).click()

    def restore_password_component(self) -> RestorationPasswordComponent:
        if not self._restore_password_popup:
            self._restore_password_popup = RestorationPasswordComponent(self.node.find_element(*RESTORE_PASSWORD_POPUP))
        return self._restore_password_popup

    def click_restore_password_button(self) -> RestorationPasswordComponent:
        self._restore_password_button.click()
        return self.restore_password_component()
