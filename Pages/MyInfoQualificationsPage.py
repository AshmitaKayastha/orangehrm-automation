from playwright.sync_api import Page
from Locators.MyInfoQualificationsLocators import QualificationsLocators

class QualificationsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_qualifications(self):
        self.page.click(QualificationsLocators.QUALIFICATIONS_TAB)

    def add_work_experience(self, company, job_title, from_date, to_date, comment):
        self.page.click(QualificationsLocators.ADD_WORK_EXP_BTN)
        self.page.fill(QualificationsLocators.COMPANY_INPUT, company)
        self.page.fill(QualificationsLocators.JOB_TITLE_INPUT, job_title)
        self.page.fill(QualificationsLocators.FROM_DATE_INPUT, from_date)
        self.page.fill(QualificationsLocators.TO_DATE_INPUT, to_date)
        self.page.fill(QualificationsLocators.COMMENT_TEXTAREA, comment)
        self.page.click(QualificationsLocators.SAVE_BTN)
        self.page.wait_for_timeout(2000) # Wait for DB update

    def edit_first_record(self, new_company):
        self.page.locator(QualificationsLocators.EDIT_ICON).first.click()
        # Clear the field before typing the new name
        self.page.locator(QualificationsLocators.COMPANY_INPUT).click(click_count=3)
        self.page.keyboard.press("Backspace")
        self.page.fill(QualificationsLocators.COMPANY_INPUT, new_company)
        self.page.click(QualificationsLocators.SAVE_BTN)
        self.page.wait_for_timeout(2000) # Wait for DB update

    def delete_first_record(self):
        self.page.locator(QualificationsLocators.DELETE_ICON).first.click()
        self.page.click(QualificationsLocators.CONFIRM_DELETE_BTN)
        self.page.wait_for_timeout(2000)