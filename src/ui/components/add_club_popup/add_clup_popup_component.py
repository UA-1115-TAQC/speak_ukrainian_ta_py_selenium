from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.add_club_popup.add_club_step_one import AddClubStepOne
from src.ui.components.add_club_popup.add_club_step_three import AddClubStepThree
from src.ui.components.add_club_popup.add_club_step_two import AddClubStepTwo
from src.ui.components.base_pop_up import BasePopUp
from src.ui.components.base_component import BaseComponent
from src.ui.elements.popup_step_element import PopUpStep


class AddClubSider(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "sider_steps_list": ("XPATH", ".//div[contains(@class,'ant-steps-item-wait') "
                                          "or contains(@class,'ant-steps-item-process')]")
        }

    @property
    def sider_steps(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["sider_steps_list"])

    @property
    def step_one(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_list[0])

    @property
    def step_two(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_list[1])

    @property
    def step_three(self) -> PopUpStep:
        return PopUpStep(self.sider_steps_list[2])


class AddClubPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "sider": ("xpath", ".//div[@class='ant-layout-sider-children']"),
            "step_container": ("xpath", ".//main[contains(@class,'add-club-container')]"),
            "active_step": ("xpath", ".//main[contains(@class,'add-club-container')]"
                                     "//div[contains(@class,'ant-steps-item-active')]"
                                     "//span[@class='ant-steps-icon']")
        }

    @property
    def sider_element(self) -> AddClubSider:
        return AddClubSider(self.sider)

    @property
    def step_one_container(self) -> AddClubStepOne:
        return AddClubStepOne(self.step_container)

    @property
    def step_two_container(self) -> AddClubStepTwo:
        return AddClubStepTwo(self.step_container)

    @property
    def step_three_container(self) -> AddClubStepThree:
        return AddClubStepThree(self.step_container)
