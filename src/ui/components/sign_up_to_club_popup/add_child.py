from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from typing import Self


class AddChild(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)

        self.locators = {
            "add_first_name": ("xpath", "./descendant::input[@id='add-child_firstName']"),
            "add_last_name": ("xpath", "./descendant::input[@id='add-child_lastName']"),
            "add_age": ("xpath", "./descendant::input[@id='add-child_age']"),
            "male_gender": ("xpath", "./descendant::input[@value='MALE']"),
            "female_gander": ("xpath", "./descendant::input[@value='FEMALE']"),
            #"submit_button": ("xpath", "./descendant::button[contains(@class,'submit-button')]"),
            "pop_up_window": ("xpath", ".//div[@class='ant-modal-content']"),
        }

    def set_first_name(self, value: str) -> None:
        self.add_first_name.send_keys(value)

    def set_last_name(self, value: str) -> None:
        self.add_last_name.send_keys(value)

    def set_age(self, value: str) -> None:
        self.add_age.send_keys(value)

    def click_male_gender(self) -> None:
        self.male_gender.click_button()

    def click_female_gender(self) -> None:
        self.female_gander.click_button()

   #def click_submit_button(self) -> None:
        #self.submit_button.click_button()
