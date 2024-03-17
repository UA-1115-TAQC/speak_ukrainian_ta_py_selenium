from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement

STEP_ICON = (By.XPATH, ".//div[@class='ant-steps-item-icon']")
STEP_SUCCESS_ICON = (By.XPATH, ".//span[contains(@class, 'steps-finish-icon')")
STEP_TITLE = (By.XPATH, ".//div[@class='ant-steps-item-title']")


class PopUpStep(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._step_icon = None
        self._step_success_icon = None
        self._step_title = None

    @property
    def step_icon(self) -> WebElement:
        if not self._step_icon:
            self._step_icon = self.node.find_element(*STEP_ICON)
        return self._step_icon

    def get_step_icon_text(self) -> str:
        return self.step_icon.text

    @property
    def step_success_icon(self) -> WebElement:
        if not self._step_success_icon:
            self._step_success_icon = self.node.find_element(*STEP_SUCCESS_ICON)
        return self._step_success_icon

    @property
    def step_title(self) -> WebElement:
        if not self._step_title:
            self._step_title = self.node.find_element(*STEP_TITLE)
        return self._step_title

    def get_step_title_text(self) -> str:
        return self.step_title.text
