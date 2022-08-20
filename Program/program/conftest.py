import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'Chrome' or browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'safari' or browser == 'Safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):               # this will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):      # this will return the Browser value to setup method
    return request.config.getoption("--browser")