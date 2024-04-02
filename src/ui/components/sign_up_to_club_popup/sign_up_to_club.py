from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from src.ui.components.sign_up_to_club_popup.add_child import AddChild


class SignUpToClub(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "sign_up_checkbox": ("xpath", "./descendant::div[contains(@class,'SignUpForClub_customCheckbox')]"),
            "add_comment": ("xpath", "//textarea[@id='registration-to-club_comment']"),
            "submit_button": ("xpath", "//button[contains(@class,'SignUpForClub_formButton')]"),
            "add_child": ("xpath", ".//button[contains(@class,'add-children')]"),
            "add_child_pop_up": ("xpath", "//div[contains(@class,'add-child-modal')]")
        }

    def click_add_children(self) -> AddChild:
        self.add_child.click_button()
        return AddChild(self.add_child_pop_up)

    def click_self_or_child_sign_in(self):
        self.sign_up_checkbox.click_button()

    def set_comment(self, value):
        self.add_comment.send_keys(value)

    def click_submit_button(self):
        self.submit_button.click_button()



