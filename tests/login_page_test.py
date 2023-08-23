"""
These are the tests for the login page.
"""
from pages.login_page import LoginPage
from pages.home_page import HomePage
from helpers.page_names import PageNames
from helpers.config_helper import ConfigHelper

def test_login_with_valid_credentials_should_be_logged_in(browser):
    # Given Main website page is opened
    browser.get(ConfigHelper().get_base_url())

    # When the user enters valid username and password and clicks the login button 
    LoginPage(browser).login("test@test.com", "test")

    # Then the user should be logged in  
    assert HomePage(browser).get_url() == f"{ConfigHelper().get_base_url()}{PageNames.HOME.value}"
