import pytest
import re
from playwright.sync_api import sync_playwright, expect, Page
from Pages.MyInfoQualificationsPage import QualificationsPage
from Locators.MyInfoQualificationsLocators import QualificationsLocators
from config import USERNAME, PASSWORD, BASE_URL, TIMEOUT

@pytest.fixture(scope="function")
def setup(page: Page):
    """Handles login and navigates to the My Info section as a starting point."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator("input[name='username']").fill(USERNAME)
    page.locator("input[name='password']").fill(PASSWORD)
    page.locator("button[type='submit']").click()
    
    page.wait_for_url("**/dashboard/**", timeout=TIMEOUT)
    
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
    expect(setup.get_by_text("Updated Company Name").first).to_be_visible(timeout=10000)

def test_MI_103_delete_work_experience(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.delete_first_record()
    expect(setup.locator(QualificationsLocators.TOAST_MESSAGE)).to_be_visible()

def test_MI_104_add_without_mandatory_fields(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.add_work_experience("", "", "", "", "")

    expect(setup.get_by_text("Required").first).to_be_visible()

def test_MI_105_add_education_record(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    qual_page.add_education(
        level="Bachelor's Degree",
        institute="University of Wolverhampton",
        major="Computer Science",
        year="2024",
        gpa="3.9",
        start_date="2020-01-09",
        end_date="2024-05-15"
    )
    

    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()
    
    expect(setup.get_by_text("Bachelor's Degree").first).to_be_visible()

def test_MI_106_edit_education_record(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.edit_education_institute("Seneca Polytechnic")
   
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

def test_MI_107_delete_education_record(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
  
    target_record = "Seneca Polytechnic" 
    
    qual_page.delete_education_record()
    
    expect(setup.get_by_text(target_record)).to_be_hidden(timeout=10000)


def test_MI_108_add_skill(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.add_skill("Java", "5", "Proficient in backend development")
    

def test_MI_109_edit_skill(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    qual_page.edit_skill_experience("8")
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

def test_MI_110_delete_skill(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()

    skill_to_delete = "Java"
    qual_page.delete_skill_record(skill_to_delete)
    expect(setup.get_by_text(skill_to_delete)).to_be_hidden(timeout=10000)

# test_qualifications.py
def test_MI_111_add_language(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    # Ensure these strings match the text inside your OrangeHRM dropdowns exactly
    qual_page.add_language("French", "Writing","Good", "Testing MI-111")
    
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

# MI-112: Test Editing a Language
# test_qualifications.py

def test_MI_112_edit_language(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.edit_language("English", "Poor")
    
    # Assert success
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

# MI-113: Test Deleting a Language
def test_MI_113_delete_language(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    target_lang = "French"
    qual_page.delete_language(target_lang)
    
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()
    expect(setup.get_by_text(target_lang)).to_be_hidden()

def test_MI_114_add_license(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    license_name = "Cisco Certified Network Professional (CCNP)"
    license_no = "LIC-999"
    qual_page.add_license(license_name, license_no, "2024-01-01", "2026-01-01")
        
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

# MI-115: Edit License Number
def test_MI_115_edit_license(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    target_license = "Cisco Certified Network Professional (CCNP)"
    new_num = "LIC-2026-999"
    
    qual_page.edit_license_number(target_license, new_num)
    
    # Assertions
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()
    # Verify the specific row contains the new number
    license_row = setup.locator(".oxd-table-card").filter(has_text=target_license)
    expect(license_row).to_contain_text(new_num)

# MI-116: Delete License
def test_MI_116_delete_license(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    
    license_to_remove = "Cisco Certified Network Professional (CCNP)"
    
    qual_page.delete_license(license_to_remove)
    
    # Assertions
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()
    # Verify the text is no longer in the table
    expect(setup.get_by_text(license_to_remove)).to_be_hidden()