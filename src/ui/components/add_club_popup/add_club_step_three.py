from typing import Self

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent
from src.ui.elements.gallery_image_element import GalleryImageElement
from src.ui.elements.uploaded_image_element import UploadedImageElement

CLUB_POPUP_TITLE = (By.XPATH, ".//div[contains(@class,'add-club-header')]")
COMPLETE_BUTTON = (By.XPATH, ".//button[contains(@class,'add-club-content-next')]")
PREVIOUS_STEP_BUTTON = (By.XPATH, ".//button[contains(@class,'add-club-content-prev')]")
CLUB_LOGO_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][1]")
LOGO_DOWNLOAD_BUTTON = (By.XPATH, "./descendant::span[(@class='ant-upload') and (@role='button')][1]")
LOGO_DOWNLOAD_INPUT = (By.XPATH, ".//input[@id='basic_urlLogo']")
LOGO_UPLOADED_IMG_CONTAINER = (By.XPATH, "./descendant::div[@class='ant-upload-list ant-upload-list-text'][1]")
CLUB_COVER_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][2]")
COVER_DOWNLOAD_BUTTON = (By.XPATH, "./descendant::span[(@class='ant-upload') and (@role='button')][2]")
COVER_DOWNLOAD_INPUT = (By.XPATH, ".//input[@id='basic_urlBackground']")
COVER_UPLOADED_IMG_CONTAINER = (By.XPATH, "/descendant::div[@class='ant-upload-list ant-upload-list-text'][2]")
CLUB_GALLERY_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][3]")
GALLERY_DOWNLOAD_BUTTON = (By.XPATH, "./descendant::span[(@class='ant-upload') and (@role='button')][3]")
GALLERY_DOWNLOAD_INPUT = (By.XPATH, "./descendant::span[(@class='ant-upload') and (@role='button')][3]//input")
GALLERY_IMAGE_CONTAINER = (By.XPATH, "//span[contains(@class,'ant-upload-picture-card-wrapper')]"
                                     "//div[@class='ant-upload-list-item-container']")
DESCRIPTION_TITLE = (By.XPATH, "./descendant::span[contains(@class,'ant-typography')][4]")
DESCRIPTION_TEXTAREA = (By.XPATH, ".//textarea[contains(@id,'basic_description')]")
TEXTAREA_VALIDATION_ICON = (By.XPATH, ".//div[@class='ant-form-item-control-input']"
                                      "/descendant::span[contains(@class,'anticon-close-circle') "
                                      "or contains(@class,'anticon-check-circle')]")
TEXTAREA_ERRORS = (By.XPATH, ".//div[contains(@class,'ant-col')]/descendant::div[@class='ant-form-item-explain-error']")


class AddClubStepThree(BaseComponent):
    def __init__(self, popup: 'AddClubPopUp', node: WebElement) -> None:
        super().__init__(node)
        self._popup = popup
        self._popup_title = None
        self._logo_title = None
        self._logo_download_button = None
        self._cover_title = None
        self._cover_download_button = None
        self._gallery_title = None
        self._description_title = None
        self._description_textarea = None
        self._previous_button = None
        self._complete_button = None

    @property
    def popup_title(self) -> WebElement:
        if not self._popup_title:
            self._popup_title = self.node.find_element(*CLUB_POPUP_TITLE)
        return self._popup_title

    @property
    def logo_title(self) -> WebElement:
        if not self._logo_title:
            self._logo_title = self.node.find_element(*CLUB_LOGO_TITLE)
        return self._logo_title

    @property
    def logo_download_button(self) -> WebElement:
        if not self._logo_download_button:
            self._logo_download_button = self.node.find_element(*LOGO_DOWNLOAD_BUTTON)
        return self._logo_download_button

    def click_logo_download_button(self) -> Self:
        self.logo_download_button.click()
        return self

    @property
    def logo_uploaded_img_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.node.find_element(*LOGO_UPLOADED_IMG_CONTAINER))

    @property
    def logo_input(self) -> WebElement:
        return self.node.find_element(*LOGO_DOWNLOAD_INPUT)

    def upload_logo(self, img_path: str) -> Self:
        self.logo_input.send_keys(img_path)
        WebDriverWait(self.node.parent, 10).until(lambda d: self.logo_uploaded_img_element.is_displayed())
        return self

    @property
    def cover_title(self) -> WebElement:
        if not self._cover_title:
            self._cover_title = self.node.find_element(*CLUB_COVER_TITLE)
        return self._cover_title

    @property
    def cover_download_button(self) -> WebElement:
        if not self._cover_download_button:
            self._cover_download_button = self.node.find_element(*COVER_DOWNLOAD_BUTTON)
        return self._cover_download_button

    def click_cover_download_button(self) -> Self:
        self.cover_download_button.click()
        return self

    @property
    def cover_uploaded_img_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.node.find_element(*COVER_UPLOADED_IMG_CONTAINER))

    @property
    def cover_input(self) -> WebElement:
        return self.node.find_element(*COVER_DOWNLOAD_INPUT)

    def upload_cover(self, img_path: str) -> Self:
        self.cover_input.send_keys(img_path)
        WebDriverWait(self.node.parent, 10).until(lambda d: self.cover_uploaded_img_element.is_displayed())
        return self

    @property
    def gallery_title(self) -> WebElement:
        if not self._gallery_title:
            self._gallery_title = self.node.find_element(*CLUB_GALLERY_TITLE)
        return self._gallery_title

    @property
    def gallery_input(self) -> WebElement:
        return self.node.find_element(*GALLERY_DOWNLOAD_INPUT)

    @property
    def gallery_img_list(self) -> list[WebElement]:
        return self.node.find_elements(*GALLERY_IMAGE_CONTAINER)

    def get_list_of_gallery_image_elements(self) -> list[GalleryImageElement]:
        return [GalleryImageElement(img) for img in self.gallery_img_list]

    def get_gallery_image_element_by_index(self, index: int) -> GalleryImageElement:
        return self.get_list_of_gallery_image_elements()[index]

    def upload_img_to_gallery(self, img_path: str) -> Self:
        img_count = len(self.gallery_img_list)
        self.gallery_input.send_keys(img_path)
        WebDriverWait(self.node.parent, 10).until(lambda d: img_count < len(self.gallery_img_list))
        return self

    @property
    def description_title(self) -> WebElement:
        if not self._description_title:
            self._description_title = self.node.find_element(*DESCRIPTION_TITLE)
        return self._description_title

    @property
    def description_textarea(self) -> WebElement:
        if not self._description_textarea:
            self._description_textarea = self.node.find_element(*DESCRIPTION_TEXTAREA)
        return self._description_textarea

    @property
    def textarea_value(self) -> str:
        return self.description_textarea.get_attribute("value")

    @textarea_value.setter
    def textarea_value(self, value: str):
        self.description_textarea.send_keys(value)

    @property
    def error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*TEXTAREA_ERRORS)

    def get_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.error_messages_list]

    def clear_textarea(self) -> None:
        textarea = self.description_textarea
        current_platform = self.node.parent.capabilities['platformName']
        if current_platform.lower() == 'mac':
            textarea.send_keys(Keys.COMMAND + 'a')
            textarea.send_keys(Keys.DELETE)
        else:
            textarea.send_keys(Keys.CONTROL + 'a')
            textarea.send_keys(Keys.BACK_SPACE)

    @property
    def previous_button(self) -> WebElement:
        if not self._previous_button:
            self._previous_button = self.node.find_element(*PREVIOUS_STEP_BUTTON)
        return self._previous_button

    @property
    def popup(self) -> 'AddClubPopUp':
        return self._popup

    def click_previous_step_button(self) -> 'AddClubStepTwo':
        self.previous_button.click()
        return self.popup.step_container

    @property
    def complete_button(self) -> WebElement:
        if not self._complete_button:
            self._complete_button = self.node.find_element(*COMPLETE_BUTTON)
        return self._complete_button

    def click_complete_button(self) -> None:
        self.complete_button.click()
