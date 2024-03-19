from typing import Self

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.elements.base_element import BaseElement

PAPER_CLIP_ICON = (By.XPATH, ".//span[(@role='img') and (@aria-label='paper-clip')]")
IMAGE_TITLE = (By.XPATH, ".//span[@class='ant-upload-list-item-name']")
REMOVE_IMAGE_BUTTON = (By.XPATH, ".//button[(@title='Remove file') and (@type='button')]")
UPLOAD_ERROR = (By.XPATH, ".//div[@class='ant-tooltip-inner']")
PREVIEW_FILE = (By.XPATH, ".//a[@title='Preview file']")
PREVIEW_ICON = (By.XPATH, ".//span[(@role='img') and (@aria-label='eye')]")
CLOSE_BUTTON = (By.XPATH, "//descendant::button[(@type='button') and (@aria-label='Close')][3]")
UPLOAD_DONE = (By.XPATH, ".//div[contains(@class,'ant-upload-list-item-done')]")


class UploadedImageElement(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._paper_clip_icon = None
        self._image_title = None
        self._remove_img_button = None
        self._upload_error = None
        self._preview_file = None
        self._preview_icon = None
        self._close_button = None
        self._upload_done = None

    @property
    def paper_clip_icon(self) -> WebElement:
        if not self._paper_clip_icon:
            self._paper_clip_icon = self.node.find_element(*PAPER_CLIP_ICON)
        return self._paper_clip_icon

    @property
    def image_title(self) -> WebElement:
        if not self._image_title:
            self._image_title = self.node.find_element(*IMAGE_TITLE)
        return self._image_title

    @property
    def remove_img_button(self) -> WebElement:
        if not self._remove_img_button:
            self._remove_img_button = self.node.find_element(*REMOVE_IMAGE_BUTTON)
        return self._remove_img_button

    @property
    def upload_error(self) -> WebElement:
        if not self._upload_error:
            self._upload_error = self.node.find_element(*UPLOAD_ERROR)
        return self._upload_error

    @property
    def preview_file(self) -> WebElement:
        if not self._preview_file:
            self._preview_file = self.node.find_element(*PREVIEW_FILE)
        return self._preview_file

    def click_preview_file(self) -> Self:
        self.preview_file.click()
        return self

    @property
    def preview_icon(self) -> WebElement:
        if not self._preview_icon:
            self._preview_icon = self.node.find_element(*PREVIEW_FILE)
        return self._preview_icon

    @property
    def close_button(self) -> WebElement:
        if not self._close_button:
            self._close_button = self.node.find_element(*CLOSE_BUTTON)
        return self._close_button

    def click_close_button(self) -> Self:
        self.close_button.click()
        return self

    @property
    def upload_done(self) -> WebElement:
        if not self._upload_done:
            self._upload_done = self.node.find_element(*UPLOAD_DONE)
        return self._upload_done

    def wait_image_loaded(self, timeout: int) -> Self:
        WebDriverWait(self.node.parent, timeout).until(lambda d: self.upload_done.is_displayed())
        return self

    def wait_image_changed(self, prev_img: str, timeout: int) -> Self:
        wait = WebDriverWait(self.node.parent, timeout)
        wait.until(lambda d: self.image_title.text != prev_img)
        wait.until(lambda d: self.upload_done.is_displayed())
        return self
