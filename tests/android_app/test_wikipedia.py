from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(make_screenshot):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        make_screenshot("search_click")
        
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
        make_screenshot("after_typing")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
        make_screenshot("search_results")


def test_open_article(make_screenshot):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        make_screenshot("search_click")
        
        search_input = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search_input.type('Hello')
        make_screenshot("after_typing")

    with step('Click on article'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        
        # Находим и кликаем на первую статью
        first_article = results.first
        make_screenshot("before_click_article")
        
        first_article.click()
        make_screenshot("after_click_article")