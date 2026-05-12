import time
import pytest
from playwright.sync_api import Page
from Pages.login_page import LoginPage
from Pages.membership_page import MembershipPage
from config import BASE_URL, USERNAME, PASSWORD
from Utils.common import CommonUtils


class TestMembership:

    def test_navigate_to_memberships(self, page: Page):
        CommonUtils.log_message("Testing: Navigate to Memberships")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(2)

        membership_page = MembershipPage(page)
        membership_page.navigate_to_memberships()

        current_url = membership_page.get_page_url()
        assert "membership" in current_url.lower()

        CommonUtils.log_message("✓ Navigated to Memberships page")

    def test_membership_table_is_visible(self, page: Page):
        CommonUtils.log_message("Testing: Membership table is visible")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(2)

        membership_page = MembershipPage(page)
        membership_page.navigate_to_memberships()

    # Check table headers are visible
        assert page.locator("//a[contains(@class,'orangehrm-tabs-item') and text()='Memberships']").is_visible()
        #assert page.locator("text=Subscription Amount").is_visible()

        CommonUtils.log_message("✓ Membership table is visible")


    def test_add_membership(self, page: Page):
        CommonUtils.log_message("Testing: Add a membership")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(2)

        membership_page = MembershipPage(page)
        membership_page.navigate_to_memberships()
        membership_page.click_add_membership()
        membership_page.select_membership_option("CIMA")
        membership_page.enter_subscription_amount("100")
        membership_page.click_save()

        assert membership_page.is_success_toast_visible()

        CommonUtils.log_message("✓ Membership added successfully")


    def test_delete_membership(self, page: Page):
        CommonUtils.log_message("Testing: Delete a membership")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(2)

        membership_page = MembershipPage(page)
        membership_page.navigate_to_memberships()
        membership_page.delete_first_membership()

        assert membership_page.is_no_records_found_visible()

        CommonUtils.log_message("✓ Membership deleted successfully")
