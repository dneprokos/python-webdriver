# Python-WebDriver test project

This Project design to pratice in creation of WebDriver tests using Python programming language

![Config file](/images/python_vs_browsers.png)

# Setup Instructions

## Python Setup

- Install Python of version "3.11" or higher from [Python.org](https://www.python.org/downloads/). Don't forget to include it to PATH variables
- Install pipenv, run `pip install pipenv` from the command line.


## Install dependencies

- In the root of the repository, run "pipenv install" from the command line.

##  Activate a virtual environment

- Run "pipenv shell" from command line to activate virtual environment

## WebDriver Setup

- For Web UI testing, you will need to install the latest versions of the browsers e.g. [Google Chrome](https://www.google.com/chrome/) or/and [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).
- You will also need to install the latest versions of the WebDriver executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for the browsers e.g Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

Note: Please be careful, some of the browser versions and WebDriver executables may be not compatible. So, it's recommended to use latest versions of both if you don't need some specific version

### Example of WebDriver Setup for Windows

1. Create a folder named `C:\Selenium`. Note: It can be any name name
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)


# Code Editor

- I was using Visual Studio Code [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- Poople also recommend [PyCharm](https://www.jetbrains.com/pycharm/)


# Run tests

## Run from command line

- Run command `pipenv run python -m pytest` from the command line

- Run command `pipenv run python -m pytest -n 5` from command line in order to run tests in parallel. Number "5" can be changed to expected number of threads

- Run command `pipenv run python -m pytest -s` from command line to run all the tests and see all printed outputs

- Run command `pipenv run python -m pytest -m 'smoke'` from command line when you want to add test category

## Run configuration

- Edit "config.json" file in order to update test config
- At this moment you can change
    - browser (Supported values are: "Firefox", "Chrome", "Headless Chrome")
    - implicit_wait (Just integer value for implicit timeout)
    - explicit_wait (Just integer value for explicit timeout)

![Config file](/images/config_json.png)

