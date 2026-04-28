import pytest
import re
from playwright.sync_api import sync_playwright, expect, Page
from Pages.MyInfoQualificationsPage import QualificationsPage
from Locators.MyInfoQualificationsLocators import QualificationsLocators
from config import USERNAME, PASSWORD, BASE_URL, TIMEOUT

@pytest.fixture(scope="function")
def setup(page: Page):
    """Handles login and navigates to the My Info section as a starting point."""
    # 1. Login Logic
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator("input[name='username']").fill(USERNAME)
    page.locator("input[name='password']").fill(PASSWORD)
    page.locator("button[type='submit']").click()
    
    # 2. Ensure dashboard is reached
    page.wait_for_url("**/dashboard/**", timeout=TIMEOUT)
    
    # 3. Navigate to My Info (common starting point for all these tests)
    page.get_by_role("link", name="My Info").click()
    
    return page

def test_MI_100_navigate_to_qualifications(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    expect(setup).to_have_url(re.compile(r".*viewQualifications.*"))

def test_MI_101_add_work_experience(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.add_work_experience("Playwright Corp", "SDET", "2024-01-01", "2025-01-01", "Testing")
    expect(setup.get_by_text("Playwright Corp").first).to_be_visible()

def test_MI_102_edit_work_experience(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.edit_first_record("Updated Company Name")
    # Extended timeout for demo site latency
    expect(setup.get_by_text("Updated Company Name").first).to_be_visible(timeout=10000)

def test_MI_103_delete_work_experience(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.delete_first_record()
    # Checking for the toast is the most reliable way to confirm deletion
    expect(setup.locator(QualificationsLocators.TOAST_MESSAGE)).to_be_visible()

def test_MI_104_add_without_mandatory_fields(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.add_work_experience("", "", "", "", "")
    expect(setup.get_by_text("Required").first).to_be_visible()