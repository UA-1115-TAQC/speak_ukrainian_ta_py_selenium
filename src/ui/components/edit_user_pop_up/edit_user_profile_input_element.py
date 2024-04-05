from typing import Self

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


LABEL = (By.XPATH, ".//label")
INPUT = (By.XPATH, ".//input")
VALIDATION_CIRCLE_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                                    "//span[contains(@class,'anticon-close-circle') "
                                    "or contains(@class,'anticon-check-circle')]")
ERROR_MESSAGES_LIST = (By.XPATH, ".//div[contains(@class,'ant-col')]"
                                 "//div[@class='ant-form-item-explain-error']")
LOADING_ERROR_MESSAGES_LIST = (By.XPATH, ".//div[contains(@class,'ant-col')]"
                                         "//div[contains(@class,'ant-form-item-explain-error')]")


class EditUserProfilePopupInputElement:

    def __init__(self, node: WebElement):
        self.node = node
        self.driver = node.parent
        self._label = None
        self._input = None
        self._validation_circle_icon = None
        self._error_msg_list = None
        self._loading_error_msg_list = None

    @property
    def edit_profile_input_label(self):
        if not self._label:
            self._label = self.node.find_element(*LABEL)
            return self._label

    def get_edit_profile_input_label_text(self) -> str:
        return self.edit_profile_input_label.text

    @property
    def edit_profile_input_value(self):
        return self.node.find_element(*INPUT)

    def get_edit_profile_input_value(self) -> str:
        return self.edit_profile_input_value.get_attribute("value")

    def set_edit_profile_input_value(self, value: str) -> None:
        self.edit_profile_input_value.send_keys(value)

    def clear_edit_profile_input(self) -> Self:
        self.edit_profile_input_value.click()
        (self.get_edit_profile_actions().key_down(Keys.CONTROL)
            .send_keys('a')
            .key_up(Keys.CONTROL)
            .send_keys(Keys.BACKSPACE)
            .perform())
        (self.get_edit_profile_actions().key_down(Keys.COMMAND)
            .send_keys('a')
            .key_up(Keys.COMMAND)
            .send_keys(Keys.BACKSPACE)
            .perform())
        return self

    @property
    def edit_profile_error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*ERROR_MESSAGES_LIST)

    def get_edit_profile_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.edit_profile_error_messages_list]

    @property
    def loading_edit_profile_error_messages_list_in_edit_user_profile(self) -> list[WebElement]:
        return self.node.find_elements(*LOADING_ERROR_MESSAGES_LIST)

    def clear_input_with_wait_in_edit_user_profile(self):
        self.clear_edit_profile_input()
        (self.get_edit_profile_wait(20)
             .until(lambda wd: not self.loading_edit_profile_error_messages_list_in_edit_user_profile[0]
                                        .get_attribute("style")))
        return self

    def get_edit_profile_actions(self):
        return ActionChains(self.driver)

    def get_edit_profile_wait(self, timeout: int):
        return WebDriverWait(self.driver, timeout)
