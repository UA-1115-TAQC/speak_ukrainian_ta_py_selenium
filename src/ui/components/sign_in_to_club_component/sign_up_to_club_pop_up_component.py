from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from src.ui.components.sign_in_to_club_component.add_child_component import AddChildComponent


class SignUpToClubPopUpComponent(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "self_or_child_sign_in": ("xpath", "./descendant::div[contains(@class,'SignUpForClub_customCheckbox')]"),
            "add_comment": ("xpath", "//textarea[@id='registration-to-club_comment']"),
            "submit_button": ("xpath", "//button[contains(@class,'SignUpForClub_formButton')]"),
            "add_child": ("xpath", "//button[contains(@class,'add-children')]")

        }

    def click_add_children(self) -> AddChildComponent:
        self.add_children.click_button()
        return AddChildComponent(self.node)

    def click_self_or_child_sign_in(self) -> None:
        self.self_or_child_sign_in.click_button()

    def set_comment(self, value) -> None:
        self.add_comment.send_keys(value)

    def click_submit_button(self) -> None:
        self.submit_button.click_button()



