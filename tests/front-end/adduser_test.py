from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the WebDriver executable filename
webdriver_filename = './chromedriver.exe'  # Replace with the actual filename

# Initialize the WebDriver with the specified filename
options = webdriver.ChromeOptions()
options.binary_location = webdriver_filename
driver = webdriver.Chrome(options=options)

# Navigate to the login page and fill in the credentials
driver.get("http://127.0.0.1:8000/")  # Replace with the actual login page URL
username_input = driver.find_element(By.NAME, 'username')

username_input.send_keys('test_user')

# Submit the login form
login_button = driver.find_element(By.XPATH, "//button[text()='Create account']")
login_button.click()

# Wait for a bit to see the result
time.sleep(2)