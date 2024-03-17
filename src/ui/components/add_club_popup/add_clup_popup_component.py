from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_club_popup.add_club_step_one import AddClubStepOne
from src.ui.components.base_pop_up import BasePopUp
from src.ui.components.base_component import BaseComponent
from src.ui.elements.popup_step_element import PopUpStep

ADD_CLUB_POPUP = (By.XPATH, "//div[contains(@class,'modal-add-club')]")
SIDER_ELEMENT = (By.XPATH, ".//div[@class='ant-layout-sider-children']")
STEP_CONTAINER = (By.XPATH, ".//main[contains(@class,'add-club-container')]")
ACTIVE_STEP = (By.XPATH, ".//main[contains(@class,'add-club-container')]"
                         "//div[contains(@class,'ant-steps-item-active')]"
                         "//span[@class='ant-steps-icon']")
SIDER_STEPS_LIST = (By.XPATH, ".//div[contains(@class,'ant-steps-item-wait') "
                              "or contains(@class,'ant-steps-item-process')]")


class AddClubPopUpComponent(BasePopUp):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.sider = AddClubSider(node.find_element(*SIDER_ELEMENT))

    @property
    def step_container(self):
        active_step = self.node.find_element(*ACTIVE_STEP).get_attribute("innerText")
        match active_step:
            case "1":
                return AddClubStepOne(self.node.find_element(*STEP_CONTAINER))
            case _:
                return None


class AddClubSider(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._steps_node_list = None
        self._step_one = None
        self._step_two = None
        self._step_three = None

    @property
    def steps_node_list(self) -> list[WebElement]:
        if not self._steps_node_list:
            self._steps_node_list = PopUpStep(self.node.find_elements(*SIDER_STEPS_LIST))
        return self._steps_node_list

    @property
    def step_one(self) -> PopUpStep:
        if not self._step_one:
            self._step_one = PopUpStep(self.steps_node_list[0])
        return self._step_one

    @property
    def step_two(self) -> PopUpStep:
        if not self._step_two:
            self._step_two = PopUpStep(self.steps_node_list[1])
        return self._step_two

    @property
    def step_three(self) -> PopUpStep:
        if not self._step_three:
            self._step_three = PopUpStep(self.steps_node_list[2])
        return self._step_three
