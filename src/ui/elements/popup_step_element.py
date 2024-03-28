from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.base_element import BaseElement


class PopUpStep(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "step_icon": ("xpath", ".//div[@class='ant-steps-item-icon']"),
            "step_success_icon": ("xpath", ".//span[contains(@class, 'ant-steps-finish-icon')]"),
            "step_title": ("xpath", ".//div[@class='ant-steps-item-title']")
        }

    def get_step_icon_text(self) -> str:
        return self.step_icon.text

    def get_step_title_text(self) -> str:
        return self.step_title.text
