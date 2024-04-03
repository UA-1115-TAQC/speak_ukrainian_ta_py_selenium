from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.message_component import MessageComponent
from src.ui.pages.base_pages.base_page import BasePage


class MessagePage(BasePage):

    def __init__(self, driver: WebElement) -> None:
        super().__init__(driver)
        self.locators = {
            "search_input": ("xpath", ".//input[contains(@class, 'input') and @placeholder='Пошук...']"),
            "selected_item_dropdown": ("xpath", ".//span[contains(@class, 'selection-item')]"),

            "dropdown": ("xpath", ".//div[contains(@class, 'select-dropdown')]"),
            "new_first_item_dropdown": ("xpath", ".//div[contains(@id, 'rc_select_2_list_0')]"),
            "old_first_item_dropdown": ("xpath", ".//div[contains(@id, 'rc_select_2_list_1')]"),
            "show_unread_message_title": ("xpath", ".//span[text()='Показати тільки непрочитані повідомлення: ']"),
            "show_unanswered_message_title": ("xpath", ".//span[text()='Повідомлення без відповіді: ']"),
            "unread_messages_switch": ("xpath", ".//span[text()='Показати тільки непрочитані повідомлення: "
                                                "']/following-sibling::button//span[@class='ant-switch-inner']"),
            "unanswered_messages_switch": ("xpath", ".//span[text()='Повідомлення без відповіді: "
                                                    "']/following-sibling::button//span[@class='ant-switch-inner']"),
            "no_message_title": ("xpath", ".//div[contains(@class, 'noMessages')]"),
            "message_elements": ("xpath", ".//ul[contains(@class, 'ant-list-items')]//div[contains(@class, 'collapse "
                                          "')]"),

        }

    def search_input_send_keys(self, keys):
        self.search_input.send_keys(keys)

    def selected_item_dropdown_click(self):
        self.selected_item_dropdown.click()

    def new_first_item_dropdown_click(self):
        self.new_first_item_dropdown.click()

    def old_first_item_dropdown_click(self):
        self.old_first_item_dropdown.click()

    def unread_messages_switch_click(self):
        self.unread_messages_switch.click()

    def unanswered_messages_switch_click(self):
        self.unanswered_messages_switch.click()

    @property
    def message_elements(self) -> list[WebElement]:
        return self.driver.find_elements(*self.locators["message_elements"])

    # todo here am I

    def get_message_elements(self):
        return [MessageComponent(el) for el in self.message_elements]
