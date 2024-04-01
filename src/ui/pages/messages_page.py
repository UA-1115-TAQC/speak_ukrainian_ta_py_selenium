from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.message_component import MessageComponent
from src.ui.pages.base_pages.base_page import BasePage

class MessagePage(BasePage):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
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
            "message_elements": ("xpath", ".//ul[contains(@class, 'ant-list-items')]//div[contains(@class, 'collapse ')]"),
        }

    @property
    def search_input(self) -> WebElement:
        return self.node.find_elements(*self.locators["search_input"])

    def search_input_send_keys(self, keys):
        self.search_input.send_keys(keys)

    @property
    def selected_item_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["selected_item_dropdown"])

    def selected_item_dropdown_click(self):
        self.selected_item_dropdown.click()

    @property
    def dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["dropdown"])

    @property
    def new_first_item_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["new_first_item_dropdown"])

    def new_first_item_dropdown_click(self):
        self.new_first_item_dropdown.click()

    @property
    def old_first_item_dropdown(self) -> WebElement:
        return self.node.find_elements(*self.locators["old_first_item_dropdown"])

    def old_first_item_dropdown_click(self):
        self.old_first_item_dropdown.click()

    @property
    def show_unread_message_title(self) -> WebElement:
        return self.node.find_elements(*self.locators["show_unread_message_title"])

    @property
    def show_unanswered_message_title(self) -> WebElement:
        return self.node.find_elements(*self.locators["old_first_item_dropdown"])


    @property
    def unread_messages_switch(self) -> WebElement:
        return self.node.find_elements(*self.locators["unread_messages_switch"])

    def unread_messages_switch_click(self):
        self.unread_messages_switch.click()

    @property
    def unanswered_messages_switch(self) -> WebElement:
        return self.node.find_elements(*self.locators["unanswered_messages_switch"])

    def unanswered_messages_switch_click(self):
        self.unanswered_messages_switch.click()

    @property
    def no_message_title(self) -> WebElement:
        return self.node.find_elements(*self.locators["no_message_title"])

    @property
    def message_elements(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["message_elements"])

    #todo отут помилка отримується WebElement, а не list

    def get_message_elements(self):
        return [MessageComponent(el) for el in self.message_elements]
