from selenium import webdriver


class BaseAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def close_browser(self):
        self.driver.quit()


class LoginAutomation(BaseAutomation):
    def open_browser(self):
        self.driver.get("https")
    def perform_login(self,username,password):
        self.driver.find_element("id",username).send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "submit")


# using the child class

ob = LoginAutomation()
ob.open_browser()
ob.perform_login("test_user","password")
ob.close_browser()