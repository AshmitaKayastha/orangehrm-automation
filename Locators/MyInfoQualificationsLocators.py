class QualificationsLocators:
    QUALIFICATIONS_TAB = "text=Qualifications"
    ADD_WORK_EXP_BTN = "xpath=(//button[contains(.,'Add')])[1]" 
    COMPANY_INPUT = "xpath=//label[text()='Company']/../../div[2]/input"
    JOB_TITLE_INPUT = "xpath=//label[text()='Job Title']/../../div[2]/input"
    FROM_DATE_INPUT = "xpath=//label[text()='From']/../../div[2]//input"
    TO_DATE_INPUT = "xpath=//label[text()='To']/../../div[2]//input"
    COMMENT_TEXTAREA = "xpath=//label[text()='Comment']/../../div[2]/textarea"
    SAVE_BTN = "button[type='submit']"
    
    EDIT_ICON = ".bi-pencil-fill"
    DELETE_ICON = ".bi-trash"
    RECORD_ROW = ".oxd-table-card"
    
    REQUIRED_ERROR = ".oxd-input-group__message"
    TOAST_MESSAGE = ".oxd-toast"
    CONFIRM_DELETE_BTN = "button:has-text('Yes, Delete')"