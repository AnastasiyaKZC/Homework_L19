from selene import have, browser
from allure import step

def test_search():
    browser.config.base_url = 'https://www.wikipedia.org'

    print(f"BASE_URL: {browser.config.base_url}")
    browser.open('/')

    with step('Type search'):
        browser.element('#searchInput').type('Appium')

    with step('Verify content found'):
        results = browser.all('.suggestion-link')
        results.should(have.size_greater_than(0))
        results.first.should(have.text('AppImage'))