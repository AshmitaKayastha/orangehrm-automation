import pytest
from config import BASE_URL, USERNAME, PASSWORD
from Pages.MyInfoJobPage import MyInfoJobPage
from Assertions.myInfoJobAssertions import MyInfoJobAssertions

@pytest.fixture
def job_page(page):
    """Fixture to handle login and navigation to the Job tab once per test."""
    page.goto(BASE_URL)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")
    
    job = MyInfoJobPage(page)
    job.open_my_info()
    job.open_job_tab()
    page.wait_for_load_state("networkidle")
    return job

def test_MI_081_navigate_to_job_tab(job_page):
    """Test navigation to Job tab."""
    MyInfoJobAssertions.assert_job_tab_navigated(job_page)

def test_MI_082_to_088_verify_job_fields(job_page):
    """Verify all job detail fields are visible (Joined Date, Title, Category, etc)."""
    MyInfoJobAssertions.assert_all_job_fields_visible(job_page)

# def test_MI_089_contract_fields_visibility(job_page):
#     """Verify Contract Start and End Date fields appear when toggle is enabled."""
#     # Enable the contract toggle
#     job_page.enable_contract_details()
    
#     # Assert fields are visible
#     MyInfoJobAssertions.assert_contract_fields_visible(job_page)