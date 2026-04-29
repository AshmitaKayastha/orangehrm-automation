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
        self.page.wait_for_timeout(2000) 

    def edit_first_record(self, new_company):
        self.page.locator(QualificationsLocators.EDIT_ICON).first.click()
        self.page.locator(QualificationsLocators.COMPANY_INPUT).click(click_count=3)
        self.page.keyboard.press("Backspace")
        self.page.fill(QualificationsLocators.COMPANY_INPUT, new_company)
        self.page.click(QualificationsLocators.SAVE_BTN)
        self.page.wait_for_timeout(2000) 
    def delete_first_record(self):
        self.page.locator(QualificationsLocators.DELETE_ICON).first.click()
        self.page.click(QualificationsLocators.CONFIRM_DELETE_BTN)
        self.page.wait_for_timeout(2000)

    #Education
    def add_education(self, level, institute, major, year, gpa, start_date, end_date):
        self.page.locator(QualificationsLocators.ADD_EDUCATION_BTN).first.click()
        self.page.wait_for_timeout(1000)
        
        # (Your existing fill logic which is working)
        self.page.locator(QualificationsLocators.LEVEL_DROPDOWN).first.click()
        self.page.get_by_role("option", name=level).click()
        
        self.page.locator(QualificationsLocators.INSTITUTE_INPUT).fill(institute)
        self.page.locator(QualificationsLocators.MAJOR_INPUT).fill(major)
        self.page.locator(QualificationsLocators.YEAR_INPUT).fill(year)
        self.page.locator(QualificationsLocators.GPA_INPUT).fill(gpa)
        self.page.locator(QualificationsLocators.START_DATE_INPUT).fill(start_date)
        self.page.locator(QualificationsLocators.END_DATE_INPUT).fill(end_date)
        
        self.page.locator(QualificationsLocators.SAVE_BTN).first.click()
        try:
            self.page.wait_for_selector("//h6[text()='Add Education']", state="hidden", timeout=5000)
        except:
            # If it didn't hide, maybe the toast is still there? 
            # We check the toast as a backup.
            self.page.locator(QualificationsLocators.SUCCESS_TOAST).wait_for(state="visible", timeout=3000)

    def edit_education_institute(self, new_institute):
        edit_btn = self.page.locator(QualificationsLocators.EDU_EDIT_ICON).first
        edit_btn.scroll_into_view_if_needed()
        edit_btn.click(force=True)
        
        inst_field = self.page.locator(QualificationsLocators.INSTITUTE_INPUT)
        inst_field.wait_for(state="visible", timeout=10000)
        inst_field.fill(new_institute)
    
        self.page.locator(QualificationsLocators.SAVE_BTN).first.click()

    def delete_education_record(self):
        self.page.locator(QualificationsLocators.EDU_DELETE_ICON).first.click()
        confirm_btn = self.page.locator(QualificationsLocators.CONFIRM_DELETE_BTN)
        confirm_btn.click()
        confirm_btn.wait_for(state="hidden")

    def add_skill(self, skill_name, years, comments):
        self.page.locator("//h6[text()='Skills']/following-sibling::button").click()
        self.page.locator(".oxd-select-text").first.click()
        options = self.page.get_by_role("listbox")
        options.get_by_text(skill_name, exact=True).click()
        self.page.get_by_role("textbox").nth(1).fill(years)
        self.page.locator("textarea").fill(comments)
        self.page.get_by_role("button", name="Save").click()

    def edit_skill_experience(self, years):
        edit_button = self.page.locator("//div[@role='row' and .//div[text()='Java']]//button[i[contains(@class, 'bi-pencil-fill')]]")
        edit_button.wait_for(state="visible")
        edit_button.click()
        years_input = self.page.locator("xpath=//label[text()='Years of Experience']/parent::div/following-sibling::div//input")
        
        years_input.wait_for(state="visible", timeout=5000)
        years_input.clear() # Clear the old value first
        years_input.fill(years)
        self.page.get_by_role("button", name="Save").click()

    def delete_skill_record(self, skill_name="Java"):
        trash_icon = self.page.locator(f"//div[@role='row' and .//div[text()='{skill_name}']]//button[i[contains(@class, 'bi-trash')]]")
        
        trash_icon.wait_for(state="visible")
        trash_icon.click()
        confirm_button = self.page.get_by_role("button", name="Yes, Delete")
        confirm_button.wait_for(state="visible")
        confirm_button.click()
        self.page.locator(".oxd-toast").wait_for(state="hidden", timeout=5000)