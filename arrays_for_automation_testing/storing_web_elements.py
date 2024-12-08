# In web automation testing, we often deal with multiple elements of the same type, such as a group of checkboxes.
from os import close

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://example.com")

# Find all checkbox elements
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Click each checkbox
for checkbox in checkboxes:
    checkbox.click()

# Close the browser
driver.quit()
