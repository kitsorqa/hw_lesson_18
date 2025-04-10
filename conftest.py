import pytest
from selene import browser
from utils.attach import add_screenshot


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    add_screenshot(browser)
    browser.quit()