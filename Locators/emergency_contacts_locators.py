from playwright.sync_api import Page


class EmergencyContactLocators:
    """
    Contains all locators for OrangeHRM Emergency Contacts Page
    """
    # -------------------------------------------------
    # Login Page Locators
    # -------------------------------------------------
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    # -------------------------------------------------
    # Navigation Locators
    # -------------------------------------------------
    MY_INFO = "//span[text()='My Info']"
    EMERGENCY_CONTACT_TAB = "//a[text()='Emergency Contacts']"
    # -------------------------------------------------
    # Emergency Contact Form Locators
    # -------------------------------------------------
    ADD_BUTTON= "//h6[text()='Assigned Emergency Contacts']/following::button[normalize-space()='Add'][1]"
    NAME_INPUT = "//label[text()='Name']/following::input[1]"
    RELATIONSHIP_INPUT = ("//label[text()='Relationship']/following::input[1]")
    HOME_CONTACT = ("//label[text()='Home Telephone']/following::input[1]")
    EDIT_HOME_CONTACT = ("//label[text()='Home Telephone']""/ancestor::div[contains(@class,'oxd-input-group')]//input")
    MOBILE = "//label[text()='Mobile']/following::input[1]"
    WORK_TELEPHONE = ("//label[text()='Work Telephone']/following::input[1]")
    SAVE_BUTTON = "//button[normalize-space()='Save']"
    CANCEL_BUTTON = "//button[normalize-space()='Cancel']"
    # -------------------------------------------------
    # Attachment Section Locators
    # -------------------------------------------------
    ATTACHMENT_ADD_BUTTON = ("(//button[normalize-space()='Add'])[2]")
    BROWSE_BUTTON = ("//div[contains(@class,'oxd-file-button') ""and text()='Browse']")
    ATTACHMENT_SAVE_BUTTON = ("//button[@type='submit' and normalize-space()='Save']")
    DOWNLOAD_BUTTON = ("//button[i[contains(@class,'bi-download')]]")
    # -------------------------------------------------
    # Delete Locators
    # -------------------------------------------------
    DELETE_CONFIRM_BUTTON = ("//button[normalize-space()='Yes, Delete']")
    EMERGENCY_CONTACT_TAB = ("//a[text()='Emergency Contacts']")
    # -------------------------------------------------
    # Table Column Locators
    # -------------------------------------------------
    NAME_COLUMN = ("//div[@role='columnheader' ""and normalize-space()='Name']")
    RELATIONSHIP_COLUMN = ("//div[@role='columnheader' ""and normalize-space()='Relationship']")
    HOME_TELEPHONE_COLUMN = ("//div[@role='columnheader' ""and normalize-space()='Home Telephone']")
    MOBILE_COLUMN = ("//div[@role='columnheader' ""and normalize-space()='Mobile']")
    WORK_TELEPHONE_COLUMN = ("//div[@role='columnheader' ""and normalize-space()='Work Telephone']")
class OrangeHRMEmergencyContactPage:
    """
    Page Object Model for OrangeHRM Emergency Contacts
    """
    def __init__(page_object, page: Page):
        page_object.page = page
        page_object.locators = EmergencyContactLocators()
        page_object.timeout = 10000

    # -------------------------------------------------
    # Open Application
    # -------------------------------------------------
    def open_application(page_object):
        page_object.page.goto("https://opensource-demo.orangehrmlive.com/""web/index.php/auth/login")

    # -------------------------------------------------
    # Login Methods
    # -------------------------------------------------
    def fill_username(page_object, username):
        username_input = page_object.page.locator(page_object.locators.USERNAME_INPUT)
        username_input.wait_for(state="visible",timeout=page_object.timeout)
        username_input.fill(username)

    def fill_password(page_object, password):
        password_input = page_object.page.locator(page_object.locators.PASSWORD_INPUT)
        password_input.wait_for(state="visible",timeout=page_object.timeout)
        password_input.fill(password)

    def click_login(page_object):
        login_button = page_object.page.locator(page_object.locators.LOGIN_BUTTON)
        login_button.wait_for(state="visible",timeout=page_object.timeout)
        login_button.click()

    def login(page_object, username, password):
        page_object.fill_username(username)
        page_object.fill_password(password)
        page_object.click_login()

    # -------------------------------------------------
    # Dashboard Verification
    # -------------------------------------------------
    def verify_dashboard(page_object):
        page_object.page.wait_for_url("**/dashboard",timeout=page_object.timeout)
    # -------------------------------------------------
    # Navigation Methods
    # -------------------------------------------------
    def click_my_info(page_object):
        my_info = page_object.page.locator(f"xpath={page_object.locators.MY_INFO}")
        my_info.wait_for(state="visible",timeout=page_object.timeout)
        my_info.click()

    def click_emergency_contact_tab(page_object):
        emergency_tab = page_object.page.locator(f"xpath={page_object.locators.EMERGENCY_CONTACT_TAB}")
        emergency_tab.wait_for(state="visible",timeout=page_object.timeout)
        emergency_tab.click()
    # -------------------------------------------------
    # Add Button Methods
    # -------------------------------------------------
    def is_add_button_visible(page_object):
        try:
            add_button = page_object.page.locator(f"xpath={page_object.locators.ADD_BUTTON}")
            add_button.wait_for(state="visible",timeout=page_object.timeout)
            return add_button.is_visible()
        except Exception:
            return False

    def click_add_button(page_object):
        add_button = page_object.page.locator(f"xpath={page_object.locators.ADD_BUTTON}")
        add_button.wait_for(state="visible",timeout=page_object.timeout)
        add_button.click()

    # -------------------------------------------------
    # Fill Emergency Contact Form
    # -------------------------------------------------
    def fill_name(page_object, name):
        name_input = page_object.page.locator(f"xpath={page_object.locators.NAME_INPUT}")
        name_input.wait_for(state="visible",timeout=page_object.timeout)
        name_input.fill(name)

    def fill_relationship(page_object, relationship):
        relationship_input = page_object.page.locator(f"xpath={page_object.locators.RELATIONSHIP_INPUT}")
        relationship_input.wait_for(state="visible",timeout=page_object.timeout)
        relationship_input.fill(relationship)

    def fill_home_contact(page_object, phone):
        home_contact = page_object.page.locator(f"xpath={page_object.locators.HOME_CONTACT}")
        home_contact.wait_for(state="visible",timeout=page_object.timeout)
        home_contact.fill(phone)

    def fill_mobile(page_object, mobile):
        mobile_input = page_object.page.locator(f"xpath={page_object.locators.MOBILE}")
        mobile_input.wait_for(state="visible",timeout=page_object.timeout)
        mobile_input.fill(mobile)

    def fill_work_telephone(page_object, work_phone):
        work_phone_input = page_object.page.locator(f"xpath={page_object.locators.WORK_TELEPHONE}")
        work_phone_input.wait_for(state="visible",timeout=page_object.timeout)
        work_phone_input.fill(work_phone)

    # -------------------------------------------------
    # Save / Cancel Methods
    # -------------------------------------------------
    def click_save(page_object):
        save_button = page_object.page.locator(f"xpath={page_object.locators.SAVE_BUTTON}")
        save_button.wait_for(state="visible",timeout=page_object.timeout)
        save_button.click()

    def click_cancel(page_object):
        cancel_button = page_object.page.locator(f"xpath={page_object.locators.CANCEL_BUTTON}")
        cancel_button.wait_for(state="visible",timeout=page_object.timeout)
        cancel_button.click()

    # -------------------------------------------------
    # Add Emergency Contact
    # -------------------------------------------------
    def add_emergency_contact(page_object,name,relationship,phone):
        page_object.click_add_button()
        page_object.fill_name(name)
        page_object.fill_relationship(relationship)
        page_object.fill_home_contact(phone)
        page_object.click_save()
        print("Emergency Contact Added Successfully")

    # -------------------------------------------------
    # Wait For Contact
    # -------------------------------------------------
    def wait_for_contact(page_object, name):
        contact = page_object.page.locator(f"xpath=//div[contains(text(),'{name}')]")
        contact.wait_for(state="visible",timeout=page_object.timeout)

    # -------------------------------------------------
    # Edit Contact
    # -------------------------------------------------
    def edit_home_contact(page_object, phone):
        home_contact = page_object.page.locator(f"xpath={page_object.locators.EDIT_HOME_CONTACT}")
        home_contact.wait_for(state="visible",timeout=page_object.timeout)
        home_contact.clear()
        home_contact.fill(phone)

    # -------------------------------------------------
    # Click Edit Button For Specific Contact
    # -------------------------------------------------
    def click_edit_for_contact(page_object, name):
        edit_xpath = (f"//div[@role='row']//div[contains(text(),'{name}')]"f"/following::button[2]")
        edit_button = page_object.page.locator(f"xpath={edit_xpath}")
        edit_button.wait_for(state="visible",timeout=page_object.timeout)
        edit_button.scroll_into_view_if_needed()
        edit_button.click()

    # -------------------------------------------------
    # Delete Methods
    # -------------------------------------------------
    def click_delete_for_contact(page_object, name):
        delete_xpath = (f"//div[@role='row']//div[contains(text(),'{name}')]"f"/following::button[1]")
        delete_button = page_object.page.locator(f"xpath={delete_xpath}")
        delete_button.wait_for(state="visible",timeout=page_object.timeout)
        delete_button.scroll_into_view_if_needed()
        delete_button.click()

    def confirm_delete(page_object):
        confirm_button = page_object.page.locator(f"xpath={page_object.locators.DELETE_CONFIRM_BUTTON}")
        confirm_button.wait_for(state="visible",timeout=page_object.timeout)
        confirm_button.click()
        print("Emergency Contact Deleted Successfully")

    # -------------------------------------------------
    # Attachment Methods
    # -------------------------------------------------
    def click_attachment_add(page_object):
        attachment_add = page_object.page.locator(f"xpath={page_object.locators.ATTACHMENT_ADD_BUTTON}")
        attachment_add.wait_for(state="visible",timeout=page_object.timeout)
        attachment_add.click()

    def upload_attachment(page_object, file_path):
        file_input = page_object.page.locator("input[type='file']")
        file_input.wait_for(state="attached",timeout=page_object.timeout)
        file_input.set_input_files(file_path)

    def click_attachment_save(page_object):
        save_button = page_object.page.locator(f"xpath={page_object.locators.ATTACHMENT_SAVE_BUTTON}")
        save_button.wait_for(state="visible",timeout=page_object.timeout)
        save_button.click()

    # -------------------------------------------------
    # Download Attachment
    # -------------------------------------------------
    def click_download(page_object):
        download_button = page_object.page.locator(f"xpath={page_object.locators.DOWNLOAD_BUTTON}")
        download_button.wait_for(state="visible",timeout=page_object.timeout)
        download_button.click()