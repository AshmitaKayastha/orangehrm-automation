import pytest
import re
from playwright.sync_api import sync_playwright, expect, Page
from Pages.emergency_contact_page import EmergencyContactPage
from config import USERNAME, PASSWORD, BASE_URL, TIMEOUT


@pytest.fixture(scope="function")
def setup():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator("input[name='username']").fill(USERNAME)
    page.locator("input[name='password']").fill(PASSWORD)
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/dashboard/**", timeout=TIMEOUT)
    page.get_by_role("link", name="My Info").click()
    yield page
    context.close()
    browser.close()
    playwright.stop()
    """return page"""

def test_navigate_to_emergency_contact(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    expect(setup).to_have_url(re.compile(r".*viewEmergencyContacts.*"))
    print("Successfully navigated to Emergency Contacts page")

def test_verify_add_button_displayed(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    assert emergency_page.is_add_button_displayed(), \
        "Add button is NOT displayed"
    print("Add button is displayed successfully")

def test_add_new_emergency_contact(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_add_button()
    emergency_page.add_contact_required_fields("mack","Brother","9876543210")
    print("Contact added successfully")

def test_add_new_emergency_contact_without_name(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_add_button()
    emergency_page.add_contact_without_name("Brother","9876543210")
    print("Validation checked for mandatory Name field")

def test_add_new_emergency_contact_without_relationship(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_add_button()
    emergency_page.add_contact_without_relationship("mack","9876543210")
    print("Validation checked for mandatory Relationship field")

def test_edit_emergency_contact(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_edit_for_contact("mack")
    print("Edit button clicked successfully")

def test_cancel_emergency_contact(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_add_button()
    emergency_page.add_contact_required_fields_for_cancel("mack","Brother","9876543210")
    print("cancelled successfully")

def test_delete_emergency_contact(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_delete_for_contact("mack")
    emergency_page.confirm_delete()
    print("Contact deleted successfully")

    # Verify Emergency Contact Table Columns
# -------------------------------------------------
def test_verify_emergency_contact_table_columns(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    assert emergency_page.verify_name_column()
    assert emergency_page.verify_relationship_column()
    assert emergency_page.verify_home_telephone_column()
    assert emergency_page.verify_mobile_column()
    assert emergency_page.verify_work_telephone_column()
    print("All table columns verified successfully")
# -----------------------------
# Attachment Add Button
# -----------------------------
def test_click_attachment_add_button(setup):
    emergency_page = EmergencyContactPage(setup)
    emergency_page.navigate_to_emergency_contacts()
    emergency_page.click_attachment_add_button()
    print("Attachment Add button clicked") 
    # Upload file
    emergency_page.upload_attachment_file()
    print("Browse button clicked successfully")
    # Download file
    emergency_page.download_attachment() 
if __name__ == "__main__":
    pytest.main(["-v"])