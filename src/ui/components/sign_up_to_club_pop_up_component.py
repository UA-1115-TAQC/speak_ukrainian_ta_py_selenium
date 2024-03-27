from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from selenium.webdriver.common.by import By

SELF_SIGN_IN = (By.XPATH, "//div[contains(@class,'SignUpForClub_customCheckbox')]")
ADD_COMMENT = (By.XPATH, "//textarea[@id='registration-to-club_comment']")
SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'SignUpForClub_formButton')]")
ADD_CHILDREN_BUTTON = (By.XPATH, "//button[contains(@class,'add-children')]")


class SignUpToClubPopUpComponent(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._self_sign_in = None
        self._add_comment = None
        self._submit = None
        self._add_children = None

    def click_on_self_sign_in_checkbox(self):
        self._self_sign_in = self.node.find_element(*SELF_SIGN_IN)
        return self._self_sign_in.click()

    def add_comment(self, text):
        self._add_comment = self.node.find_element(*ADD_COMMENT)
        return self._add_comment.send_keys(text)

    def click_on_submit_button(self):
        self._submit = self.node.find_element(*SUBMIT_BUTTON)
        return self._submit.click()

    def click_add_children(self):
        self._add_children = self.node.find_element(*ADD_CHILDREN_BUTTON)
        self._add_children.click()




