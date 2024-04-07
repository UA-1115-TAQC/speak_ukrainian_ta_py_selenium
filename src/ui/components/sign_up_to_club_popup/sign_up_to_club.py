from typing import Self
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent
from src.ui.components.sign_up_to_club_popup.add_child import AddChild


class SignUpToClub(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "sign_up_checkbox_list": (
                "xpath", "//div[contains(@class,'ant-checkbox-group')]//div[contains(@class,'customCheckbox')]"),
            "add_comment": ("xpath", ".//textarea[@id='registration-to-club_comment']"),
            "submit_button": ("xpath", "//button[contains(@class,'SignUpForClub_formButton')]"),
            "add_child": ("xpath", ".//button[contains(@class,'add-children')]"),
            "add_child_pop_up": ("xpath", "//div[contains(@class,'add-child-modal')]")

        }

        self.wait = WebDriverWait(self.driver, 30)

    def click_add_children(self) -> AddChild:
        self.add_child.click_button()
        return AddChild(self.add_child_pop_up)

    def set_comment(self, value):
        self.add_comment.send_keys(value)

    def click_submit_button(self):
        self.submit_button.click_button()

    @property
    def children_list(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["sign_up_checkbox_list"])

    def get_children_list_names(self) -> list[str]:
        return [children.text for children in self.children_list]

    def click_child_checkbox_by_index(self, index: int) -> Self:
        self.children_list[index].click()
        return self

    def click_child_checkbox_by_name(self, name: str) -> Self:
        for children in self.children_list:
            if name in children.text:
                children.click()
        return self
