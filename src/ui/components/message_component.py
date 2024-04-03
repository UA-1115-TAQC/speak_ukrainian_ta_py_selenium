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

    def arrow_icon_click(self):
        self.arrow_icon.click()

    def message_delete_icon_click(self):
        self.message_delete_icon.click()

    def answer_button_click(self):
        self.answer_button.click()
