"""
These are the tests for the login page.
"""
from selenium.common.exceptions import NoAlertPresentException
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from helpers.page_names import PageNames
from helpers.config_helper import ConfigHelper
from assertpy import soft_assertions

def test_login_with_valid_credentials_should_be_logged_in(browser):
    # Given Main website page is opened
    browser.get(ConfigHelper().get_base_url())

    # Get credentials from config
    credentials = ConfigHelper().get_login_credentials()
    username = credentials["username"]
    password = credentials["password"]

    # When the user enters valid username and password and clicks the login button 
    LoginPage(browser).login(username, password)

    # Then the user should be logged in
    with soft_assertions():  
        assert HomePage(browser).get_url() == f"{ConfigHelper().get_base_url()}{PageNames.HOME.value}"
        assert HomePage(browser).get_logo_text() == "QA Automation Web"


def test_login_with_invalid_password_should_not_be_logged_in(browser):
    # Arrange
    browser.get(ConfigHelper().get_base_url())

    # Get credentials from config
    credentials = ConfigHelper().get_login_credentials()
    username = credentials["username"]

    # Act
    LoginPage(browser).login(username, "wrong")

    # Assert
    try:
        alert = browser.switch_to.alert
        assert alert.text == "Invalid credentials", "The alert message is not as expected."
        alert.accept()
    except NoAlertPresentException:
        assert False, "No alert was presented when invalid credentials were used."    
