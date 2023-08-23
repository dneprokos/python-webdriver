"""
These are the tests for the login page.
"""

import time
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_with_valid_credentials_should_be_logged_in(browser):
    # Given Main website page is opened
    browser.get("https://qa-automation-test-site.web.app/login")

    # When the user enters valid username and password and clicks the login button 
    LoginPage(browser).login("test@test.com", "test")

    # Then the user should be logged in  
    assert HomePage(browser).get_url() == "https://qa-automation-test-site.web.app/home"
    
    #time.sleep(10) # wait for 10 seconds. - Just left for example.
    #raise Exception("Incomplete Test") - Just left for example.
