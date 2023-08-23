from helpers.config_helper import ConfigHelper
from .page_names import PageNames

class NavigationHelper:
    def __init__(self, driver):
        self.driver = driver
        self.config_helper = ConfigHelper()
    
    def open_base_page_and_login_with_session_storage(self) -> None:
        base_url = self.config_helper.get_base_url()
        self.driver.get(base_url)
        self.driver.execute_script(
            """
            window.sessionStorage.setItem('user', 'admin');
            """
        )
        self.driver.refresh()
