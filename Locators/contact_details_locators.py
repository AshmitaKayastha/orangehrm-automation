# Locators for OrangeHRM - Contact Details Page
# URL: /web/index.php/pim/contactDetails/empNumber/{id}

class ContactDetailsLocators:

    # ── Page Header ───────────────────────────────────────────────────────────
    PAGE_HEADER = "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]"

    # ── Section Headers ───────────────────────────────────────────────────────
    SECTION_CONTACT_DETAILS = "//h6[normalize-space()='Contact Details']"
    SECTION_EMERGENCY_CONTACTS = "//h6[normalize-space()='Emergency Contacts']"

    # ── Contact Details Fields (Label-based, stable) ──────────────────────────
    INPUT_STREET1 = "//label[text()='Street 1']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_STREET2 = "//label[text()='Street 2']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_CITY = "//label[text()='City']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_STATE = "//label[contains(text(),'State')]/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_ZIP = "//label[contains(text(),'Zip')]/ancestor::div[contains(@class,'oxd-input-group')]//input"

    # ── Country Dropdown (STRICT MODE FIXED) ──────────────────────────────────
    DROPDOWN_COUNTRY = "//label[text()='Country']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text') and not(contains(@class,'--after'))]"
    DROPDOWN_COUNTRY_OPTIONS = "//div[@role='listbox']//span"

    # ── Phone Fields ──────────────────────────────────────────────────────────
    INPUT_HOME_TELEPHONE = "//label[text()='Home']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_WORK_TELEPHONE = "//label[text()='Work']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_MOBILE = "//label[text()='Mobile']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    # ── Email Fields ──────────────────────────────────────────────────────────
    INPUT_WORK_EMAIL = "//label[text()='Work Email']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_OTHER_EMAIL = "//label[text()='Other Email']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    # ── Save Button ───────────────────────────────────────────────────────────
    BTN_CONTACT_DETAILS_SAVE = "//button[normalize-space()='Save']"

    # ── Toast Messages ────────────────────────────────────────────────────────
    TOAST_SUCCESS = "//div[contains(@class,'oxd-toast--success')]//p[contains(@class,'oxd-text--toast-message')]"
    TOAST_ERROR = "//div[contains(@class,'oxd-toast--error')]//p[contains(@class,'oxd-text--toast-message')]"

    # ── Validation Message ────────────────────────────────────────────────────
    VALIDATION_MESSAGE = "//span[contains(@class,'oxd-input-field-error-message')]"

    # ── Emergency Contacts Section ────────────────────────────────────────────
    BTN_ADD_EMERGENCY_CONTACT = "//button[normalize-space()='Add']"

    # ── Emergency Contact Modal Fields (Label-based) ──────────────────────────
    INPUT_EC_NAME = "//label[text()='Name']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_EC_RELATIONSHIP = "//label[text()='Relationship']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_EC_HOME_PHONE = "//label[text()='Home Telephone']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_EC_MOBILE = "//label[text()='Mobile']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    INPUT_EC_WORK_PHONE = "//label[text()='Work Telephone']/ancestor::div[contains(@class,'oxd-input-group')]//input"

    # ── Dialog Buttons ────────────────────────────────────────────────────────
    BTN_EC_SAVE = "//button[normalize-space()='Save']"
    BTN_EC_CANCEL = "//button[normalize-space()='Cancel']"

    # ── Emergency Contact Table ───────────────────────────────────────────────
    EC_TABLE_ROWS = "//div[contains(@class,'orangehrm-container')]//div[@role='row'][not(contains(@class,'header'))]"
    EC_TABLE_FIRST_ROW_NAME = "(//div[contains(@class,'orangehrm-container')]//div[@role='row'][not(contains(@class,'header'))]//div[@role='cell'])[1]"

    # ── Row Actions (Edit/Delete) ─────────────────────────────────────────────
    BTN_EC_ROW_EDIT = ".//button[contains(@class,'oxd-icon-button') and .//*[contains(@*,'pencil')]]"
    BTN_EC_ROW_DELETE = ".//button[contains(@class,'oxd-icon-button') and .//*[contains(@*,'trash')]]"

    # ── Delete Confirmation Dialog ────────────────────────────────────────────
    BTN_CONFIRM_DELETE = "//button[normalize-space()='Yes, Delete']"