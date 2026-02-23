import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def selenium_driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--guest")
    driver = webdriver.Chrome(chrome_opt)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)  # Implicit wait to handle timing issues


    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()
