from assertpy import soft_assertions

import pytest
from pages.check_box.check_box_names import CheckBoxNames
from pages.check_box.check_boxes_page import CheckboxesPage

def test_mark_indeterminate_checks_all_checkboxes(browser_after_login):
    # Given the user is logged in and on the checkboxes page
    check_boxes_page = CheckboxesPage(browser_after_login)
    check_boxes_page.click_navigation_menu_button('Check-boxes')
    check_boxes_page.wait_for_checkboxes_page_to_load()

    # When the user clicks indeterminate checkbox
    check_boxes_page.click_checkbox(CheckBoxNames.indeterminate)
    
    # Then all checkboxes should be checked
    with soft_assertions():
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.indeterminate) == True
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.primary) == True
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.accent) == True
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.warn) == True


def test_mark_and_unmark_indeterminate_unchecks_all_checkboxes(browser_after_login):
    # Given the user is logged in and on the checkboxes page
    check_boxes_page = CheckboxesPage(browser_after_login)
    check_boxes_page.click_navigation_menu_button('Check-boxes')
    check_boxes_page.wait_for_checkboxes_page_to_load()

    # When the user clicks indeterminate checkbox
    check_boxes_page.click_checkbox(CheckBoxNames.indeterminate)
    
    # And then clicks indeterminate checkbox again
    check_boxes_page.click_checkbox(CheckBoxNames.indeterminate)
    
    # Then all checkboxes should be unchecked
    with soft_assertions():
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.indeterminate) == False
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.primary) == False
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.accent) == False
        assert check_boxes_page.is_checkbox_checked(CheckBoxNames.warn) == False

@pytest.mark.parametrize('check_box_name', [CheckBoxNames.primary, CheckBoxNames.accent, CheckBoxNames.warn])
def test_mark_specified_checkbox(browser_after_login, check_box_name):
    # Given the user is logged in and on the checkboxes page
    check_boxes_page = CheckboxesPage(browser_after_login)
    check_boxes_page.click_navigation_menu_button('Check-boxes')
    check_boxes_page.wait_for_checkboxes_page_to_load()
    # When the user clicks specified checkbox
    check_boxes_page.click_checkbox(check_box_name)
    
    # Then the specified checkbox should be checked
    with soft_assertions():
        assert check_boxes_page.is_checkbox_checked(check_box_name) == True
        
        expected_unchecked_checkboxes = [x for x in CheckBoxNames if x != check_box_name]
        for checkbox in expected_unchecked_checkboxes:
            assert check_boxes_page.is_checkbox_checked(checkbox) == False
    