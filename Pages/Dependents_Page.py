from playwright.sync_api import Page, expect
from Locators.dependents_locators import Dependents_Locators as dep_loc
from Pages.login_page import LoginPage
from Pages.MyInfoJobPage import MyInfoJobPage
from config import BASE_URL, USERNAME, PASSWORD


class Dependents_Page:

    def __init__(self, page):
        self.page = page

    def open_dependents_tab(self):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)

        myInfo = MyInfoJobPage(self.page)
        myInfo.open_my_info()   
        self.page.click(dep_loc.DEPENDENTS_TAB)

    # ---- Visibility checks ----
    def is_assigned_dependents_header_visible(self):
        return self.page.locator(dep_loc.DEPENDENTS_HEADER).is_visible(timeout=10000)

    def is_assigned_dependents_add_button_visible(self):
        return self.page.locator(dep_loc.ADD_DEPENDENT_BUTTON).is_visible(timeout=10000)   

    def is_attachments_header_visible(self):
        return self.page.locator(dep_loc.ATTACHMENTS_HEADER).is_visible(timeout=10000)
    
    def is_attachments_add_button_visible(self):
        return self.page.locator(dep_loc.ADD_ATTACHMENT_BUTTON).is_visible(timeout=10000)

    def is_other_relationship_input_visible(self, name):    
        self.click_add_button()
        self.fill_name(name)
        self.select_relationship("Other")
        return self.page.locator(dep_loc.OTHER_RELATIONSHIP_INPUT).is_visible()

    # ---------------- Actions ----------------
    def click_add_button(self):
        self.page.click(dep_loc.ADD_DEPENDENT_BUTTON)

    def fill_name(self, name):
        #self.page.locator(dep_loc.NAME_INPUT).clear()
        self.page.locator("input").nth(1).clear()
        self.page.locator("input").nth(1).fill(name)
        #self.page.get_by_label("Name").click()
        #self.page.get_by_label("Name").fill(name)

    def fill_date_of_birth(self, dob):
        #self.page.locator(dep_loc.DATE_OF_BIRTH_INPUT).click()
        #self.page.locator(dep_loc.DATE_OF_BIRTH_INPUT).fill(dob)
        self.page.get_by_placeholder("yyyy-dd-mm", exact=True).click()
        #expect(self.page.get_by_placeholder("yyyy-mm-dd")).to_be_visible(timeout=10000)
        #self.page.get_by_placeholder("yyyy-mm-dd").wait_for(state="visible").fill(dob)
        self.page.get_by_placeholder("yyyy-dd-mm").fill(dob)
        
    def select_relationship(self, Relationship_option):
        self.page.locator(dep_loc.RELATIONSHIP_DROPDOWN).click()
        self.page.get_by_role("option", name=Relationship_option).click()
   
    def select_relationship_other_specify_relationship(self, relation):
        self.page.locator(dep_loc.OTHER_RELATIONSHIP_INPUT).fill(relation)

    def click_save(self):
        self.page.click(dep_loc.SAVE_BUTTON)

    def click_cancel(self):
        self.page.click(dep_loc.CANCEL_BUTTON)

    def add_dependent_child(self, name, dob):
        self.click_add_button()
        self.fill_name(name)
        self.select_relationship("Child")
        self.fill_date_of_birth(dob)
        self.click_save()

    def add_dependent_other(self, name, Specify_relation, dob):
        self.click_add_button()
        self.fill_name(name)
        self.select_relationship("Other")
        self.select_relationship_other_specify_relationship (Specify_relation)
        self.fill_date_of_birth(dob)
        self.click_save()
       

    # #---------------- Success Message ------------
    # def is_success_message_visible(self):
    #     return self.page.locator(dep_loc.TOAST_MESSAGE).is_visible(timeout=20000)

    #---------------- Attachments ----------------
    def add_attachment(self, file_path, comment_text):
        self.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        # Assuming there's a file input that becomes visible after clicking add
        self.page.set_input_files(dep_loc.BROWSE_FILE_BUTTON, file_path)
        self.page.fill(dep_loc.COMMENT_TEXTAREA, comment_text)
        #self.page.wait_for_timeout(2000)
        # Click save or upload button if necessary
        self.page.click(dep_loc.SAVE_ATTACHMENT_BUTTON) 
        #self.page.wait_for_timeout(2000)  # Wait for upload to complete, adjust as needed  

    def cancel_attachment(self, file_path, comment_text):
        self.page.click(dep_loc.ADD_ATTACHMENT_BUTTON)
        self.page.set_input_files(dep_loc.BROWSE_FILE_BUTTON, file_path)
        self.page.fill(dep_loc.COMMENT_TEXTAREA, comment_text)
        #self.page.wait_for_timeout(2000)
        self.page.click(dep_loc.CANCEL_BUTTON) 
        #self.page.wait_for_timeout(2000)  # Wait for cancellation to complete, adjust as needed

    def click_download_attachment_button(self):
        self.page.locator(dep_loc.DOWNLOAD_ATTACHMENT_BUTTON_1).first.click()   
  


