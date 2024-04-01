from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent


class MessageComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "arrow_icon": ("xpath", ".//div[contains(@class, 'collapse-expand-icon')]"),
            "message_header": ("xpath", ".//span[contains(@class, 'header-text')]"),

            "date_title": ("xpath", ".//div[contains(@class, 'date')]"),
            "message_status_icon": ("xpath", ".//span[contains(@aria-label, 'circle')]"),
            "message_delete_icon": ("xpath", ".//span[contains(@aria-label, 'delete')]"),
            "user_avatar": ("xpath", ".//descendant::span[contains(@class, 'avatar-circle')]"),
            "user_name": ("xpath", ".//div[contains(@class, 'userName')]"),
            "message_text": ("xpath", ".//div[@class='ant-collapse-content-box']"),
            "answer_button": ("xpath", ".//button[contains(@class, 'btn')]"),
        }

    def message_text_get_text(self):
        full_text = self.message_text.text
        reply_button = self.message_text.find_element_by_xpath("./descendant::button")
        button_text = reply_button.text
        return full_text.replace(button_text, "").strip()

    @property
    def arrow_icon(self) -> WebElement:
        return self.node.find_elements(*self.locators["arrow_icon"])

    def arrow_icon_click(self):
        self.arrow_icon.click()

    @property
    def message_header(self) -> WebElement:
        return self.node.find_elements(*self.locators["message_header"])

    @property
    def date_title(self) -> WebElement:
        return self.node.find_elements(*self.locators["date_title"])

    @property
    def message_status_icon(self) -> WebElement:
        return self.node.find_elements(*self.locators["message_status_icon"])

    @property
    def message_delete_icon(self) -> WebElement:
        return self.node.find_elements(*self.locators["message_delete_icon"])

    def message_delete_icon_click(self):
        self.message_delete_icon.click()

    @property
    def user_avatar(self) -> WebElement:
        return self.node.find_elements(*self.locators["user_avatar"])

    @property
    def user_name(self) -> WebElement:
        return self.node.find_elements(*self.locators["user_name"])

    @property
    def message_text(self) -> WebElement:
        return self.node.find_elements(*self.locators["message_text"])

    @property
    def answer_button(self) -> WebElement:
        return self.node.find_elements(*self.locators["answer_button"])

    def answer_button_click(self):
        self.answer_button.click()
