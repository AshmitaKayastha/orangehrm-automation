import re
from playwright.sync_api import Page, expect

class JobTitleAssertions:
    def __init__(self, page: Page):
        self.page = page

    def verify_navigation_success(self):
        expect(self.page).to_have_url(re.compile(r".*/admin/viewJobTitleList"))

    def verify_success_message(self):
        success_toast = self.page.locator(".oxd-toast-content--success")
        expect(success_toast).to_be_visible()
        expect(success_toast).to_contain_text("Successfully Saved")