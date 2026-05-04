from playwright.sync_api import Page, sync_playwright, expect
from Locators.dependents_locators import Dependents_Locators as dep_loc
from Pages.dependents_page import Dependents_Page
from Asserssion.dependents_assertions import DependentsAssertions
import os

class TestPositiveDependentScenarios:
  
    def test_navigate_to_dependents_tab(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()       
        page.wait_for_load_state("networkidle")
        DependentsAssertions.assert_dependents_header_visible(dependents)
        DependentsAssertions.assert_dependents_add_button_visible(dependents)
        DependentsAssertions.assert_attachments_header_visible(dependents)
        DependentsAssertions.assert_attachments_add_button_visible(dependents)  
  
    def test_add_dependent_child(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()      
        dependents.add_dependent_child("John Doe", "2010-05-15")
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after adding dependent"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Saved"), "Success message should contain 'Success' text"

    def test_add_dependent_other_specify(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()    
        DependentsAssertions.assert_other_relationship_input_visible(dependents, "Johny Antony")
    
    def test_add_dependent_other(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()
        dependents.add_dependent_other("Jane Smith", "Spouse", "2015-09-30")
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after adding dependent"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Saved"), "Success message should contain 'SuccessSuccessfully Saved' text"
       
    def test_cancel_add_dependent(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()      
        dependents.click_add_button()
        dependents.fill_name("Jane Doe")
        dependents.select_relationship("Child")
        dependents.fill_date_of_birth("2012-08-20")
        dependents.click_cancel()
        DependentsAssertions.assert_success_message_not_visible(dependents), "Success message should not be visible after cancelling add dependent" 
     
    def test_edit_first_dependent_record(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab() 
        page.wait_for_timeout(2000)     
        page.locator(dep_loc.EDIT_BUTTON_1).first.click()    
        page.wait_for_timeout(2000)   
        dependents.fill_name("Aaana Doe Updated")
        page.wait_for_timeout(2000)
        dependents.click_save()
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after editing dependent"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Updated"), "Success message should contain 'SuccessSuccessfully Updated' text"
         
    def test_delete_first_dependent_record(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()      
        page.wait_for_timeout(2000)
        # Assuming the first row has a delete button with a specific locator
        page.locator(dep_loc.DELETE_BUTTON_1).first.click()
        page.wait_for_timeout(2000)
        # Confirm the deletion in the dialog
        page.click(dep_loc.DELETE_CONFIRM_BUTTON)
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after deleting dependent"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Deleted"), "Success message should contain 'SuccessSuccessfully Deleted' text"                

    #---Attachments tests can be added here---

    def test_add_attachment(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.add_attachment("C:\\Users\\athir\\Music\\Sample files\\basic-text.pdf", "Test attachment")
        # Validate success
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after adding attachment"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Saved"), "Success message should contain 'SuccessSuccessfully Saved' text"
        # Validate attachment is visible in the list
        DependentsAssertions.assert_attachment_name_visible(dependents, "basic-text.pdf"), "Added attachment should be visible in the list"

    def test_cancel_add_attachment(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.cancel_attachment("C:\\Users\\athir\\Music\\Sample files\\basic-text.pdf", "Test attachment")
        # Validate cancellation (attachment should not be added)
        DependentsAssertions.assert_success_message_not_visible(dependents), "Success message should not be visible after canceling attachment addition"

    def test_edit_first_attachment_record(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        page.wait_for_timeout(2000)     
        page.locator(dep_loc.EDIT_ATTACHMENT_BUTTON_1).first.click()    
        page.wait_for_timeout(2000)   
        dependents.add_attachment("C:\\Users\\athir\\Music\\Sample files\\abc.txt", "Test attachment changed")
        page.wait_for_timeout(2000)
        dependents.click_save()
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after editing dependent"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Updated"), "Success message should contain 'SuccessSuccessfully Updated' text"

    def test_download_first_attachment_record(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        DependentsAssertions.assert_download_started(dependents), "Attachment to be downloaded should be visible in the list" 
    
    def test_delete_first_attachment_record(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        page.wait_for_timeout(2000)
        # Assuming the first row has a delete button with a specific locator
        page.locator(dep_loc.DELETE_ATTACHMENT_BUTTON_1).first.click()
        page.wait_for_timeout(2000)
        # Confirm the deletion in the dialog
        page.click(dep_loc.DELETE_CONFIRM_BUTTON)
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after deleting attachment"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Deleted"), "Success message should contain 'SuccessSuccessfully Deleted' text"


class TestNegativeDependentScenarios:

    def test_add_dependent_without_name(self, page: Page):
        dependents = Dependents_Page(page)        
        dependents.open_dependents_tab()     
        dependents.click_add_button()
        dependents.select_relationship("Child")
        dependents.fill_date_of_birth("2015-03-10")
        dependents.click_save()
        DependentsAssertions.assert_required_message_visible(dependents)

    def test_add_dependent_without_relationship(self, page: Page):
        dependents = Dependents_Page(page)        
        dependents.open_dependents_tab()      
        dependents.click_add_button()
        dependents.fill_name("Emily Doe")
        dependents.fill_date_of_birth("2018-11-25")
        dependents.click_save()
        DependentsAssertions.assert_required_message_visible(dependents)

    def test_add_dependent_without_dob(self, page: Page):
        dependents = Dependents_Page(page)        
        dependents.open_dependents_tab()    
        dependents.click_add_button()
        dependents.fill_name("Michael Doe")
        dependents.select_relationship("Child")
        page.wait_for_timeout(2000)
        dependents.click_save()
        DependentsAssertions.assert_required_message_not_visible(dependents)

    def test_add_dependent_other_without_specifying_relationship(self, page: Page):
        dependents = Dependents_Page(page)        
        dependents.open_dependents_tab()  
        dependents.click_add_button()
        dependents.fill_name("Sarah Doe")
        dependents.select_relationship("Other")
        dependents.fill_date_of_birth("2017-06-05")
        dependents.click_save()
        DependentsAssertions.assert_required_message_visible(dependents)
             
    #---Attachments negative tests can be added here---
    def test_add_attachment_without_file(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        dependents.page.fill(dep_loc.COMMENT_TEXTAREA, "Attachment without file")
        dependents.page.click(dep_loc.SAVE_ATTACHMENT_BUTTON) 
        DependentsAssertions.assert_required_file_message_visible(dependents)

    def test_add_attachment_with_invalid_file_type(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        # Attempt to upload an unsupported file type (e.g., .exe)
        dependents.page.set_input_files(dep_loc.BROWSE_FILE_BUTTON, "C:\\Users\\athir\\Music\\Sample files\\jmap.exe")
        dependents.page.fill(dep_loc.COMMENT_TEXTAREA, "Attachment with invalid file type")
        dependents.page.click(dep_loc.SAVE_ATTACHMENT_BUTTON) 
        # Validate error message (assuming there's an error message for invalid file type)
        DependentsAssertions.assert_invalid_file_type_message_visible(dependents)

    def test_add_attachment_with_large_file(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        # Attempt to upload a large file (e.g., >1MB)
        dependents.page.set_input_files(dep_loc.BROWSE_FILE_BUTTON, "C:\\Users\\athir\\Music\\Sample files\\python-3.13.12-amd64.exe")
        dependents.page.fill(dep_loc.COMMENT_TEXTAREA, "Attachment with large file")
        dependents.page.click(dep_loc.SAVE_ATTACHMENT_BUTTON) 
        # Validate error message (assuming there's an error message)    
        DependentsAssertions.assert_attachment_with_large_file_message_visible(dependents)

    def test_add_attachment_without_comment(self, page: Page):
        dependents = Dependents_Page(page)
        dependents.open_dependents_tab()  
        dependents.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        dependents.page.set_input_files(dep_loc.BROWSE_FILE_BUTTON, "C:\\Users\\athir\\Music\\Sample files\\basic-text.pdf")
        dependents.page.click(dep_loc.SAVE_ATTACHMENT_BUTTON) 
        # Validate if attachment is added successfully without comment (assuming comment is optional)
        DependentsAssertions.assert_success_message_visible(dependents), "Success message should be visible after adding attachment without comment"
        DependentsAssertions.assert_success_message_text(dependents, "SuccessSuccessfully Saved"), "Success message should contain 'SuccessSuccessfully Saved' text"
        DependentsAssertions.assert_attachment_name_visible(dependents, "basic-text.pdf"), "Added attachment should be visible in the list even without comment"
