from typing import Self
from selenium.webdriver.remote.webelement import WebElement
from src.ui.elements.base_element import BaseElement


class UploadedImageElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "paper_clip_icon": ("xpath", ".//span[(@role='img') and (@aria-label='paper-clip')]"),
            "image_title": ("xpath", ".//span[@class='ant-upload-list-item-name']"),
            "delete_image_button": ("xpath", ".//button[(@title='remove file') and (@type='button')]"),
            "upload_error": ("xpath", ".//div[@class='ant-tooltip-inner']"),
            "upload_done": ("xpath", ".//div[contains(@class,'ant-upload-list-item-done')]")
        }

    def click_delete_button(self) -> Self:
        self.delete_image_button.click_button()
        return self

    @property
    def error_tooltip(self) -> WebElement:
        self.image_title.click()
        return self.upload_error

    def get_error_tooltip_text(self) -> str:
        return self.error_tooltip.text

    def wait_image_loaded(self, timeout: int) -> Self:
        self.upload_done.visibility_of_element_located(timeout)
        return self

    def wait_image_changed(self, prev_img: str, timeout: int) -> Self:
        self.get_wait(timeout).until(lambda d: self.image_title.text != prev_img)
        self.upload_done.visibility_of_element_located()
        return self

    def get_image_title_text(self) -> str:
        return self.image_title.text

