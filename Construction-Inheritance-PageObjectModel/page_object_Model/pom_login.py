from selenium.webdriver.common.by import By

from base_class import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://example.com/login"

    def open(self):
        self.driver.get(self.url)

    def login(self,username, password):
        self.wait_for_element(By.ID, "username").send_keys()
        self.wait_for_element(By.NAME, "password").send_keys()
        self.wait_for_element(By.ID, "submit").click()

