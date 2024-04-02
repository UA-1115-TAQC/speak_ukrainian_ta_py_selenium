from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.add_center_popup.add_center_step_three import AddCenterStepThree
from src.ui.components.base_component import BaseComponent
from src.ui.elements.input_with_label_icons_errors import InputWithLabelIconsErrors


class AddCenterStepTwo(BaseComponent):
    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "center_popup_title": ("xpath", ".//div[@class='modal-title']"),
            "center_contacts_title": ("xpath", ".//span[contains(@class,'ant-typography')]"),
            "telephone_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                              "/descendant::div[contains(@class,'add-club-contact')][1]"),
            "facebook_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                             "/descendant::div[contains(@class,'add-club-contact')][2]"),
            "whatsapp_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                             "/descendant::div[contains(@class,'add-club-contact')][3]"),
            "email_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                          "/descendant::div[contains(@class,'add-club-contact')][4]"),
            "skype_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                          "/descendant::div[contains(@class,'add-club-contact')][5]"),
            "site_input_node": ("xpath", ".//div[contains(@class,'add-club-contacts')]"
                                         "/descendant::div[contains(@class,'add-club-contact')][6]"),
            "next_step_button": ("xpath", ".//button[contains(@class,'next-btn')]"),
            "previous_step_button": ("xpath", ".//button[contains(@class,'prev-btn')]")
        }

    def get_center_popup_title_text(self) -> str:
        return self.center_popup_title.text

    def get_center_contacts_title_text(self) -> str:
        return self.center_contacts_title.text

    @property
    def telephone_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.telephone_input_node)

    @property
    def facebook_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.facebook_input_node)

    @property
    def whatsapp_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.whatsapp_input_node)

    @property
    def email_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.email_input_node)

    @property
    def skype_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.skype_input_node)

    @property
    def site_element(self) -> InputWithLabelIconsErrors:
        return InputWithLabelIconsErrors(self.site_input_node)


    def click_next_step_button(self) -> AddCenterStepThree:
        self.next_step_button.click_button()
        return AddCenterStepThree(self.node)

    def click_previous_step_button(self) -> 'AddCenterStepOne':
        self.previous_step_button.click_button()
        from src.ui.components.add_center_popup.add_center_step_one import AddCenterStepOne
        return AddCenterStepOne(self.node)
