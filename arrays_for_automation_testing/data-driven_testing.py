from selenium import webdriver

# Test data: list of URLs to test
urls = ["https://example1.com", "https://example2.com", "https://example3.com"]

# Initialize WebDriver
driver = webdriver.Chrome()

# Iterate through each URL
for url in urls:
    driver.get(url)
    print(f"Testing URL: {url}")
    # Add your test logic here

# Close the browser
driver.quit()
