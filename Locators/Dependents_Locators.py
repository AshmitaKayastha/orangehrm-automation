class Dependents_Locators:
  
    #---- Dependents Tab ---
    DEPENDENTS_TAB= "a:has-text('Dependents')"

    #--- Assigned Dependents ---
    DEPENDENTS_HEADER = "h6:has-text('Assigned Dependents')"
    ADD_DEPENDENT_BUTTON = "(//button[@type='button'][normalize-space()='Add'])[1]"

    #--- Attachments ---
    ATTACHMENTS_HEADER = "h6:has-text('Attachments')"
    ADD_ATTACHMENT_BUTTON = "div[class='orangehrm-attachment'] button[type='button']"
