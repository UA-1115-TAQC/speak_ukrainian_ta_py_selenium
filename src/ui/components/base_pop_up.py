from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent

CLOSE_BUTTON = (By.XPATH, ".//button[@class='ant-modal-close']")


class BasePopUp(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._close_button = None

    def wait_popup_open(self, seconds: int) -> None:
        wait = WebDriverWait(self.node.parent, seconds)
        wait.until(lambda d: self.node.is_displayed())

    def is_open(self) -> bool:
        return self.node.is_displayed()

    def close(self) -> None:
        self._close_button.click()
