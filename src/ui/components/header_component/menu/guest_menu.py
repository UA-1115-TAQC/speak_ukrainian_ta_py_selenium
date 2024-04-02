from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent
from src.ui.components.login_pop_up_component.login_pop_up_component import LoginPopUpComponent
from src.ui.components.register_popup.register_popup_component import RegisterPopupComponent


class GuestMenu(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "login": ("xpath", ".//li[contains(@data-menu-id, 'login')]"),
            "registration": ("xpath", ".//li[contains(@data-menu-id, 'register')]"),
            "login_form": ("xpath", "//descendant::div[contains(@class, 'modal-login')][1]"),
            "registration_form": ("xpath", "//div[contains(@class, 'ant-modal-content')"
                                           " and contains(., 'Реєстрація')]")
        }
        self.wait = WebDriverWait(self.node, 10)

    def open_login_form(self) -> LoginPopUpComponent:
        self.wait.until(EC.element_to_be_clickable(self.login)).click()
        return LoginPopUpComponent(self.login_form)

    def open_registration_form(self) -> RegisterPopupComponent:
        self.wait.until(EC.element_to_be_clickable(self.registration)).click()
        return RegisterPopupComponent(self.registration_form)
