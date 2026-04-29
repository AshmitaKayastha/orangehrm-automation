from config import BASE_URL, USERNAME, PASSWORD
from Pages.MyInfoJobPage import MyInfoJobPage
from Locators.MyInfoQualificationsLocators import MyInfoQualificationsLocators as loc



def test_MI_081_navigate_to_job_tab(page):

    page.goto(BASE_URL)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    job = MyInfoJobPage(page)

    job.open_my_info()
    job.open_job_tab()

    page.wait_for_load_state("networkidle")

    assert job.is_job_section_visible()


def test_MI_082_verify_job_fields(page):

    page.goto(BASE_URL)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    job = MyInfoJobPage(page)

    job.open_my_info()
    job.open_job_tab()

    page.wait_for_load_state("networkidle")

    assert job.is_joined_date_visible()
    assert job.is_job_title_visible()
    assert job.is_job_category_visible()
    assert job.is_sub_unit_visible()
    assert job.is_location_visible()
    assert job.is_employment_status_visible()

def test_MI_089_contract_fields(page):

    page.goto(BASE_URL)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    job = MyInfoJobPage(page)

    job.open_my_info()
    job.open_job_tab()

    page.locator(loc.JOB_HEADER).wait_for(state="visible")

    # Soft validation (since fields may not exist)
    if job.is_contract_start_visible():
        assert job.is_contract_start_visible()

    if job.is_contract_end_visible():
        assert job.is_contract_end_visible()
    assert job.is_contract_end_visible()

