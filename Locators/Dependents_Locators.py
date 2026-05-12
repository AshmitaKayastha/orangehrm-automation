class Dependents_Locators:
  
    #---- Dependents Tab ---
    DEPENDENTS_TAB= "a:has-text('Dependents')"

    #--- Assigned Dependents ---
    DEPENDENTS_HEADER = "h6:has-text('Assigned Dependents')"
    ADD_DEPENDENT_BUTTON = "(//button[@type='button'][normalize-space()='Add'])[1]"

    #---Dependents Info Form ---
    NAME_INPUT = "(//input[@class='oxd-input oxd-input--active'])[2]" # Not using as there are multiple inputs with same class, using nth-child in page object instead
    RELATIONSHIP_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    OTHER_RELATIONSHIP_INPUT = "div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] div:nth-child(3) div:nth-child(1) div:nth-child(2) input:nth-child(1)"
    DATE_OF_BIRTH_INPUT = "input[placeholder='yyyy-dd-mm']" #"input[placeholder='yyyy-mm-dd']"
    SAVE_BUTTON = "(//button[normalize-space()='Save'])[1]"
    CANCEL_BUTTON = "(//button[normalize-space()='Cancel'])[1]"
    REQUIRED_MESSAGE = "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[1]"
    TOAST_MESSAGE = ".oxd-toast" #"#oxd-toaster_1" #"(//div[@id='oxd-toaster_1'])[1]" 
    #TABLE_ROWS = "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[3]"
    #EDIT_ROW_1="div .oxd-table-card"
    EDIT_BUTTON_1 = "div.oxd-table .bi-pencil-fill" #".bi-pencil-fill" #"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)"
    DELETE_BUTTON_1 = ".bi-trash"
    DELETE_CONFIRM_BUTTON = ".oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin" # Same for both Dependent and Attachment delete confirmation
  
    #--- Attachments ---
    ATTACHMENTS_HEADER = "h6:has-text('Attachments')"
    ADD_ATTACHMENT_BUTTON = "div[class='orangehrm-attachment'] div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] button[type='button']" #"div[class='orangehrm-attachment'] button[type='button']" 
    BROWSE_FILE_BUTTON = "input[type='file']" #"input[type='file']"
    REQUIRED_FILE_MESSAGE = ".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message" #"span:has-text('Required')"
    COMMENT_TEXTAREA = "textarea[placeholder='Type comment here']"
    SAVE_ATTACHMENT_BUTTON = "button[type='submit']" #"button:has-text('Save')"
    CANCEL_ATTACHMENT_BUTTON = ".oxd-button.oxd-button--medium.oxd-button--ghost" #"button[type='button'][normalize-space()='Cancel']"
    EDIT_ATTACHMENT_BUTTON_1 = "div.orangehrm-attachment .bi-pencil-fill" 
    DELETE_ATTACHMENT_BUTTON_1 = "div.orangehrm-attachment .bi-trash" 
    DOWNLOAD_ATTACHMENT_BUTTON_1 = "div.orangehrm-attachment .bi-download" 
