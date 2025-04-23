import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from config import config


def android_mobile_config():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": config.android_platform_version,
        "deviceName": config.android_device_name,
        "app": config.android_app,
        'bstack:options': {
            "projectName": config.project_name,
            "buildName": config.build_name,
            "sessionName": config.session_name,
            "userName": config.browserstack_username,
            "accessKey": config.browserstack_access_key
        }
    })
    return options


def ios_mobile_config():
    options = XCUITestOptions().load_capabilities({
        "platformName": "ios",
        "platformVersion": config.ios_platform_version,
        "deviceName": config.ios_device_name,
        "app": config.ios_app,
        'bstack:options': {
            "projectName": config.project_name,
            "buildName": config.build_name,
            "sessionName": config.session_name,
            "userName": config.browserstack_username,
            "accessKey": config.browserstack_access_key
        }
    })
    return options


@pytest.fixture(params=["android", "ios"])
def setup_mobile(request):
    """
    Fixture for setting up mobile testing environment.
    Supports both Android and iOS platforms.
    """
    platform = request.param
    
    if platform == "android":
        options = android_mobile_config()
    else:
        options = ios_mobile_config()

    browser.config.driver = webdriver.Remote(
        command_executor=config.browserstack_url,
        options=options
    )

    browser.config.timeout = 10.0

    yield

    # Получаем статус теста
    test_status = "passed" if request.node.rep_call.passed else "failed"
    
    # Отправляем статус в BrowserStack
    browser.driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"' + test_status + '"}}'
    )

    # Делаем скриншот перед закрытием браузера
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="test_finished",
        attachment_type=AttachmentType.PNG
    )
    
    browser.quit()


@pytest.fixture
def android_only(request):
    """
    Fixture for Android-only tests
    """
    options = android_mobile_config()
    
    browser.config.driver = webdriver.Remote(
        command_executor=config.browserstack_url,
        options=options
    )

    browser.config.timeout = 10.0

    yield

    # Получаем статус теста
    test_status = "passed" if request.node.rep_call.passed else "failed"
    
    # Отправляем статус в BrowserStack
    browser.driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"' + test_status + '"}}'
    )

    # Делаем скриншот перед закрытием браузера
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="test_finished",
        attachment_type=AttachmentType.PNG
    )
    
    browser.quit()


@pytest.fixture
def ios_only(request):
    """
    Fixture for iOS-only tests
    """
    options = ios_mobile_config()
    
    browser.config.driver = webdriver.Remote(
        command_executor=config.browserstack_url,
        options=options
    )

    browser.config.timeout = 10.0

    yield

    # Получаем статус теста
    test_status = "passed" if request.node.rep_call.passed else "failed"
    
    # Отправляем статус в BrowserStack
    browser.driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"' + test_status + '"}}'
    )

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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep) 