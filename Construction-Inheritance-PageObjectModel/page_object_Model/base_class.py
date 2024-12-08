# Base Class: Manages WebDriver initialization and teardown.

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(by, value))

    def quit(self):
        self.driver.quit()

