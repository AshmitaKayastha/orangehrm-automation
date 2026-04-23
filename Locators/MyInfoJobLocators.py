class MyInfoJobLocators:
# MI-081
    MY_INFO = "text=My Info"
    JOB_TAB = "a.orangehrm-tabs-item:has-text('Job')"
    JOB_HEADER = "text=Job Title"

# MI-082
    JOINED_DATE = "text=Joined Date"
    JOB_TITLE = "text=Job Title"
    JOB_CATEGORY = "text=Job Category"
    SUB_UNIT = "text=Sub Unit"
    LOCATION = "text=Location"
    EMPLOYMENT_STATUS = "text=Employment Status"   

      # MI-082/ Contract section
    # CONTRACT_TOGGLE = "//label[contains(text(),'Include Employment Contract Details')]/following::span[contains(@class,'oxd-switch-input')][1]"
    CONTRACT_TOGGLE = "label:has-text('Include Employment Contract Details') >> xpath=following::span[1]"
    # CONTRACT_START = "text=Contract Start Date"
    # CONTRACT_END = "text=Contract End Date"
    CONTRACT_START_INPUT = ".oxd-form-row:has(label:has-text('Contract Start Date')) input"
    CONTRACT_END_INPUT   = ".oxd-form-row:has(label:has-text('Contract End Date')) input"