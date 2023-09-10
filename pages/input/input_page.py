from helpers.page_names import PageNames
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InputPage(BasePage):
    firstNameInputLocator = 'input#firstName'
    lastNameInputLocator ='input#lastName'
    primaryLanguageInputLocator = "//input[@name='primaryProgrammingLanguage']"
    otherLanguageInputLocator = "//input[@name='otherProgrammingLenguages']"
    totalYearsInputLocator = "//input[@name='yearsExperience']"
    cityInputLocator = "//input[@name='city']"

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_input_page_to_load(self):
        input_page_url = self.config_helper.get_base_url() + PageNames.INPUT_FIELDS.value
        print(input_page_url)
        self.wait_until_url_contains(input_page_url)

    """ First Name Input """
    
    def enter_first_name(self, first_name: str):
        first_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.firstNameInputLocator))
        first_name_input.send_keys(first_name)

    def get_first_name(self):
        first_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.firstNameInputLocator))
        return first_name_input.get_attribute('value')

    def clear_first_name(self):
        first_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.firstNameInputLocator))
        first_name_input.clear()

    """ Last Name Input """

    def enter_last_name(self, last_name: str):
        last_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.lastNameInputLocator))
        last_name_input.send_keys(last_name)

    def get_last_name(self):
        last_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.lastNameInputLocator))
        return last_name_input.get_attribute('value')

    def clear_last_name(self):
        last_name_input = self.wait_until_element_located((By.CSS_SELECTOR, self.lastNameInputLocator))
        last_name_input.clear()

    """ Primary Language Input """

    def enter_primary_language(self, primary_language: str):
        primary_language_input = self.wait_until_element_located((By.XPATH, self.primaryLanguageInputLocator))
        primary_language_input.send_keys(primary_language)

    def get_primary_language(self):
        primary_language_input = self.wait_until_element_located((By.XPATH, self.primaryLanguageInputLocator))
        return primary_language_input.get_attribute('value')

    def clear_primary_language(self):
        primary_language_input = self.wait_until_element_located((By.XPATH, self.primaryLanguageInputLocator))
        primary_language_input.clear()
    
    """ Other Language Input """

    def enter_other_language(self, other_language: str):
        other_language_input = self.wait_until_element_located((By.XPATH, self.otherLanguageInputLocator))
        other_language_input.send_keys(other_language)

    def get_other_language(self):
        other_language_input = self.wait_until_element_located((By.XPATH, self.otherLanguageInputLocator))
        return other_language_input.get_attribute('value')

    def clear_other_language(self):
        other_language_input = self.wait_until_element_located((By.XPATH, self.otherLanguageInputLocator))
        other_language_input.clear()

    """ Total Years Input """

    def enter_total_years(self, total_years: str):
        total_years_input = self.wait_until_element_located((By.XPATH, self.totalYearsInputLocator))
        total_years_input.send_keys(total_years)

    def get_total_years(self):
        total_years_input = self.wait_until_element_located((By.XPATH, self.totalYearsInputLocator))
        return total_years_input.get_attribute('value')

    def clear_total_years(self):
        total_years_input = self.wait_until_element_located((By.XPATH, self.totalYearsInputLocator))
        total_years_input.clear()

    """ City Input """

    def enter_city(self, city: str):
        city_input = self.wait_until_element_located((By.XPATH, self.cityInputLocator))
        city_input.send_keys(city)

    def get_city(self):
        city_input = self.wait_until_element_located((By.XPATH, self.cityInputLocator))
        return city_input.get_attribute('value')

    def clear_city(self):
        city_input = self.wait_until_element_located((By.XPATH, self.cityInputLocator))
        city_input.clear()
