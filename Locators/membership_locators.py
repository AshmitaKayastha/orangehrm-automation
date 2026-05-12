# Locators for Membership Page

class MembershipLocators:
    """
    Contains all locators for the OrangeHRM Membership page
    """

    # --- Navigation ---
    # Sidebar "Memberships" link (to navigate to the page)
    MEMBERSHIPS_MENU_ITEM = "//a[contains(@class,'orangehrm-tabs-item') and text()='Memberships']"

    # --- Assigned Memberships Section ---
    # The "+ Add" button in the Assigned Memberships section
    ADD_MEMBERSHIP_BUTTON = "(//button[normalize-space()='Add'])[1]"

    # Membership dropdown inside the Add form
    MEMBERSHIP_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"

    # Subscription Paid By dropdown
    SUBSCRIPTION_PAID_BY_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"

    # Subscription Amount input
    SUBSCRIPTION_AMOUNT_INPUT = "(//input[@class='oxd-input oxd-input--active'])[2]"

    # Currency dropdown
    CURRENCY_DROPDOWN = "(//div[@class='oxd-select-text oxd-select-text--active'])[3]"

    # Subscription Commence Date input
    SUBSCRIPTION_COMMENCE_DATE = "(//input[@placeholder='yyyy-dd-mm'])[1]"

    # Subscription Renewal Date input
    SUBSCRIPTION_RENEWAL_DATE = "(//input[@placeholder='yyyy-dd-mm'])[2]"

    # Save button inside the form
    SAVE_BUTTON = "//button[@type='submit']"

    # Cancel button inside the form
    CANCEL_BUTTON = "//button[normalize-space()='Cancel']"

    # Success toast notification
    SUCCESS_TOAST = ".oxd-toast--success"

    # No records found text
    NO_RECORDS_FOUND = "//span[normalize-space()='No Records Found']"

    # First row delete button in Assigned Memberships table
    DELETE_MEMBERSHIP_BUTTON = "(//div[@class='oxd-table-cell-actions']//button)[1]"

    # Confirm delete button in the popup
    CONFIRM_DELETE_BUTTON = "//button[normalize-space()='Yes, Delete']"

    # --- Attachments Section ---
    # The "+ Add" button in the Attachments section
    ADD_ATTACHMENT_BUTTON = "(//button[normalize-space()='Add'])[2]"

    # File input for attachment upload
    ATTACHMENT_FILE_INPUT = "//input[@type='file']"

    # Attachment description input
    ATTACHMENT_DESCRIPTION_INPUT = "(//input[@class='oxd-input oxd-input--active'])[1]"

    # Attachment record count text e.g. "(1) Record Found"
    ATTACHMENT_RECORD_COUNT = "//span[contains(text(),'Record Found')]"

    # First attachment row delete button
    DELETE_ATTACHMENT_BUTTON = "(//div[@class='oxd-table-cell-actions']//button)[2]"