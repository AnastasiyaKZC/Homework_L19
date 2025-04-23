from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_ios_search(ios_only, make_screenshot):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        make_screenshot("search_click")
        
        search_input = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        search_input.type('Hello')
        make_screenshot("after_typing")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ACCESSIBILITY_ID, 'article_title'))
        results.should(have.size_greater_than(0))
        make_screenshot("search_results")


def test_ios_open_article(ios_only, make_screenshot):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        make_screenshot("search_click")
        
        search_input = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        search_input.type('Hello')
        make_screenshot("after_typing")

    with step('Click on article'):
        results = browser.all((AppiumBy.ACCESSIBILITY_ID, 'article_title'))
        results.should(have.size_greater_than(0))
        
        # Находим и кликаем на первую статью
        first_article = results.first
        make_screenshot("before_click_article")
        
        first_article.click()
        make_screenshot("after_click_article") 