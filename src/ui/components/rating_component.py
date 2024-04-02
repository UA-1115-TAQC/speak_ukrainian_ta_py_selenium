from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent

ZERO_STAR_RATE = (By.XPATH, "./descendant::li[@class='ant-rate-star ant-rate-star-zero']")
FULL_STAR_RATE = (By.XPATH, "./descendant::li[@class='ant-rate-star ant-rate-star-full']")
HALF_STAR_RATE = (By.XPATH, "./descendant::li[@class='ant-rate-star ant-rate-star-half']")


class RatingComponent(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
