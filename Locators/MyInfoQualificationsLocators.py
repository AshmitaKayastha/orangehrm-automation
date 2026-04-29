class QualificationsLocators:
    QUALIFICATIONS_TAB = "a:has-text('Qualifications')"
    # Work Experience
    ADD_WORK_EXP_BTN = "//h6[text()='Work Experience']/following::button[normalize-space()='Add'][1]"

    COMPANY_INPUT = "//label[text()='Company']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    JOB_TITLE_INPUT = "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    FROM_DATE_INPUT = "(//input[@placeholder='yyyy-mm-dd'])[1]"
    TO_DATE_INPUT = "(//input[@placeholder='yyyy-mm-dd'])[2]"

    COMMENT_TEXTAREA = "//textarea"

    SAVE_BTN = "button:has-text('Save')"
    RECORD_ROW = ".oxd-table-card"

    EDIT_ICON = "button:has(i.bi-pencil-fill)"
    DELETE_ICON = "button:has(i.bi-trash)"
    REQUIRED_ERROR = ".oxd-input-group__message"
    TOAST_MESSAGE = ".oxd-toast"
    SUCCESS_TOAST = ".oxd-toast--success"

    CONFIRM_DELETE_BTN = "button:has-text('Yes, Delete')"

   
    # Education
    EDUCATION_SECTION = "h6:has-text('Education')"
    ADD_EDUCATION_BTN = "//h6[text()='Education']/parent::div//button"

    INSTITUTE_INPUT = "//label[text()='Institute']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    MAJOR_INPUT = "//label[text()='Major/Specialization']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    YEAR_INPUT = "//label[text()='Year']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    GPA_INPUT = "//label[text()='GPA/Score']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    START_DATE_INPUT = "//label[text()='Start Date']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    END_DATE_INPUT = "//label[text()='End Date']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    LEVEL_DROPDOWN = "//label[text()='Level']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"

    ADD_EDUCATION_HEADER = "h6:has-text('Add Education')"

    EDU_EDIT_ICON = "//h6[text()='Education']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'pencil')]]"
    EDU_DELETE_ICON = "//h6[text()='Education']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'trash')]]"


    # Skills
    SKILLS_SECTION_ADD_BTN = "//h6[text()='Skills']/parent::div//button"

    SKILL_DROPDOWN = "//label[text()='Skill']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
    SKILL_OPTION = "//div[@role='listbox']//span[text()='{0}']"

    YEARS_EXP_INPUT = "//label[text()='Years of Experience']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    COMMENTS_TEXTAREA = "//label[text()='Comments']/ancestor::div[contains(@class,'oxd-input-group')]//textarea"

    SKILL_EDIT_ICON = "//h6[text()='Skills']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'pencil')]]"
    SKILL_DELETE_ICON = "//h6[text()='Skills']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'trash')]]"