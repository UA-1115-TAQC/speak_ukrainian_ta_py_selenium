from src.ui.elements.base_element import BaseElement


class DirectionElement(BaseElement):
    def __init__(self, node):
        super().__init__(node)
        self.locators = {
            "logo": ("xpath", ".//div[contains(@class,'icon')]"),
            "name": ("xpath", ".//span[contains(@class,'name')]"),
        }

    def get_name_text(self):
        return self.name.text
