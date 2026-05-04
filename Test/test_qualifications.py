import pytest
import re
import os
from playwright.sync_api import sync_playwright, expect, Page
from Pages.MyInfoQualificationsPage import QualificationsPage
from Locators.MyInfoQualificationsLocators import QualificationsLocators
from config import USERNAME, PASSWORD, BASE_URL, TIMEOUT

@pytest.fixture(scope="function")
def setup(page: Page):
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
    level_to_find = "Bachelor's Degree"
    new_name = "Seneca Polytechnic"
    qual_page.edit_education_institute(level_to_find, new_name)

def test_MI_107_delete_education_record(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    target_level = "Bachelor's Degree"
    qual_page.delete_education_record(target_level)
    expect(setup.locator(".oxd-table-card").filter(has_text=target_level)).not_to_be_visible()


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


def test_MI_111_add_language(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.add_language("French", "Writing","Good", "Testing MI-111")
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()


def test_MI_112_edit_language(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.edit_language("French", "Poor")
    expect(setup.locator(QualificationsLocators.SUCCESS_TOAST)).to_be_visible()

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
    selected_license = qual_page.add_first_available_license()
    expect(setup.get_by_text(re.compile("Successfully Saved", re.IGNORECASE))).to_be_visible()
    license_table = setup.locator("div.orangehrm-background-container").filter(
        has=setup.get_by_role("heading", name="License")
    )
    expect(license_table).to_contain_text(selected_license)

def test_MI_115_edit_first_license(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    added_license = qual_page.add_first_available_license()
    qual_page.edit_first_license_record("LIC-999")
    expect(setup.get_by_text("Successfully Updated")).to_be_visible()

def test_MI_116_delete_first_license(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    qual_page.delete_first_license_record()
    expect(setup.get_by_text("Successfully Deleted")).to_be_visible()

def test_MI_117_add_attachment(setup):
    qual_page = QualificationsPage(setup)
    qual_page.navigate_to_qualifications()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "test_upload.txt"
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "w") as f:
        f.write("Automated test attachment content.")
    qual_page.add_attachment(file_path, "Certification Upload Test")
    expect(setup.get_by_text(re.compile("Successfully Saved", re.IGNORECASE))).to_be_visible()
    attachment_table = setup.locator(QualificationsLocators.ATTACH_RECORDS_TABLE)
    expect(attachment_table).to_contain_text(file_name)