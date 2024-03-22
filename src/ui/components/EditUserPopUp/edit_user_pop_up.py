from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_pop_up import BasePopUp

EDIT_USER_POPUP_TITLE = (By.XPATH, ".//div[@class='edit-header']")
USER_ICON = (By.XPATH, "")
USER_TYPE_BUTTON = (By.XPATH, "")
MANAGER_ICON = (By.XPATH, "")
MANAGER_TYPE_BUTTON = (By.XPATH, "")
LAST_NAME_INPUT_ELEMENT = (By.XPATH, "")
FIRST_NAME_INPUT_ELEMENT = (By.XPATH, "")
PHONE_INPUT_ELEMENT = (By.XPATH, "")
EMAIL_INPUT_ELEMENT = (By.XPATH, "")
UPLOAD_PHOTO_INPUT_ELEMENT = (By.XPATH, "")
PHOTO_TITLE = (By.XPATH, "")

CHECKBOX_CHANGE_PASSWORD = (By.XPATH, "")
CURRENT_PASSWORD_INPUT_ELEMENT = (By.XPATH, "")
NEW_PASSWORD_INPUT_ELEMENT = (By.XPATH, "")
CONFIRM_PASSWORD_INPUT_ELEMENT = (By.XPATH, "")
SUBMIT_BUTTON = (By.XPATH, "")



class EditUserPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super(self).__init__(node)


