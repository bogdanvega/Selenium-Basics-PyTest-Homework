from selenium import webdriver # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

# Instantiate the web driver for Chrome
driver = webdriver.Chrome()

# Navigate to the Sauce Demo website
driver.get("https://www.saucedemo.com/")

# Wait for 2 seconds to allow the page to load completely
time.sleep(2)

# Login to the Website
# Locate and interact with the login form
# Enter the username: standard_user
driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys('standard_user')
# Enter the password: secret_sauce
driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys('secret_sauce')
# Click the "Login" button
driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()

# Wait for 2 seconds to allow the page to load completely
time.sleep(2)

## Verify that you have successfully logged in by checking the presence of a product element.
product_element = driver.find_elements(By.XPATH, "//a[@id = 'item_4_title_link']")
assert len(product_element) > 0



# Close the browser and end the WebDriver session
driver.quit()