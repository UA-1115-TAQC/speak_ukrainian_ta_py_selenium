from selenium.webdriver.remote.webelement import WebElement

class BaseElement:
    def __init__(self, node: WebElement):
        self.node = node

    def is_displayed(self)->bool:
        return self.node.is_displayed()
    
    def get_value_css_property(self, property_name)->str:
        return self.node.value_of_css_property(property_name)