

from config import BASE_URL, USERNAME, PASSWORD
from playwright.sync_api import Page, sync_playwright
from Pages.login_page import LoginPage
from Pages.MyInfoJobPage import MyInfoJobPage
from Pages.Dependents_Page import Dependents_Page

class TestPositiveDependentScenarios:
  
    def test_navigate_to_dependents_tab(self, page: Page):

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)

        myInfo = MyInfoJobPage(page)
        dependents = Dependents_Page(page)

        myInfo.open_my_info()
        dependents.open_dependents_tab()       

        page.wait_for_load_state("networkidle")


        assert dependents.is_assigned_dependents_header_visible(), "Assigned Dependents header is not visible"
        assert dependents.is_assigned_dependents_add_button_visible(), "Add button for Assigned Dependents is not visible"
        assert dependents.is_attachments_header_visible(), "Attachments header is not visible"  
        assert dependents.is_attachments_add_button_visible(), "Add button for Attachments is not visible"
  
    
 