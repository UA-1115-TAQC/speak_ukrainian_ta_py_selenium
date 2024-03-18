from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors

INFO_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                       "/descendant::span[contains(@class,'anticon-check-circle')]")
INFO_ICON_TOOLTIP = (By.XPATH, "//div[contains(@class, 'ant-tooltip ') and not(contains(@class, 'ant-tooltip-hidden'))]"
                               "//div[@class='ant-tooltip-inner']")


class InputWithInfoTooltip(InputWithLabelIconsErrors):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._info_icon = None

    @property
    def info_icon(self) -> WebElement:
        if not self._info_icon:
            self._info_icon = self.node.find_element(*INFO_ICON)
        return self._info_icon

    def click_info_icon(self) -> WebElement:
        return self.info_icon_tooltip

    @property
    def info_icon_tooltip(self) -> WebElement:
        return self.node.find_element(*INFO_ICON_TOOLTIP)

    def get_info_icon_tooltip_text(self) -> str:
        return self.info_icon_tooltip.get_attribute("innerText")
