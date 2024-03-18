from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent


class RatingComponent(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)

