import pytest
from dotenv import load_dotenv
from selene import browser

BASE_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    browser.config.window_width = '1900'
    browser.config.window_height = '1080'
    browser.open(BASE_URL)

    yield browser

    browser.quit()
