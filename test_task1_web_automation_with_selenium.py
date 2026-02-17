from selenium import webdriver  # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

URL = "https://www.saucedemo.com/"


def get_driver(url=URL):
    # Instantiate the web driver for Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Navigate to the desired website
    driver.get(url)
    return driver


def test_login_and_product_search():
    driver = get_driver()
    # Wait for 3 seconds to allow the page to load completely
    time.sleep(3)
    # Locate and interact with the login form. Enter the username: standard_user
    driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys('standard_user')
    # Enter the password: secret_sauce
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys('secret_sauce')
    # Click the "Login" button
    driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
    # Wait for 2 seconds to allow the page to load completely
    time.sleep(2)
    # Verify that you have successfully logged in by checking the presence of the products page title.
    assert driver.find_element(By.XPATH, "//span[@class = 'title']").text == "Products"
    assert driver.find_element(By.XPATH, "//div[@class = 'inventory_item_name ']").text == "Sauce Labs Backpack"
    # Close the browser and end the WebDriver session
    driver.quit()
