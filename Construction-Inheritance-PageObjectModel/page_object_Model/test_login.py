from selenium import webdriver
from pom_login import LoginPage

driver = webdriver.Chrome()
ob = LoginPage(driver)
ob.open()
ob.login("username","password")
ob.quit()