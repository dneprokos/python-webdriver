from pages.drop_down.drop_down_page import DropDownPage
from assertpy import soft_assertions


def test_dropdown_select_value_should_be_selected(browser_after_login):
    # Navigate to the Drop-down page
    drop_down_page = DropDownPage(browser_after_login)
    drop_down_page.navigate()

    # Select a value and verify it is selected
    selected_option = "Steak"
    drop_down_page.select_favorite_food_option(selected_option)

    # Assert that the selected option is correctly displayed
    with soft_assertions():
        assert drop_down_page.get_favorite_food_selected_option() == selected_option