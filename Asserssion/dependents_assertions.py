from Pages.dependents_page import Dependents_Page
from playwright.sync_api import expect
from Locators.dependents_locators import Dependents_Locators as dep_loc

class DependentsAssertions:
    """Assertions for Dependents page tests"""
      
    @staticmethod
    def assert_dependents_header_visible(page_obj: Dependents_Page):
        """Assert Dependents header is visible"""
        assert page_obj.is_assigned_dependents_header_visible(),"Assigned Dependents header should be visible"

    @staticmethod
    def assert_dependents_add_button_visible(page_obj: Dependents_Page):
        """Assert Add button is visible"""
        assert page_obj.is_assigned_dependents_add_button_visible(),"Add button for Assigned Dependents should be visible"

    @staticmethod
    def assert_attachments_header_visible(page_obj: Dependents_Page):
        """Assert Attachments header is visible"""
        assert page_obj.is_attachments_header_visible(),"Attachments header should be visible"

    @staticmethod
    def assert_attachments_add_button_visible(page_obj: Dependents_Page):
        """Assert Add button for Attachments is visible"""
        assert page_obj.is_attachments_add_button_visible(),"Add button for Attachments should be visible"  

    @staticmethod
    def assert_success_message_visible(page_obj: Dependents_Page):
        """Assert success message is visible"""
        expect(page_obj.page.locator(dep_loc.TOAST_MESSAGE)).to_be_visible(timeout=10000)
        # assert page_obj.is_success_message_visible(), \
        #     "Success message should be visible"

    @staticmethod
    def assert_success_message_text(page_obj: Dependents_Page, expected_text):
        """Assert success message contains expected text"""
        expect(page_obj.page.locator(dep_loc.TOAST_MESSAGE)).to_contain_text(expected_text, timeout=10000)
        # actual_text = page_obj.page.locator(dep_loc.TOAST_MESSAGE).inner_text()
        # assert expected_text in actual_text, \
        #     f"Expected success message to contain '{expected_text}' but got '{actual_text}'"

    @staticmethod
    def assert_success_message_not_visible(page_obj: Dependents_Page):
        """Assert success message is not visible"""
        expect(page_obj.page.locator(dep_loc.TOAST_MESSAGE)).not_to_be_visible(timeout=10000)

    @staticmethod
    def assert_other_relationship_input_visible(page_obj: Dependents_Page, name):
        """Assert 'Other Relationship' input is visible when 'Other' is selected"""
        assert page_obj.is_other_relationship_input_visible(name),"Other Relationship' input should be visible when 'Other' is selected in relationship dropdown"

    @staticmethod
    def assert_required_message_visible(page_obj: Dependents_Page):
        """Assert required message is visible for missing mandatory fields"""
        expect(page_obj.page.locator(dep_loc.REQUIRED_MESSAGE)).to_be_visible(timeout=10000), "Required message should be visible when trying to save without filling mandatory fields"

    @staticmethod
    def assert_required_message_not_visible(page_obj: Dependents_Page):
        """Assert required message is not visible when mandatory fields are filled"""
        expect(page_obj.page.locator(dep_loc.REQUIRED_MESSAGE)).not_to_be_visible(timeout=10000), "Required message should not be visible when mandatory fields are filled"
    
    @staticmethod
    def assert_attachment_name_visible(page_obj: Dependents_Page, attachment_name):
        """Assert added attachment is visible in the list"""
        #page_obj.page.wait_for_selector("text=basic-text.pdf", state="visible")
        expect(page_obj.page.locator(f"text={attachment_name}")).to_be_visible(timeout=10000)
    
    @staticmethod
    def assert_download_started(page_obj: Dependents_Page):
        """Assert download has started by checking for the download event"""
        with page_obj.page.expect_download(timeout=10000) as download_info:
            page_obj.click_download_attachment_button()
        download = download_info.value
        # Assertions
        assert download is not None
        # You can also check the suggested filename or save path if needed
        assert download.suggested_filename is not None
        # Optional: verify file name -- run using -s to see the print output
        print(download.suggested_filename)
        assert download.suggested_filename.endswith(".pdf")

    @staticmethod
    def assert_required_file_message_visible(page_obj: Dependents_Page):
        """Assert required message is visible when trying to save attachment without selecting a file"""
        expect(page_obj.page.locator(dep_loc.REQUIRED_FILE_MESSAGE)).to_be_visible(timeout=10000), "Required message should be visible when trying to save attachment without selecting a file"

    @staticmethod
    def assert_invalid_file_type_message_visible(page_obj: Dependents_Page):
        """Assert error message is visible when trying to upload an invalid file type"""
        expect(page_obj.page.get_by_text("File type not allowed")).to_be_visible(timeout=10000), "Error message should be visible when trying to upload an invalid file type"

    @staticmethod
    def assert_attachment_with_large_file_message_visible(page_obj: Dependents_Page):
        """Assert error message is visible when trying to upload a file that exceeds size limit"""
        expect(page_obj.page.get_by_text("Attachment Size Exceeded")).to_be_visible(timeout=10000), "Error message should be visible when trying to upload a file that exceeds size limit"   
