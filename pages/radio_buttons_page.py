"""
This module contains the RadioButtonsPage,
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from helpers.page_names import PageNames

class RadioButtonsPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_radio_button(self, radio_button_name):
        radio_button_xpath = f'//mat-radio-button[.//span[contains(text(), "{radio_button_name}")]]'
        radio_button = self.wait_until_element_located((By.XPATH, radio_button_xpath))
        radio_button.click()

    def get_current_favorite_season(self):
        favorite_season_element = self.wait_until_element_located(
            (By.XPATH, '//div[contains(text(), "Your favorite season is:")]')
        )
        return favorite_season_element.text
    
    def wait_for_radio_buttons_page_to_load(self):
        radio_buttons_page_url = self.config_helper.get_base_url() + PageNames.RADIO_BUTTONS.value
        self.wait_until_url_contains(radio_buttons_page_url)