import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": "iakivkramarenko_qKHOLN",
            "accessKey": "FSHAmndKHW3XsDkgm5zT"
        }
    })

    browser.config.driver = webdriver.Remote(
        command_executor='http://hub.browserstack.com/wd/hub',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    # Делаем скриншот перед закрытием браузера
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="test_finished",
        attachment_type=AttachmentType.PNG
    )
    
    browser.quit()


@pytest.fixture
def make_screenshot():
    def _make_screenshot(name: str):
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )
    return _make_screenshot