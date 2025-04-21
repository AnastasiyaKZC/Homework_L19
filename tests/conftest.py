import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def browser_config():
    # Настройка драйвера и других параметров браузера
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.timeout = 5.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()