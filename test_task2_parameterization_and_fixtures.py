import pytest
from conftest import selenium_driver  # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

URL = "https://www.saucedemo.com/"


@pytest.mark.parametrize('user, password, should_login, expected_error', [
    ('standard_user', 'secret_sauce', True, None),
    ('locked_out_user', 'secret_sauce', False, 'Epic sadface: Sorry, this user has been locked out.'),
    ('problem_user', 'secret_sauce', True, None),
    ('performance_glitch_user', 'secret_sauce', True, None),
    ('error_user', 'secret_sauce', True, None),
    ('visual_user', 'secret_sauce', True, None)
])
def test_login_and_product_search(user, password, should_login, expected_error, selenium_driver):
    driver = selenium_driver
    # Navigate to the desired website
    driver.get(URL)
    # Wait for 3 seconds to allow the page to load completely
    time.sleep(3)
    # Locate and interact with the login form. Enter the username: standard_user
    driver.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys(user)
    # Enter the password: secret_sauce
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys(password)
    # Click the "Login" button
    driver.find_element(By.XPATH, "//input[@id = 'login-button']").click()
    # Wait for 2 seconds to allow the page to load completely
    time.sleep(2)
    if should_login:
        # Verify that you have successfully logged in by checking the presence of the products page title.
        assert driver.find_element(By.XPATH, "//span[@class = 'title']").text == "Products"
        assert driver.find_element(By.XPATH, "//div[@class = 'inventory_item_name ']").text == "Sauce Labs Backpack"
    else:
        # Error message
        assert driver.find_element(By.XPATH, "//h3[@data-test = 'error']").text == expected_error

