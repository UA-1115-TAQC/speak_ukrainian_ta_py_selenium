from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent


class BasicCarouselComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "left_arrow_button": ("xpath", ".//span[contains(@aria-label, 'arrow-left')]"),
            "right_arrow_button": ("xpath", ".//span[contains(@aria-label, 'arrow-right')]"),
            "slick_dots": ("xpath", ".//ul[contains(@class,\"slick-dots\")]/li"),
            "slick_dots_container": ("xpath", ".//ul[contains(@class,\"slick-dots\")]"),
            "slider_container": ("xpath", ".//div[contains(@class,\"slick-slider\")]"),
        }
        self._wait = WebDriverWait(self.driver, 30)

    @property
    def slick_dots(self) -> list[WebElement]:
        return self.node.find_elements(*self.locators["slick_dots"])

    def click_right_arrow_button(self):
        self.right_arrow_button.click()
        return self

    def click_left_arrow_button(self):
        self.left_arrow_button.click()
        return self

    def get_slick_dot_by_index(self, index) -> WebElement:
        if 0 <= index < len(self.slick_dots):
            return self.slick_dots[index]
        raise ValueError("The index must be in the range between 0 and "
                         + str((len(self.slick_dots) - 1)) + ", inclusive")

    def click_slick_dot_by_index(self, index):
        slick_dot = self.get_slick_dot_by_index(index)
        slick_dot.click()
        self._wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             f"(//ul[contains(@class,'slick-dots')]/li)[{index + 1}][@style='background-color: rgb(250, 140, 22)']")
        ))
        return self

    def get_active_slick_dot(self) -> WebElement:
        for dot in self.slick_dots:
            if dot.get_attribute("class") == "slick-active":
                return dot
        return None

    def click_active_slick_dot(self):
        active_dot = self.get_active_slick_dot()
        if active_dot:
            active_dot.click()
        return self

    def get_slick_dot_color(self, slick_dot: WebElement) -> str:
        return Color.from_string(slick_dot.value_of_css_property("background-color")).hex
