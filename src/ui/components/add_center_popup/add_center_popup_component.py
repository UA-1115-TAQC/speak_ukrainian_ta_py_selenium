from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.add_center_step_four import AddCenterStepFour
from src.ui.components.add_center_popup.add_center_step_one import AddCenterStepOne
from src.ui.components.add_center_popup.add_center_step_three import AddCenterStepThree
from src.ui.components.add_center_popup.add_center_step_two import AddCenterStepTwo
from src.ui.components.add_club_popup.add_clup_popup_component import AddClubSider
from src.ui.components.base_pop_up import BasePopUp
from src.ui.elements.popup_step_element import PopUpStep


class AddCenterSider(AddClubSider):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)

    @property
    def step_four(self) -> PopUpStep:
        return PopUpStep(self.sider_steps[3])


class AddCenterPopUp(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            **self.locators,
            "sider": ("xpath", ".//div[@class='side']"),
            "step_container": ("xpath", ".//main[contains(@class,'add-center-container')]"),
            "active_step": ("xpath", ".//main[contains(@class,'add-center-container')]"
                                     "//div[contains(@class,'ant-steps-item-active')]"
                                     "//span[@class='ant-steps-icon']")
        }

    @property
    def sider_element(self) -> AddCenterSider:
        return AddCenterSider(self.sider)

    @property
    def step_one_container(self) -> AddCenterStepOne:
        return AddCenterStepOne(self.step_container)

    @property
    def step_two_container(self) -> AddCenterStepTwo:
        return AddCenterStepTwo(self.step_container)

    @property
    def step_three_container(self) -> AddCenterStepThree:
        return AddCenterStepThree(self.step_container)

    @property
    def step_four_container(self) -> AddCenterStepFour:
        return AddCenterStepFour(self.step_container)

    @property
    def get_active_step(self) -> WebElement:
        return self.node.find_element(*self.locators["active_step"])
