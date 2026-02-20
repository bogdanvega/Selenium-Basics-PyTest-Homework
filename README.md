# Selenium-Basics-PyTest-Homework

## Task 1 (Web Automation with Selenium):

I am tasked with automating the following actions on a demo e-commerce website:
URL: https://www.saucedemo.com/

1. **Login Automation** 
    Automate the login process for the website using provided test credentials. 
2. **Product Search Verification** 
    Navigate to the products page after login, and verify the presence of specific product names.
_________________________________________________________________________________________________________________
1. **Login to the Website**
    - Navigate to https://www.saucedemo.com/.
    - Locate and interact with the login form:
        - Enter the username: `standard_user`.
        - Enter the password: `secret_sauce`.
        - Click the "Login" button.
    - Verify that you have successfully logged in by checking the presence of the products page title or elements.
2. **Verify Specific Product**
    - After logging in, locate and verify the presence of the following product:
        - Product Name: **"Sauce Labs Backpack"**.
    - Assert that the product name is displayed on the page.

## Task 2 (Parameterization and Fixtures)

Enhanced the login script to include parameterization and create a driver fixture. Made sure to test all the usernames available on https://www.saucedemo.com

## Task 3 (Register User)

Wrote a Selenium script that does the following:
1. Launch browser
2. Navigate to url ['http://automationexercise.com'](https://automationexercise.com/)
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
