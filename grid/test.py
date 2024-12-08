from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# URL of the Selenium Hub
hub_url = "http://localhost:4444/wd/hub"

# Set up ChromeOptions
chrome_options = Options()
# You can specify additional options here if needed, e.g. headless mode
# chrome_options.add_argument("--headless")

# Set up capabilities
capabilities = {
    "browserName": "chrome",
    "platformName": "LINUX"
}

# Initialize the remote WebDriver
driver = webdriver.Remote(
    command_executor=hub_url,
    options=chrome_options,  # pass chrome_options here
    keep_alive=True
)

# Open the URL
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)

# Find the search box, input a search term, and submit it
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Grid testing")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Verify if the results page contains "Selenium"
if "Selenium" in driver.title:
    print("Test Passed: Selenium Grid is working!")
else:
    print("Test Failed: Selenium Grid is not working!")

# Close the browser
driver.quit()
