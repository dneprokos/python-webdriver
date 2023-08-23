"""
This module contains tests for the radio buttons page.
"""

import pytest
from pages.radio_buttons_page import RadioButtonsPage
from helpers.navigation_helper import NavigationHelper, PageNames

@pytest.mark.parametrize('button_name', ['Winter', 'Spring', 'Summer', 'Autumn'])
def test_select_radio_button_with_expected_value(browser, button_name):
    # Given the user is logged in and on the radio buttons page
    NavigationHelper(browser).open_base_page_and_login_with_session_storage()
    radio_btn_page = RadioButtonsPage(browser)
    radio_btn_page.click_navigation_menu_button('Radio-buttons')
    radio_btn_page.wait_until_url_contains(PageNames.RADIO_BUTTONS.value)
    
    # When the user selects a radio button
    RadioButtonsPage(browser).click_radio_button(button_name)

    # Then the radio button should be selected
    assert RadioButtonsPage(browser).get_current_favorite_season() == f"Your favorite season is: {button_name}"