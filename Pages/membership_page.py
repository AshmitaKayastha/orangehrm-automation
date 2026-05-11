# Page Object Model for Membership Page

import time
from playwright.sync_api import Page
from Locators.membership_locators import MembershipLocators


class MembershipPage:
    """
    Page Object Model for OrangeHRM Membership Page
    """

    def __init__(self, page: Page):
        self.page = page
        self.locators = MembershipLocators()

    # ------------------------------------------------------------------ #
    #  Navigation
    # ------------------------------------------------------------------ #

    def navigate_to_memberships(self):
        """
        Click the Memberships link in the left sidebar.
        Call this AFTER logging in and opening the My Info section.
        """
        self.page.click(self.locators.MEMBERSHIPS_MENU_ITEM)
        time.sleep(2)
        self.page.wait_for_load_state("domcontentloaded", timeout=30000)

    # ------------------------------------------------------------------ #
    #  Assigned Memberships — Add
    # ------------------------------------------------------------------ #

    def click_add_membership(self):
        """Click the first '+ Add' button (Assigned Memberships section)."""
        self.page.click(self.locators.ADD_MEMBERSHIP_BUTTON)
        time.sleep(1)

    def select_membership_option(self, option_text: str):
        """
        Pick a membership from the Membership dropdown.

        Args:
            option_text: Visible text of the option, e.g. 'CPIM'
        """
        self.page.click(self.locators.MEMBERSHIP_DROPDOWN)
        time.sleep(1)
        self.page.get_by_role("option", name=option_text).click()

    def enter_subscription_amount(self, amount: str):
        """
        Type into the Subscription Amount field.

        Args:
            amount: Amount as a string, e.g. '100'
        """
        self.page.fill(self.locators.SUBSCRIPTION_AMOUNT_INPUT, amount)

    def click_save(self):
        """Click the Save / submit button inside the form."""
        self.page.click(self.locators.SAVE_BUTTON)
        time.sleep(2)

    def click_cancel(self):
        """Click Cancel to dismiss the form without saving."""
        self.page.click(self.locators.CANCEL_BUTTON)
        time.sleep(1)

    # ------------------------------------------------------------------ #
    #  Assigned Memberships — Delete
    # ------------------------------------------------------------------ #

    def delete_first_membership(self):
        """Click delete on the first row, then confirm."""
        self.page.click(self.locators.DELETE_MEMBERSHIP_BUTTON)
        time.sleep(1)
        self.page.click(self.locators.CONFIRM_DELETE_BUTTON)
        time.sleep(2)

    # ------------------------------------------------------------------ #
    #  Attachments — Add
    # ------------------------------------------------------------------ #

    def click_add_attachment(self):
        """Click the second '+ Add' button (Attachments section)."""
        self.page.click(self.locators.ADD_ATTACHMENT_BUTTON)
        time.sleep(1)

    def upload_attachment_file(self, file_path: str):
        """
        Set the file input for attachment upload.

        Args:
            file_path: Absolute or relative path to the file, e.g. 'test_data/sample.txt'
        """
        self.page.set_input_files(self.locators.ATTACHMENT_FILE_INPUT, file_path)
        time.sleep(1)

    def enter_attachment_description(self, description: str):
        """
        Type a description for the attachment.

        Args:
            description: Description text
        """
        self.page.fill(self.locators.ATTACHMENT_DESCRIPTION_INPUT, description)

    # ------------------------------------------------------------------ #
    #  Attachments — Delete
    # ------------------------------------------------------------------ #

    def delete_first_attachment(self):
        """Click delete on the first attachment row, then confirm."""
        self.page.click(self.locators.DELETE_ATTACHMENT_BUTTON)
        time.sleep(1)
        self.page.click(self.locators.CONFIRM_DELETE_BUTTON)
        time.sleep(2)

    # ------------------------------------------------------------------ #
    #  State Checks (used by assertions)
    # ------------------------------------------------------------------ #

    def is_success_toast_visible(self) -> bool:
        """Return True if the green success toast is visible."""
        try:
            return self.page.locator(self.locators.SUCCESS_TOAST).is_visible(timeout=5000)
        except:
            return False

    def is_no_records_found_visible(self) -> bool:
        """Return True if 'No Records Found' text is shown in Assigned Memberships."""
        try:
            return self.page.locator(self.locators.NO_RECORDS_FOUND).is_visible(timeout=5000)
        except:
            return False

    def is_attachment_record_visible(self) -> bool:
        """Return True if at least one attachment record count label is visible."""
        try:
            return self.page.locator(self.locators.ATTACHMENT_RECORD_COUNT).is_visible(timeout=5000)
        except:
            return False

    def get_page_url(self) -> str:
        """Return the current page URL."""
        return self.page.url