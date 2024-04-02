from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from src.ui.components.base_component import BaseComponent


class BasePopUp(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "close_button": ("xpath", ".//button[@class='ant-modal-close']")
        }

    def wait_popup_open(self, seconds: int) -> None:
        self.get_wait(seconds).until(EC.visibility_of(self.node))

    def is_open(self) -> bool:
        return self.node.is_displayed()

    def click_close_button(self) -> None:
        self.close_button.click_button()
