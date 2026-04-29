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