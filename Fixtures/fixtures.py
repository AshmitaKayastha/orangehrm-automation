# Pytest Fixtures for Playwright

import pytest
from playwright.sync_api import sync_playwright, Page, Browser
from config import BASE_URL, BROWSER, HEADLESS, TIMEOUT
from Utils.common import CommonUtils


@pytest.fixture(scope="session")
def browser_instance():
    """
    Create a browser instance for the test session
    
    Yields:
        Browser instance
    """
    playwright = sync_playwright().start()
    
    if BROWSER.lower() == "chromium":
        browser = playwright.chromium.launch(headless=HEADLESS)
    elif BROWSER.lower() == "firefox":
        browser = playwright.firefox.launch(headless=HEADLESS)
    elif BROWSER.lower() == "webkit":
        browser = playwright.webkit.launch(headless=HEADLESS)
    else:
        browser = playwright.chromium.launch(headless=HEADLESS)
    
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser_instance) -> Page:
    """
    Create a new page for each test
    
    Args:
        browser_instance: Browser instance from session fixture
        
    Yields:
        Page object
    """
    page = browser_instance.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    
    yield page
    
    page.close()


@pytest.fixture
def setup_and_teardown(page):
    """
    Setup and teardown fixture for each test
    
    Args:
        page: Page object
        
    Yields:
        Page object
    """
    CommonUtils.log_message("Test setup started")
    yield page
    CommonUtils.log_message("Test teardown started")
