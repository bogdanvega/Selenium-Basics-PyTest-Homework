import pytest
from selenium import webdriver  # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def selenium_driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)  # Implicit wait to handle timing issues

    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()


@pytest.mark.parametrize('user, password', [
    ('standard_user', 'secret_sauce'),
    ('locked_out_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('error_user', 'secret_sauce'),
    ('visual_user', 'secret_sauce')
])


def test_login_and_product_search(user, password, selenium_driver):
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
    # Verify that you have successfully logged in by checking the presence of the products page title.
    assert driver.find_element(By.XPATH, "//span[@class = 'title']").text == "Products"
    assert driver.find_element(By.XPATH, "//div[@class = 'inventory_item_name ']").text == "Sauce Labs Backpack"
