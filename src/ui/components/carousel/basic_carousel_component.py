from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.components.base_component import BaseComponent

LEFT_ARROW_BUTTON = (By.XPATH, ".//span[contains(@aria-label, 'arrow-left')]")
RIGHT_ARROW_BUTTON = (By.XPATH, ".//span[contains(@aria-label, 'arrow-right')]")
SLICK_DOTS = (By.XPATH, ".//ul[contains(@class,\"slick-dots\")]/li")
SLICK_DOTS_CONTAINER = (By.XPATH, ".//ul[contains(@class,\"slick-dots\")]")
SLIDER_CONTAINER = (By.XPATH, ".//div[contains(@class,\"slick-slider\")]")


class BasicCarouselComponent(BaseComponent):
    def __init__(self, driver: webdriver, node: WebElement) -> None:
        super().__init__(driver)
        self._driver = driver
        self._node = node
        self._left_arrow_button = None
        self._right_arrow_button = None
        self._slick_dots = None
        self._slick_dots_container = None
        self._slider_container = None
        self._wait = WebDriverWait(self._driver, 30)

    @property
    def left_arrow_button(self) -> WebElement:
        if not self._left_arrow_button:
            self._left_arrow_button = self._node.find_element(*LEFT_ARROW_BUTTON)
        return self._left_arrow_button

    @property
    def right_arrow_button(self) -> WebElement:
        if not self._right_arrow_button:
            self._right_arrow_button = self._node.find_element(*RIGHT_ARROW_BUTTON)
        return self._right_arrow_button

    @property
    def slick_dots(self) -> list[WebElement]:
        if not self._slick_dots:
            self._slick_dots = self._node.find_elements(*SLICK_DOTS)
        return self._slick_dots

    @property
    def slick_dots_container(self) -> WebElement:
        if not self._slick_dots_container:
            self._slick_dots_container = self._node.find_element(*SLICK_DOTS_CONTAINER)
        return self._slick_dots_container

    @property
    def slider_container(self) -> WebElement:
        if not self._slider_container:
            self._slider_container = self._node.find_element(*SLIDER_CONTAINER)
        return self._slider_container

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

