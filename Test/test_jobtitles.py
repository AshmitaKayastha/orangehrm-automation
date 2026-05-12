import pytest
import os
from config import BASE_URL, USERNAME, PASSWORD 
from Pages.Admin_Job_JobTitles_Page import JobTitlePage
from Assertions.Job_JobTitles_Assertions import JobTitleAssertions

def test_add_job_title_successfully(page):
    page.goto(BASE_URL)
    page.fill("input[name='username']", USERNAME)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

   
    job_page = JobTitlePage(page)
    verify = JobTitleAssertions(page)


    job_page.navigate_to_job_titles()
    verify.verify_navigation_success()

    job_page.click_add()

   
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "test_upload.txt"
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "w") as f:
        f.write("Automated test job specification content.")

    unique_title = "Senior Automation Engineer " + os.urandom(2).hex()
    job_page.enter_job_details(
        title=unique_title,
        description="Responsible for end-to-end framework development.",
        note="Created via Playwright test suite"
    )

    job_page.upload_job_specification(file_path)
    
    job_page.save_form()

    verify.verify_success_message()
    
    if os.path.exists(file_path):
        os.remove(file_path)