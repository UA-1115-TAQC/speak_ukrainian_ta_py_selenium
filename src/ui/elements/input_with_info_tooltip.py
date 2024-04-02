from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors


class InputWithInfoTooltip(InputWithLabelIconsErrors):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            **self.locators,
            "info_icon": ("xpath", ".//div[@class='ant-form-item-control-input']//span[@aria-label='info-circle']"),
            "info_icon_tooltip": ("xpath", "//div[contains(@class, 'ant-tooltip ') "
                                           "and not(contains(@class, 'ant-tooltip-hidden'))]"
                                           "//div[@class='ant-tooltip-inner']")
        }

    def click_info_icon(self) -> WebElement:
        self.info_icon.click_button()
        return self.info_icon_tooltip

    def get_info_icon_tooltip_text(self) -> str:
        return self.info_icon_tooltip.get_attribute("innerText")
