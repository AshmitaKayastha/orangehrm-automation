# Pytest configuration and fixtures
import sys
import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, Page, Browser

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import configuration
from config import BASE_URL, BROWSER, HEADLESS, TIMEOUT
from Utils.common import CommonUtils

# Ensure all imports work correctly
try:
    from Pages.login_page import LoginPage
    from Locators.login_locators import LoginLocators
    from Assertions.assertions import LoginAssertions
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure all required files are in place")
    raise


@pytest.fixture(scope="session")
def browser_instance():
    """
    Create a browser instance for the test session
    """
    playwright = sync_playwright().start()

   
    SLOW_MO = 1000 

    if BROWSER.lower() == "chromium":
        browser = playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )
    elif BROWSER.lower() == "firefox":
        browser = playwright.firefox.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )
    elif BROWSER.lower() == "webkit":
        browser = playwright.webkit.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )
    else:
        browser = playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )

    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser_instance) -> Page:
    """
    Create a new page for each test
    """
    page = browser_instance.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page

    page.close()


@pytest.fixture
def setup_and_teardown(page):
    """
    Setup and teardown fixture for each test
    """
    CommonUtils.log_message("Test setup started")
    yield page
    CommonUtils.log_message("Test teardown started")