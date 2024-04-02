from typing import Self

from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement


class GalleryImageElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.locators = {
            "gallery_image_preview": ("xpath", ".//a[@title='Preview file']"),
            "gallery_image_name": ("xpath", ".//span[@class='ant-upload-list-item-name']"),
            "gallery_actions_container": ("xpath", ".//span[@class='ant-upload-list-item-actions']"),
            "gallery_image_preview_icon": ("xpath", ".//span[(@role='img') and (@aria-label='eye')]"),
            "gallery_image_delete_icon": ("xpath", ".//span[(@role='img') and (@aria-label='delete')]"),
            "gallery_image_error": ("xpath", ".//div[@class='ant-tooltip-inner']"),
            "preview_close_button": ("xpath", "//button[@class='ant-modal-close']")
        }

    def click_image_preview_icon(self) -> Self:
        self.gallery_actions_container.hover()
        self.gallery_image_preview_icon.click_button()
        return self

    def click_preview_close_button(self) -> Self:
        self.node.find_elements(*self.locators["preview_close_button"]).pop().click()
        return self

    def click_image_delete_icon(self) -> Self:
        self.gallery_actions_container.hover()
        self.gallery_image_delete_icon.click_button()
        return self

    def click_image_container(self) -> Self:
        self.node.click()
        return self
