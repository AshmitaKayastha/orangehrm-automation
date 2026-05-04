import os
from time import sleep
from playwright.sync_api import Page
from Locators.emergency_contacts_locators import (EmergencyContactLocators)

class EmergencyContactPage:

    def __init__(self, page: Page):
        self.page = page
        self.timeout = 10000

    def navigate_to_emergency_contacts(self):
        emergency_tab = self.page.locator(f"xpath={EmergencyContactLocators.EMERGENCY_CONTACT_TAB}")
        emergency_tab.wait_for(state="visible",timeout=self.timeout)
        emergency_tab.click()
    # -------------------------------------------------
    # Verify Add button is displayed
    # -------------------------------------------------
    def is_add_button_displayed(page_object):
        try:
            add_button = page_object.page.locator(f"xpath={EmergencyContactLocators.ADD_BUTTON}")
            add_button.wait_for(state="visible",timeout=page_object.timeout)
            return add_button.is_visible()
        except Exception:
            return False
    # -------------------------------------------------
    # Add new emergency contact
    # -------------------------------------------------
    def click_add_button(page_object):
        add_button = page_object.page.locator(f"xpath={EmergencyContactLocators.ADD_BUTTON}")
        add_button.wait_for(state="visible",timeout=page_object.timeout)
        add_button.scroll_into_view_if_needed()
        add_button.click(force=True)
    print("Add button clicked successfully")

    # -------------------------------------------------
    # Enter Contact Details
    # -------------------------------------------------
    def enter_name(page_object, name):
        name_input = page_object.page.locator(f"xpath={EmergencyContactLocators.NAME_INPUT}")
        name_input.wait_for(state="visible",timeout=page_object.timeout)
        name_input.fill(name)
    def enter_relationship(page_object, relationship):
        relationship_input = page_object.page.locator(f"xpath={EmergencyContactLocators.RELATIONSHIP_INPUT}")
        relationship_input.wait_for(state="visible",timeout=page_object.timeout)
        relationship_input.fill(relationship)
    def enter_phone(page_object, phone):
        phone_input = page_object.page.locator(f"xpath={EmergencyContactLocators.HOME_CONTACT}")
        phone_input.wait_for(state="visible",timeout=page_object.timeout)
        phone_input.fill(phone)

    # -------------------------------------------------
    # Save / Cancel
    # -------------------------------------------------
    def click_save(page_object):
        save_button = page_object.page.locator(f"xpath={EmergencyContactLocators.SAVE_BUTTON}")
        save_button.wait_for(state="visible",timeout=page_object.timeout)
        save_button.click()
        page_object.page.wait_for_timeout(3000)
    print("Record saved successfully")

    def click_cancel(page_object):
        cancel_button = page_object.page.locator(f"xpath={EmergencyContactLocators.CANCEL_BUTTON}")
        cancel_button.wait_for(state="visible",timeout=page_object.timeout)
        cancel_button.click()

    def add_contact_required_fields(page_object, name, relationship, phone):
        page_object.click_add_button()
        print("Clicked Add button")
        page_object.enter_name(name)
        page_object.enter_relationship(relationship)
        page_object.enter_phone(phone)
        page_object.click_save()
        print("Emergency contact added successfully")
    
    def add_contact_required_fields_for_cancel(page_object, name, relationship, phone):
        page_object.click_add_button()
        print("Clicked Add button")
        page_object.enter_name(name)
        page_object.enter_relationship(relationship)
        page_object.enter_phone(phone)
        page_object.click_cancel()
        print("Emergency contact cancelled successfully")
    

    def wait_for_contact(page_object, name):
        contact = page_object.page.locator(f"xpath=//div[contains(text(),'{name}')]")
        contact.wait_for(state="visible", timeout=page_object.timeout)

    def click_edit_for_contact(page_object, name):
        edit_xpath = (f"//div[@role='row']//div[contains(text(),'{name}')]"f"/following::button[2]")
        edit_button = page_object.page.locator(f"xpath={edit_xpath}")
        edit_button.wait_for(state="visible",timeout=page_object.timeout)
        edit_button.scroll_into_view_if_needed()
        edit_button.click()
        home_contact = page_object.page.locator(f"xpath={EmergencyContactLocators.EDIT_HOME_CONTACT}")
        home_contact.wait_for(state="visible",timeout=page_object.timeout)
        home_contact.clear()
        sleep(1)
        home_contact.fill("1234567890")
        page_object.click_save()
        print("Contact edited successfully")

    def click_delete_for_contact(page_object, name):
        delete_xpath = (f"//div[@role='row']//div[contains(text(),'{name}')]"f"/following::button[1]")
        delete_button = page_object.page.locator(f"xpath={delete_xpath}")
        delete_button.wait_for(state="visible",timeout=page_object.timeout)
        delete_button.scroll_into_view_if_needed()
        delete_button.click()

    def confirm_delete(page_object):
        confirm_button = page_object.page.locator("xpath=//button[normalize-space()='Yes, Delete']")
        confirm_button.wait_for(state="visible",timeout=page_object.timeout)
        confirm_button.click()
        print("Contact deleted successfully")

    def verify_name_column(self):
        name_column = self.page.locator(f"xpath={EmergencyContactLocators.NAME_COLUMN}")
        name_column.wait_for(state="visible",timeout=self.timeout)
        return name_column.is_visible()

    def verify_relationship_column(self):
        relationship_column = self.page.locator(f"xpath={EmergencyContactLocators.RELATIONSHIP_COLUMN}")
        relationship_column.wait_for(state="visible",timeout=self.timeout)
        return relationship_column.is_visible()

    def verify_home_telephone_column(self):
        home_column = self.page.locator(f"xpath={EmergencyContactLocators.HOME_TELEPHONE_COLUMN}")
        home_column.wait_for(state="visible",timeout=self.timeout)
        return home_column.is_visible()

    def verify_mobile_column(self):
        mobile_column = self.page.locator(f"xpath={EmergencyContactLocators.MOBILE_COLUMN}")
        mobile_column.wait_for(state="visible",timeout=self.timeout)
        return mobile_column.is_visible()

    def verify_work_telephone_column(self):
        work_column = self.page.locator(f"xpath={EmergencyContactLocators.WORK_TELEPHONE_COLUMN}")
        work_column.wait_for(state="visible",timeout=self.timeout)
        return work_column.is_visible()

    def click_attachment_add_button(page_object):
        attachment_add = page_object.page.locator("xpath=(//button[normalize-space()='Add'])[2]")
        attachment_add.wait_for(state="visible",timeout=page_object.timeout)
        attachment_add.click()
        print("Attachment Add button clicked")

    def upload_attachment_file(page_object):
        browse_input = page_object.page.locator("xpath=//input[@type='file']")
        browse_input.wait_for(state="attached",timeout=page_object.timeout)
        file_path = r"C:\Testing documents\contentfile.txt"
        print("File exists:", os.path.exists(file_path))
        browse_input.set_input_files(file_path)
        save_attachment = page_object.page.locator(f"xpath={EmergencyContactLocators.ATTACHMENT_SAVE_BUTTON}")
        save_attachment.wait_for(state="visible",timeout=page_object.timeout)
        save_attachment.click()
        print("Attachment uploaded successfully")
    
    def download_attachment(page_object):
        download_button = page_object.page.locator(f"xpath={EmergencyContactLocators.DOWNLOAD_BUTTON}")
        download_button.wait_for(state="visible",timeout=page_object.timeout)
        download_button.scroll_into_view_if_needed()
        with page_object.page.expect_download() as download_info:download_button.click()
        download = download_info.value
        download.save_as(os.path.join(os.getcwd(),download.suggested_filename))
        print("File downloaded successfully")

    def add_contact_without_name(page_object, relationship, phone):
        page_object.click_add_button()
        page_object.enter_relationship(relationship)
        page_object.enter_phone(phone)
        page_object.click_save()
        print("Validation checked for mandatory Name field")

    def add_contact_without_relationship(page_object, name, phone):
        page_object.click_add_button()
        page_object.enter_name(name)
        page_object.enter_phone(phone)
        page_object.click_save()
        print("Validation checked for mandatory Relationship field")