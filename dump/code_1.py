from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup WebDriver options
options = Options()

# Uncomment for headless mode
# options.add_argument("--headless")
# Initialize WebDriver
# Initialize WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Open website
url = "https://www.thetrainline.com/about-us"
driver.get(url)

time.sleep(3)  # Wait for elements to load

# Accept cookies if button exists
try:
    accept_button = driver.find_element(By.XPATH, "//button[contains(text(),'Accept') or contains(text(),'OK')]")
    accept_button.click()
    time.sleep(2)  # Wait for page update
except Exception as e:
    print("No cookie acceptance button found or error occurred:", e)

# Get page source
html_content = driver.page_source

# Save HTML to file
with open("trainline_about_us.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content saved successfully.")

# Close the browser
driver.quit()
