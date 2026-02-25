import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def selenium_driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--guest")
    chrome_options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")
    chrome_options.add_argument("--disable-site-isolation-trials")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-popup-blocking")

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2,
        "profile.default_content_setting_values.images": 2
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Start driver (Selenium 4 style)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)  # Implicit wait to handle timing issues

    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()
