from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent
from typing import Self

LOGO = (By.XPATH, "//div[contains(@class,'footer-logo')]")
MOTTO_UNDER_lOGO = (By.XPATH, "//div[contains(@class,'text')]")
SOCIAL_LINKS = (By.XPATH, "//div[contains(@class,'links')]/a[contains(@href, 'https')]")
COPYRIGHT_TEXT = (By.XPATH, "//div[contains(@class,'qubstudio')]")
SPONSORS_TITLE = (By.XPATH, "//div[@class='footer-partners']/div[@class='article']")
SPONSORS_LINKS = (By.XPATH, "//div[contains(@class,'sponsors')]/a[contains(@href, 'https')]")
DONATE_TITLE = (By.XPATH, "//div[@class='footer-donate']/div[@class='article']")
EXPLANATION = (By.XPATH, "//div[@class='desc']")
DONATE_BUTTON = (By.XPATH, "//button[contains(@class,'donate-button')]")

class FooterComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self._logo = None
        self._motto_under_logo = None
        self._social_links = None
        self._copyright_text = None
        self._sponsors_title = None
        self._sponsors_links = None
        self._donate_title = None
        self._explanation = None
        self._donate_button = None

    @property
    def logo_img(self) -> WebElement:
        if not self._logo:
            self._logo = self.node.find_element(*LOGO)
        return self._logo

    def click_on_logo(self) -> Self:
        self.logo_img.click()
        return self

    @property
    def motto_text(self) -> WebElement:
        if not self._motto_under_logo:
            self._motto_under_logo = self.node.find_element(*MOTTO_UNDER_lOGO)
        return self._motto_under_logo

    @property
    def list_of_social_links(self) -> list[WebElement]:
        return self.node.find_elements(*SOCIAL_LINKS)

    def social_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_social_links] if self.list_of_social_links else []

    @property
    def copyright_text(self) -> WebElement:
        if not self._copyright_text:
            self._copyright_text = self.node.find_element(*COPYRIGHT_TEXT)
        return self._copyright_text

    @property
    def sponsors_title(self) -> WebElement:
        if not self._sponsors_title:
            self._sponsors_title = self.node.find_element(*SPONSORS_TITLE)
        return self._sponsors_title

    @property
    def list_of_sponsors_links(self) -> list[WebElement]:
        return self.node.find_elements(*SPONSORS_LINKS)

    def sponsors_links(self) -> list[str]:
        return [link.get_attribute("href") for link in self.list_of_sponsors_links] if self.list_of_sponsors_links else []

    @property
    def donate_title(self) -> WebElement:
        if not self._donate_title:
            self._donate_title = self.node.find_element(*DONATE_TITLE)
        return self._donate_title

    @property
    def explanation(self) -> WebElement:
        if not self._explanation:
            self._explanation = self.node.find_element(*EXPLANATION)
        return self._explanation

    @property
    def donate_button(self) -> WebElement:
        if not self._donate_button:
            self._donate_button = self.node.find_element(*DONATE_BUTTON)
        return self._donate_button

    def click_on_donate_button(self) -> Self:
        self.donate_button.click()
        return self
