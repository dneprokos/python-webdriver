from helpers.config_helper import ConfigHelper
from helpers.page_names import PageNames
from pages.base_page import BasePage
from pages.check_box.check_box_names import CheckBoxNames
from selenium.webdriver.common.by import By


class CheckboxesPage(BasePage):
        indeterminate_checkbox = 'mat-checkbox.mat-primary.example-margin'
        primary_checkbox = 'mat-checkbox.mat-primary.ng-valid'
        accent_checkbox = 'mat-checkbox.mat-accent'
        warn_checkbox = 'mat-checkbox.mat-warn'
               
        # Class initializer. Not a constructor, but a method that is called when an object is instantiated.
        def __init__(self, driver):
            super().__init__(driver)
    
        def wait_for_checkboxes_page_to_load(self):
            check_boxes_page_url = ConfigHelper().get_base_url() + PageNames.CHECKBOXES.value
            self.wait_until_url_contains(check_boxes_page_url)

        # Clicks specified checkbox
        def click_checkbox(self, checkbox_name: CheckBoxNames):
            checkbox_selector = self._resolve_checkbox_selector(checkbox_name)
            element = self.wait_until_element_clickable((By.CSS_SELECTOR, checkbox_selector))
            element.click()

        def is_checkbox_checked(self, checkbox_name: CheckBoxNames):
            checkbox_selector = f'{self._resolve_checkbox_selector(checkbox_name)} input'
            element = self.wait_until_element_located((By.CSS_SELECTOR, checkbox_selector))
            return element.is_selected()
            
        def _resolve_checkbox_selector(self, checkbox_name: CheckBoxNames):
            if checkbox_name == CheckBoxNames.indeterminate:
                return self.indeterminate_checkbox
            elif checkbox_name == CheckBoxNames.primary:
                return self.primary_checkbox
            elif checkbox_name == CheckBoxNames.accent:
                return self.accent_checkbox
            elif checkbox_name == CheckBoxNames.warn:
                return self.warn_checkbox
            else:
                raise Exception(f'Checkbox "{checkbox_name}" is not supported')