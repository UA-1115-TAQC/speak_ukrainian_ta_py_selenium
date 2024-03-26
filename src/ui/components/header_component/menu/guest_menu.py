from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent
from src.ui.components.login_pop_up_component.login_pop_up_component import LoginPopUpComponent

LOGIN = (By.XPATH, ".//li[contains(@data-menu-id, 'login')]")
REGISTRATION = (By.XPATH, ".//li[contains(@data-menu-id, 'register')]")
LOGIN_FORM = (By.XPATH, "//descendant::div[contains(@class, 'modal-login')][1]")
REGISTRATION_FORM = (By.XPATH, "//div[contains(@class, 'ant-modal-content') and contains(., 'Реєстрація')]")


class GuestMenu(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)

    def open_login_form(self) -> LoginPopUpComponent:
        self.get_wait(10).until(EC.element_to_be_clickable(LOGIN)).click()
        return LoginPopUpComponent(self.node.find_element(*LOGIN_FORM))

    def open_registration_form(self) -> None:  # TODO
        WebDriverWait(self.node, 10).until(EC.element_to_be_clickable(*REGISTRATION)).click()
