from selenium import webdriver

class SimpleAutomation:
    def __init__(self):
        # Initialize the webdriver in the constructor
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def open_page(self,url):
        self.driver.get(url)
    def close_browser(self):
        self.driver.quit()

# using the class
ob = SimpleAutomation()
ob.open_page("https")
ob.close_browser()