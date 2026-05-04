from playwright.sync_api import Page
from Locators.MyInfoQualificationsLocators import QualificationsLocators

class QualificationsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_qualifications(self):
        self.page.click(QualificationsLocators.QUALIFICATIONS_TAB)

    # Work Experience

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
        company_input = self.page.locator(QualificationsLocators.COMPANY_INPUT)
        self.page.locator(QualificationsLocators.EDIT_ICON).first.click()
        company_input.fill(new_company)
        self.page.locator(QualificationsLocators.SAVE_BTN).click()

    def delete_first_record(self):
        self.page.locator(QualificationsLocators.DELETE_ICON).first.click()
        self.page.click(QualificationsLocators.CONFIRM_DELETE_BTN)
        self.page.wait_for_timeout(2000)

    #Education
    def add_education(self, level, institute, major, year, gpa, start_date, end_date):
        self.page.locator(QualificationsLocators.ADD_EDUCATION_BTN).first.click()
        self.page.wait_for_timeout(1000)
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
            self.page.locator(QualificationsLocators.SUCCESS_TOAST).wait_for(state="visible", timeout=3000)

    def edit_education_institute(self, education_level, new_institute_name):
        row = self.page.locator(".oxd-table-card").filter(has_text=education_level).first
        row.locator(".bi-pencil-fill").click()
        self.page.get_by_role("heading", name="Edit Education").wait_for()
        institute_input = self.page.locator("div.oxd-input-group:has(label:text('Institute')) input")
        institute_input.wait_for(state="visible")
        institute_input.click(click_count=3)
        self.page.keyboard.press("Backspace")
        institute_input.fill(new_institute_name)
        self.page.locator("button[type='submit']").first.click()

    def delete_education_record(self, education_level):
        row = self.page.locator(".oxd-table-card").filter(has_text=education_level).first
        row.locator(".bi-trash").click()
        self.page.locator("button:has-text('Yes, Delete')").click()
        self.page.wait_for_timeout(2000)

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
        years_input.clear() 
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

    def add_language(self, language, fluency, competency, comments):
        self.page.locator(QualificationsLocators.ADD_LANGUAGE_BTN).click()
        self.page.locator(QualificationsLocators.LANG_DROPDOWN).click()
        self.page.get_by_role("option").first.wait_for(state="visible")
        self.page.get_by_role("option", name=language, exact=False).click()
        self.page.locator(QualificationsLocators.FLUENCY_DROPDOWN).click()
        self.page.wait_for_timeout(500) 
        self.page.get_by_role("option", name=fluency, exact=False).click()
        self.page.locator(QualificationsLocators.COMPETENCY_DROPDOWN).click()
        self.page.wait_for_timeout(500)
        self.page.get_by_role("option", name=competency, exact=False).click()
        self.page.locator(QualificationsLocators.LANG_COMMENTS).fill(comments)
        self.page.locator(QualificationsLocators.SAVE_BTN).click()
  
    def edit_language(self, language_name, new_competency):
        edit_icon = self.page.locator(f"//div[text()='{language_name}']/following::button[i[contains(@class, 'bi-pencil-fill')]][1]")
        edit_icon.click()
        self.page.locator(QualificationsLocators.COMPETENCY_DROPDOWN).click()
        self.page.locator(QualificationsLocators.LISTBOX).wait_for(state="visible")
        self.page.get_by_role("option", name=new_competency, exact=False).click()
        self.page.locator(QualificationsLocators.SAVE_BTN).click()

    def delete_language(self, language_name):
        row = self.page.locator(QualificationsLocators.TABLE_CARD).filter(has_text=language_name)
        row.locator(QualificationsLocators.DELETE_ICON).click()
        self.page.locator(QualificationsLocators.CONFIRM_DELETE_BTN).click()

    def add_first_available_license(self):
        self.page.locator("button:has-text('Add')").nth(4).click()
        dropdown = self.page.locator(".oxd-select-wrapper").first
        dropdown.click()
        first_option = self.page.locator(".oxd-select-option").nth(1)
        license_name = first_option.inner_text()
        first_option.click()
        self.page.get_by_role("button", name="Save").first.click()
        return license_name

    def edit_first_license_record(self, new_number):
        license_section = self.page.locator("div.orangehrm-background-container").filter(has=self.page.get_by_role("heading", name="License"))
        first_row = license_section.locator(".oxd-table-card").first
        first_row.locator(".bi-pencil-fill").click()
        self.page.locator("div.oxd-input-group:has(label:text('License Number')) input").fill(new_number)
        self.page.get_by_role("button", name="Save").first.click()

    def delete_first_license_record(self):
        license_section = self.page.locator("div.orangehrm-background-container").filter(has=self.page.get_by_role("heading", name="License"))
        first_row = license_section.locator(".oxd-table-card").first
        first_row.locator(".bi-trash").click()
        self.page.get_by_role("button", name="Yes, Delete").click()

    
    def add_attachment(self, file_path, comment_text):
        self.page.locator(QualificationsLocators.ATTACH_ADD_BTN).click()
        self.page.locator(QualificationsLocators.ATTACH_FILE_INPUT).set_input_files(file_path)
        self.page.locator(QualificationsLocators.ATTACH_COMMENT_TEXTAREA).fill(comment_text)
        self.page.locator(QualificationsLocators.ATTACH_SAVE_BTN).click()
        self.page.wait_for_timeout(2000)