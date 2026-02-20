from conftest import selenium_driver  # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

URL = 'https://automationexercise.com/'


def test_register_user(selenium_driver):
    driver = selenium_driver
    # Navigate to the desired website
    driver.get(URL)
    # Wait for 3 seconds to allow the page to load completely
    time.sleep(3)
    # Verify that home page is visible successfully (orange "Home" text means Home is loaded)
    home = driver.find_element(By.XPATH, "//a[text()=' Home']")
    assert 'color: orange;' in home.get_attribute("style")
    # Click on 'Signup / Login' button
    driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()
    time.sleep(2)
    # Verify 'New User Signup!' is visible
    assert driver.find_element(By.XPATH, "//div[@class = 'signup-form']/h2").text == "New User Signup!"
    time.sleep(2)
    # Enter name and email address
    driver.find_element(By.XPATH, "//input[@data-qa = 'signup-name']").send_keys("Bogdan")
    driver.find_element(By.XPATH, "//input[@data-qa = 'signup-email']").send_keys("myemail@bogdan.com")
    # Click 'Signup' button
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@data-qa = 'signup-button']").click()
    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//div[@class = 'login-form']/h2/b").text == "ENTER ACCOUNT INFORMATION"
    # Fill details: Title, Name, Email, Password, Date of birth
    driver.find_element(By.XPATH, "//div[@id = 'uniform-id_gender1']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("123456")
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id = 'days']/option[@value = '23']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id = 'months']/option[@value = '10']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id = 'years']/option[@value = '1990']").click()
    # Select checkbox 'Sign up for our newsletter!'
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'newsletter']").click()
    # Select checkbox 'Receive special offers from our partners!'
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'optin']").click()
    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'first_name']").send_keys("Bogdan")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'last_name']").send_keys("Vega")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'company']").send_keys("Vega's Go Out")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'address1']").send_keys("Baker Str. 27, Vega's Go Out")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'address2']").send_keys("App. 1")
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id = 'country']/option[@value = 'United States']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'state']").send_keys("Florida")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'city']").send_keys("Miami")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'zipcode']").send_keys("1111")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id = 'mobile_number']").send_keys("123456789")
    # Click 'Create Account button'
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@data-qa = 'create-account']").click()
    # Verify that 'ACCOUNT CREATED!' is visible
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h2[@data-qa = 'account-created']").text == "ACCOUNT CREATED!"
    # Click 'Continue' button
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@data-qa = 'continue-button']").click()
    # Verify that 'Logged in as username' is visible
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/li/a/b").text == "Bogdan"
    # Click 'Delete Account' button
    time.sleep(2)
    driver.find_element(By.XPATH, "//i[@class = 'fa fa-trash-o']").click()
    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h2[@data-qa = 'account-deleted']").text == "ACCOUNT DELETED!"
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@data-qa = 'continue-button']").click()
    time.sleep(3)
