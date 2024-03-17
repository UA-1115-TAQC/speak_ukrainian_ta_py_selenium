import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaseTestRunner(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0.5)
        self.driver.get("http://speak-ukrainian.eastus2.cloudapp.azure.com/dev/")
        return super().setUp()
    
    # def test_example(self):
    #     text_box = self.driver.find_element(by=By.NAME, value="my-text")
    #     submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")
    #     text_box.send_keys("Selenium")
    #     time.sleep(3)
    #     submit_button.click()
    #     time.sleep(3)

    def tearDown(self) -> None:
        # self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()