from helpers.config_helper import ConfigHelper
from helpers.page_names import PageNames
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DropDownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        # Navigate to the Drop-down page using the navigation workaround
        dropdown_button = self.wait_until_element_clickable((By.XPATH, "//a[@href='/drop-down']"))
        dropdown_button.click()

        # Verify the page header is loaded correctly
        header = self.wait_until_element_located((By.XPATH, "//h4"))
        assert header.text == "mat-select", "Drop-down page header is incorrect"

    def select_favorite_food_option(self, favorite_food):
        # Open the drop-down menu
        dropdown = self.wait_until_element_clickable((By.ID, "mat-select-0"))
        dropdown.click()

        # Select the desired option
        option = self.wait_until_element_clickable((By.XPATH, f"//mat-option//span[normalize-space(text())='{favorite_food}']"))
        option.click()

    def get_favorite_food_selected_option(self):
        # Get the currently selected value
        selected_value = self.wait_until_element_located((By.CSS_SELECTOR, "#mat-select-value-1"))
        return selected_value.text


