"""
This module contains shared fixtures. 
The name of the module is important, as pytest will discover fixtures in files named conftest.py.
"""

import json
import pytest
import selenium.webdriver

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
    b = selenium.webdriver.Firefox()

  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome()

  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)

  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()