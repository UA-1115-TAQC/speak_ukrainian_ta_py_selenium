from typing import Self

from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent
from src.ui.elements.gallery_image_element import GalleryImageElement
from src.ui.elements.uploaded_image_element import UploadedImageElement


class AddClubStepThree(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "club_popup_title": ("xpath", ".//div[contains(@class,'add-club-header')]"),
            "complete_button": ("xpath", ".//button[contains(@class,'add-club-content-next')]"),
            "previous_step_button": ("xpath", ".//button[contains(@class,'add-club-content-prev')]"),
            "club_logo_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][1]"),
            "logo_download_button": ("xpath", "./descendant::span[(@class='ant-upload') and (@role='button')][1]"),
            "logo_download_input": ("xpath", ".//input[@id='basic_urlLogo']"),
            "logo_uploaded_img_container": ("xpath",
                                            "./descendant::div[@class='ant-upload-list ant-upload-list-text'][1]"),
            "club_cover_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][2]"),
            "cover_download_button": ("xpath", "./descendant::span[(@class='ant-upload') and (@role='button')][2]"),
            "cover_download_input": ("xpath", ".//input[@id='basic_urlBackground']"),
            "cover_uploaded_img_container": ("xpath",
                                             "/descendant::div[@class='ant-upload-list ant-upload-list-text'][2]"),
            "club_gallery_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][3]"),
            "gallery_download_button": ("xpath", "./descendant::span[(@class='ant-upload') and (@role='button')][3]"),
            "gallery_download_input": ("xpath",
                                       "./descendant::span[(@class='ant-upload') and (@role='button')][3]//input"),
            "gallery_image_container": ("xpath", "//span[contains(@class,'ant-upload-picture-card-wrapper')]"
                                                 "//div[@class='ant-upload-list-item-container']"),
            "description_title": ("xpath", "./descendant::span[contains(@class,'ant-typography')][4]"),
            "description_textarea": ("xpath", ".//textarea[contains(@id,'basic_description')]"),
            "textarea_validation_icon": ("xpath", ".//div[@class='ant-form-item-control-input']"
                                                  "/descendant::span[contains(@class,'anticon-close-circle') "
                                                  "or contains(@class,'anticon-check-circle')]"),
            "textarea_errors": ("xpath", ".//div[contains(@class,'ant-col')]"
                                         "//div[@class='ant-form-item-explain-error']"),
            "step_container": ("xpath", ".//main[contains(@class,'add-club-container')]")
        }

    def get_club_popup_title_text(self) -> str:
        return self.club_popup_title.text

    def get_club_cover_title_text(self) -> str:
        return self.club_cover_title.text

    def click_logo_download_button(self) -> Self:
        self.logo_download_button.click_button()
        return self

    @property
    def logo_uploaded_img_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.logo_uploaded_img_container)

    def upload_logo(self, img_path: str) -> Self:
        self.node.find_element(*self.locators["logo_download_input"]).send_keys(img_path)
        self.logo_uploaded_img_container.visibility_of_element_located()
        return self

    def get_club_logo_title_text(self) -> str:
        return self.club_logo_title.text

    def click_cover_download_button(self) -> Self:
        self.cover_download_button.click_button()
        return self

    @property
    def cover_uploaded_img_element(self) -> UploadedImageElement:
        return UploadedImageElement(self.cover_uploaded_img_container)

    def upload_cover(self, img_path: str) -> Self:
        self.node.find_element(*self.locators["cover_download_input"]).send_keys(img_path)
        self.cover_uploaded_img_container.visibility_of_element_located()
        return self

    def get_club_gallery_title_text(self) -> str:
        return self.club_gallery_title.text

    @property
    def gallery_img_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["gallery_image_container"])

    def get_list_of_gallery_image_elements(self) -> list[GalleryImageElement]:
        return [GalleryImageElement(img) for img in self.gallery_img_list]

    def get_gallery_image_element_by_index(self, index: int) -> GalleryImageElement:
        return self.get_list_of_gallery_image_elements()[index]

    def click_gallery_download_button(self):
        return self.gallery_download_button.click_button()

    def upload_img_to_gallery(self, img_path: str) -> Self:
        img_count = len(self.gallery_img_list)
        self.node.find_element(*self.locators["gallery_download_input"]).send_keys(img_path)
        self.get_wait(5).until(lambda d: img_count < len(self.gallery_img_list))
        return self

    def get_description_title_text(self) -> str:
        return self.description_title.text

    def get_description_textarea_value(self) -> str:
        return self.description_textarea.get_attribute("value")

    def set_description_textarea_value(self, value: str):
        self.description_textarea.send_keys(value)

    @property
    def error_messages_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["textarea_errors"])

    def get_error_messages_text_list(self) -> list[str]:
        return [error.get_attribute("innerText") for error in self.error_messages_list]

    def clear_textarea(self) -> Self:
        self.description_textarea.visibility_of_element_located().click()
        self.get_actions().key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        self.get_actions().key_down(Keys.COMMAND) \
            .send_keys('a') \
            .key_up(Keys.COMMAND) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
        return self

    def click_previous_step_button(self) -> 'AddClubStepTwo':
        self.previous_button.click_button()
        from src.ui.components.add_club_popup.add_club_step_two import AddClubStepTwo
        return AddClubStepTwo(self.step_container)

    def click_complete_button(self) -> None:
        self.complete_button.click_button()
