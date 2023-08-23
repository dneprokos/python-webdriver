"""
These are the tests for the login page.
"""

import time

def test_login_with_valid_credentials_should_be_logged_in(browser):
    # Given Main website page is opened
    # TODO
    browser.get("https://qa-automation-test-site.web.app/login")
    time.sleep(10) # wait for 10 seconds. Will be removed later

    # When the user enters user name ""
    # TODO

    # And the user enters password ""
    # TODO

    # And the user clicks the login button
    # TODO

    # Then the user should be logged in
    # TODO

    raise Exception("Incomplete Test")
