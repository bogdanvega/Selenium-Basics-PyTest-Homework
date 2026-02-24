import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def selenium_driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    chrome_options = Options()
    chrome_options.add_argument("--guest")

    # Get absolute path to project root
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Path to extension
    extension_path = os.path.join(project_root, "ad_block.crx")
    print(f"Extension path: {extension_path}")

    # Add extension
    chrome_options.add_extension(extension_path)

    # Start driver (Selenium 4 style)
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)  # Implicit wait to handle timing issues

    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()
