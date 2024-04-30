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
driver.get("http://127.0.0.1:8000/login/")  # Replace with the actual login page URL
username_input = driver.find_element(By.NAME, 'username')

username_input.send_keys('test_user')

# Submit the login form
login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
login_button.click()

# Wait for the login process to complete
WebDriverWait(driver, 10).until(EC.url_contains("http://127.0.0.1:8000/get_items/"))  # URL redirected to after login

# Open the webpage containing the forms
driver.get("http://127.0.0.1:8000/add_item/")  # page to add_item

try:
    # Test ItemForm
    title_input = driver.find_element(By.NAME, 'title')
    title_input.send_keys('Test Item')
    
    end_date_input = driver.find_element(By.NAME, 'end_date')
    end_date_input.send_keys('3024-04-20')

    initial_price_input = driver.find_element(By.NAME, 'initial_price')
    initial_price_input.send_keys('10000')

    description_input = driver.find_element(By.NAME, 'description')
    description_input.send_keys('This is a test description.')

    # Wait for a bit to see the result
    time.sleep(2)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[text()='Add Item']")
    submit_button.click()

    # Wait for a bit to see the result
    time.sleep(2)

    # Close the browser window
    driver.quit()

except Exception as e:
    print("An error occurred:", e)
    # Ensure the browser window is closed in case of an error
    driver.quit()
