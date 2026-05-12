from playwright.sync_api import Page
from Locators.Admin_Job_JobTitles_Locators import JobTitlesLocators as loc

class JobTitlePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_job_titles(self):
        self.page.click(loc.ADMIN_SIDEBAR)
        self.page.click(loc.JOB_DROPDOWN)
        self.page.click(loc.JOB_TITLES_OPTION)

    def click_add(self):
        self.page.click(loc.ADD_BUTTON)

    def enter_job_details(self, title, description, note):
        self.page.fill(loc.JOB_TITLE_INPUT, title)
        self.page.fill(loc.JOB_DESCRIPTION_TEXTAREA, description)
        self.page.fill(loc.NOTE_TEXTAREA, note)

    # ADD THIS METHOD TO FIX THE ATTRIBUTE ERROR
    def upload_job_specification(self, file_path):
        # This targets the hidden file input associated with the 'Browse' button
        self.page.set_input_files(loc.JOB_SPECIFICATION_UPLOAD, file_path)

    def save_form(self):
        self.page.click(loc.SAVE_BUTTON)

