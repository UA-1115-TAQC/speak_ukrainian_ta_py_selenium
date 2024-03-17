from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_club_popup.add_clup_popup_component import AddClubPopUpComponent
from src.ui.components.base_component import BaseComponent

ADD_CLUB_BUTTON = (By.XPATH, ".//button[contains(@class,'add-club-button')]")
ADD_CLUB_POPUP = (By.XPATH, "//div[contains(@class,'modal-add-club')]")


class HeaderComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)

    def add_club_click(self) -> AddClubPopUpComponent:
        self.node.find_element(*ADD_CLUB_BUTTON).click()
        return AddClubPopUpComponent(self.node.find_element(*ADD_CLUB_POPUP))
