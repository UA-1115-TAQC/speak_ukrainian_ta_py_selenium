from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.elements.base_element import BaseElement

GALLERY_IMAGE_PREVIEW = (By.XPATH, ".//a[@title='Preview file']")
GALLERY_IMAGE_NAME = (By.XPATH, ".//span[@class='ant-upload-list-item-name']")
GALLERY_IMAGE_PREVIEW_ICON = (By.XPATH, ".//span[(@role='img') and (@aria-label='eye')]")
GALLERY_IMAGE_DELETE_ICON = (By.XPATH, ".//span[(@role='img') and (@aria-label='delete')]")
GALLERY_IMAGE_ERROR = (By.XPATH, ".//div[@class='ant-tooltip-inner']")
PREVIEW_CLOSE_BUTTON = (By.XPATH, "//descendant::span[contains(@class,'ant-modal-close-icon')][2]")


class GalleryImageElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._image_preview = None
        self._image_name = None
        self._image_preview_icon = None
        self._image_delete_icon = None

    @property
    def image_preview(self) -> WebElement:
        if not self._image_preview:
            self._image_preview = self.node.find_element(*GALLERY_IMAGE_PREVIEW)
        return self._image_preview

    @property
    def image_name(self) -> WebElement:
        if not self._image_name:
            self._image_name = self.node.find_element(*GALLERY_IMAGE_NAME)
        return self._image_name

    @property
    def image_preview_icon(self) -> WebElement:
        if not self._image_preview_icon:
            self._image_preview_icon = self.node.find_element(*GALLERY_IMAGE_PREVIEW_ICON)
        return self._image_preview_icon

    def click_image_preview_icon(self) -> Self:
        self.image_preview_icon.click()
        return self

    @property
    def preview_close_button(self) -> WebElement:
        return self.node.find_element(*PREVIEW_CLOSE_BUTTON)

    def click_preview_close_button(self) -> Self:
        self.preview_close_button.click()
        return self

    @property
    def image_delete_icon(self) -> WebElement:
        if not self._image_delete_icon:
            self._image_delete_icon = self.node.find_element(*GALLERY_IMAGE_DELETE_ICON)
        return self._image_delete_icon

    def click_image_delete_icon(self) -> Self:
        self.image_delete_icon.click()
        return self

    @property
    def image_error(self) -> WebElement:
        return self.node.find_element(*GALLERY_IMAGE_ERROR)

    def click_image_container(self) -> Self:
        self.node.click()
        return self
