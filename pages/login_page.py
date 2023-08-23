"""
Page Object Model for Login Page
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    
    # --- Class initializer. Not a constructor, but a method that is called when an object is instantiated.
    def __init__(self, driver):
        super().__init__(driver)

    # --- Locators
    BY_USERNAME_FIELD_ID = (By.ID, "login") 
    BY_PASSWORD_FIELD_ID = (By.ID, "password")
    BY_LOGIN_BTN_ID = (By.ID, "loginBtn")

    # --- Methods
   
    # Enter the username in the username field
    def enter_username(self, username):
        username_field = self.wait_until_element_located(self.BY_USERNAME_FIELD_ID)
        username_field.send_keys(username)

    # Enter the password in the password field
    def enter_password(self, password):
        password_field = self.wait_until_element_located(self.BY_PASSWORD_FIELD_ID)
        password_field.send_keys(password)

    # Click the login button
    def click_login_button(self):
        login_button = self.wait_until_element_clickable(self.BY_LOGIN_BTN_ID)
        login_button.click()

    # Perform the login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    