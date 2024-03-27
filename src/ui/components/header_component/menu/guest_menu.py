from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent
from src.ui.components.login_pop_up_component.login_pop_up_component import LoginPopUpComponent
from src.ui.components.register_popup.register_popup_component import RegisterPopupComponent

LOGIN = (By.XPATH, ".//li[contains(@data-menu-id, 'login')]")
REGISTRATION = (By.XPATH, ".//li[contains(@data-menu-id, 'register')]")
LOGIN_FORM = (By.XPATH, "//descendant::div[contains(@class, 'modal-login')][1]")
REGISTRATION_FORM = (By.XPATH, "//div[contains(@class, 'ant-modal-content') and contains(., 'Реєстрація')]")


class GuestMenu(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.wait = WebDriverWait(self.node, 10)

    def open_login_form(self) -> LoginPopUpComponent:
        self.wait.until(expected_conditions.element_to_be_clickable(self.node.find_element(*LOGIN))).click()
        return LoginPopUpComponent(self.node.find_element(*LOGIN_FORM))

    def open_registration_form(self) -> RegisterPopupComponent:
        self.wait.until(expected_conditions.element_to_be_clickable(self.node.find_element(*REGISTRATION))).click()
        return RegisterPopupComponent(self.node.find_element(*REGISTRATION_FORM))
