import pytest
from pages.input.input_page import InputPage
from assertpy import soft_assertions

@pytest.mark.smoke
def test_enter_values_to_the_fields(browser_after_login):
    # Given the user is logged in and on the input page
    input_page = InputPage(browser_after_login)
    input_page.click_navigation_menu_button('Input fields')
    input_page.wait_for_input_page_to_load()

    # When the user enters values to the fields
    first_name = 'John'
    last_name = 'Doe'
    primary_language = 'English'
    other_language = 'Spanish'
    total_years = '5'
    city = 'New York'

    input_page.enter_first_name(first_name)
    input_page.enter_last_name(last_name)
    input_page.enter_primary_language(primary_language)
    input_page.enter_other_language(other_language)
    input_page.enter_total_years(total_years)
    input_page.enter_city(city)

    # Then the values should be entered
    with soft_assertions():
        assert input_page.get_first_name() == first_name
        assert input_page.get_last_name() == last_name
        assert input_page.get_primary_language() == primary_language
        assert input_page.get_other_language() == other_language
        assert input_page.get_total_years() == total_years
        assert input_page.get_city() == city
