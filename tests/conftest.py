"""
This module contains shared fixtures. 
The name of the module is important, as pytest will discover fixtures in files named conftest.py.
"""

import json
import pytest
import os
from helpers.navigation_helper import NavigationHelper
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import datetime  # Import the datetime module

@pytest.fixture
def config(scope="session"): # scope="session" means that the fixture is initialized only once, before all tests are run. Other possible values are "function", "class", and "module".
  
  # Read the file
  with open("config.json") as conf_file:
    config = json.load(conf_file)

  # Assert values are acceptable
  assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
  assert isinstance(config["implicit_wait"], int)
  assert config["implicit_wait"] > 0

  # Return config so it can be used
  return config


@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance
  if config['browser'] == 'Firefox':
    b = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

  elif config['browser'] == 'Chrome':
    b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  elif config['browser'] == 'Headless Chrome':
    opts = webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')
  
  # Maximize the browser window
  b.maximize_window()

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()

@pytest.fixture(scope="function")
def browser_after_login(browser):
  NavigationHelper(browser).open_base_page_and_login_with_session_storage()
  return browser

# Define a custom pytest hook to take a screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Check if the test failed
    if rep.failed:
        try:
            browser = item.funcargs['browser']
            # Get the current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Build the screenshot filename
            screenshot_dir = 'failed_test_screenshots'
            os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist
            screenshot_name = f'{item.name}_{current_time}.png'
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            # Capture a screenshot using WebDriver and save it to the specified path
            browser.save_screenshot(screenshot_path)
        except (WebDriverException, KeyError):
            pass  # Handle exceptions gracefully
