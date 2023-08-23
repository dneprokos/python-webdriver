"""
Page Object Model for Home Page
"""

from .base_page import BasePage

class HomePage(BasePage):

    # Class initializer. Not a constructor, but a method that is called when an object is instantiated.
    def __init__(self, driver):
        super().__init__(driver)

