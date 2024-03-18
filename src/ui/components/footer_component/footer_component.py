from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.ui.components.base_component import BaseComponent

LOGO = (By.XPATH, "./descendant::div[contains(@class,'footer-logo')]")
MOTTO_UNDER_lOGO = (By.XPATH, "./descendant::div[contains(@class,'text')]")
SOCIAL_LINKS = (By.XPATH, "./descendant::div[contains(@class,'links')]")
COPYRIGHT_TEXT = (By.XPATH, "./descendant::div[contains(@class,'qubstudio')]")
SPONSORS_TITLE = (By.XPATH, "./descendant::div[@class='footer-partners']/div[@class='article']")
SPONSORS_LINKS = (By.XPATH, "./descendant::div[contains(@class,'sponsors')]")
DONATE_TITLE = (By.XPATH, "./descendant::div[@class='footer-donate']/div[@class='article']")
EXPLANATION = (By.XPATH, "./descendant::div[@class='desc']")
DONATE_BUTTON = (By.XPATH, "./descendant::button[contains(@class,'donate-button')]")


class FooterComponent(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.logo = node.find_element(*LOGO)
        self.motto_under_logo = node.find_element(*MOTTO_UNDER_lOGO)
        self.social_links = node.find_elements(*SOCIAL_LINKS)
        self.copyright_text = node.find_element(*COPYRIGHT_TEXT)
        self.sponsors_title = node.find_element(*SPONSORS_TITLE)
        self.sponsors_links = node.find_elements(*SPONSORS_LINKS)
        self.donate_title = node.find_element(*DONATE_TITLE)
        self.explanation = node.find_element(*EXPLANATION)
        self.donate_button = node.find_element(*DONATE_BUTTON)


    def click_on_logo(self):
        self.logo.click()

    def get_motto_text(self):
        return self.motto_under_logo.text

    def get_social_links(self):
        return [link.get_attribute("href") for link in self.social_links]

    def get_copyright_text(self):
        return self.copyright_text.text

    def get_sponsors_title(self):
        return self.sponsors_title.text

    def get_sponsors_links(self):
        return [link.get_attribute("href") for link in self.sponsors_links]

    def get_donate_title(self):
        return self.donate_title.text

    def donate_explanation_text(self):
        return self.explanation.text

    def click_on_donate_button(self):
        self.donate_button.click()

