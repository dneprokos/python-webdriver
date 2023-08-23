"""
Page Object Model for Home Page
"""

from .base_page import BasePage
from helpers.page_names import PageNames
from helpers.config_helper import ConfigHelper


class HomePage(BasePage):

    # Class initializer. Not a constructor, but a method that is called when an object is instantiated.
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_home_page_to_load(self):
        home_page_url = ConfigHelper().get_base_url() + PageNames.HOME.value
        self.wait_until_url_contains(home_page_url)

        
        

