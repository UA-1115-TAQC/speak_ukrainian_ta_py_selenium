from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.ui.page_factory.custom_page_factory import CustomPageFactory


class BaseComponent(CustomPageFactory):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node.parent, node)

    def click_element(self, element: WebElement):
        self.get_wait(40).until(EC.element_to_be_clickable(element)).click()

