class QualificationsLocators:
    QUALIFICATIONS_TAB = "a:has-text('Qualifications')"

    # Work Experience
    ADD_WORK_EXP_BTN = "//h6[text()='Work Experience']/following::button[normalize-space()='Add'][1]"
    COMPANY_INPUT = "//label[text()='Company']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    JOB_TITLE_INPUT = "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    FROM_DATE_INPUT = "//label[text()='From']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    TO_DATE_INPUT = "//label[text()='To']/ancestor::div[contains(@class,'oxd-input-group')]//input"
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
    EDU_EDIT_ICON = "//h6[text()='Education']/parent::div/following-sibling::div//button[i[contains(@class,'pencil')]]"
    EDU_DELETE_ICON = "//h6[text()='Education']/parent::div/following-sibling::div//button[i[contains(@class,'trash')]]"
    INSTITUTE_INPUT = "//label[text()='Institute']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    SAVE_BTN = "button[type='submit']"


    # Skills
    SKILLS_SECTION_ADD_BTN = "//h6[text()='Skills']/parent::div//button"
    SKILL_DROPDOWN = "//label[text()='Skill']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
    SKILL_OPTION = "//div[@role='listbox']//span[text()='{0}']"
    YEARS_EXP_INPUT = "//label[text()='Years of Experience']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    COMMENTS_TEXTAREA = "//label[text()='Comments']/ancestor::div[contains(@class,'oxd-input-group')]//textarea"
    SKILL_EDIT_ICON = "//h6[text()='Skills']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'pencil')]]"
    SKILL_DELETE_ICON = "//h6[text()='Skills']/ancestor::div[contains(@class,'orangehrm-edit-employee-content')]//button[i[contains(@class,'trash')]]"


    
    # Languages Section
    ADD_LANGUAGE_BTN = "//h6[text()='Languages']/following-sibling::button"
    SAVE_BTN = "//button[@type='submit']"
    SUCCESS_TOAST = "//div[contains(@class, 'oxd-toast--success')]"
    LANG_DROPDOWN = "//label[text()='Language']/parent::div/following-sibling::div"
    FLUENCY_DROPDOWN = "//label[text()='Fluency']/parent::div/following-sibling::div"
    COMPETENCY_DROPDOWN = "//label[text()='Competency']/parent::div/following-sibling::div"
    LANG_COMMENTS = "//label[text()='Comments']/parent::div/following-sibling::div//textarea"
    LISTBOX = "//div[@role='listbox']"
    TABLE_CARD = ".oxd-table-card" 
    EDIT_ICON = ".bi-pencil-fill"
    SAVE_BTN = "button[type='submit']"
    CONFIRM_DELETE_BTN = "button:has-text('Yes, Delete')"


    # License
    ADD_LICENSE_BTN = "//h6[text()='License']/following-sibling::button"
    SAVE_BTN = "button[type='submit']"
    SUCCESS_TOAST = "//div[contains(@class, 'oxd-toast--success')]"
    LICENSE_TYPE_DROPDOWN = "//label[text()='License Type']/parent::div/following-sibling::div"
    LICENSE_NUMBER_INPUT = "//label[text()='License Number']/parent::div/following-sibling::div//input"
    LICENSE_ISSUED_DATE = "//label[text()='Issued Date']/parent::div/following-sibling::div//input"
    LICENSE_EXPIRY_DATE = "//label[text()='Expiry Date']/parent::div/following-sibling::div//input"
    LICENSE_SECTION_TABLE = "//h6[text()='License']/ancestor::div[@class='orangehrm-horizontal-padding']//div[@role='table']"
    LICENSE_RECORD_ROW = "//h6[text()='License']/ancestor::div[@class='orangehrm-horizontal-padding']//div[@class='oxd-table-card']"
    EDIT_ICON = ".bi-pencil-fill"
    DELETE_ICON = ".bi-trash"
    LICENSE_CHECKBOX = ".oxd-checkbox-input"
    DELETE_SELECTED_BTN = "//button[text()=' Delete Selected ']"
    CONFIRM_DELETE_BTN = "//button[text()=' Yes, Delete ']"

    #Attachment
    ATTACH_ADD_BTN = "//h6[text()='Attachments']/following-sibling::button[text()=' Add ']"
    ATTACH_FILE_INPUT = "//input[@type='file']"
    ATTACH_COMMENT_TEXTAREA = "//textarea"
    ATTACH_SAVE_BTN = "//div[@class='orangehrm-attachment']//button[@type='submit']"
    ATTACH_RECORDS_TABLE = "div.orangehrm-attachment .orangehrm-container"