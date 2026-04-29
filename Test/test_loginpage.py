# Test Cases for OrangeHRM Login Page

import time

import pytest
from playwright.sync_api import Page
from Pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD
from Utils.common import CommonUtils
from Assertions.assertions import LoginAssertions


class TestPositiveLoginScenarios:
    """
    Positive Test Cases - Happy Path Scenarios
    """

    def test_user_can_access_login_page(self, page: Page):
        """
        Test: User can open the login page successfully
        """
        CommonUtils.log_message("Testing: Can user access login page?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Use custom assertion to verify login page loaded correctly

        time.sleep(20)  # Brief pause to ensure page is fully loaded before assertions

        LoginAssertions.assert_login_page_loaded(page, login_page)

        CommonUtils.log_message("✓ User can access login page")


    def test_successful_login_with_correct_credentials(self, page: Page):
        """
        Test: User can login successfully with correct username and password
        """
        CommonUtils.log_message("Testing: Can user login with correct credentials?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Enter correct username and password
        login_page.login(USERNAME, PASSWORD)

        # Use custom assertion to verify successful login
        LoginAssertions.assert_successful_login(login_page)

        CommonUtils.log_message("✓ User can login successfully with correct credentials")

    

class TestNegativeLoginScenarios:
    """
    Negative Test Cases - Error Scenarios
    """

    def test_login_fails_with_wrong_username(self, page: Page):
        """
        Test: Login fails when username is incorrect
        """
        CommonUtils.log_message("Testing: What happens with wrong username?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Try login with wrong username
        login_page.login("wronguser", PASSWORD)

        # Use custom assertions to verify login failed and error is shown
        LoginAssertions.assert_login_failed(login_page)
        LoginAssertions.assert_error_message_displayed(login_page)

        CommonUtils.log_message("✓ Login correctly fails with wrong username")

    def test_login_fails_with_wrong_password(self, page: Page):
        """
        Test: Login fails when password is incorrect
        """
        CommonUtils.log_message("Testing: What happens with wrong password?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Try login with wrong password
        login_page.login(USERNAME, "wrongpass")

        # Use custom assertions to verify login failed and error is shown
        LoginAssertions.assert_login_failed(login_page)
        LoginAssertions.assert_error_message_displayed(login_page)

        CommonUtils.log_message("✓ Login correctly fails with wrong password")

    def test_login_fails_with_empty_username(self, page: Page):
        """
        Test: Login fails when username field is empty
        """
        CommonUtils.log_message("Testing: What happens with empty username?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Try login with empty username
        LoginAssertions.assert_login_form_validation(login_page, "", PASSWORD)

        CommonUtils.log_message("✓ Login correctly fails with empty username")

    def test_login_fails_with_empty_password(self, page: Page):
        """
        Test: Login fails when password field is empty
        """
        CommonUtils.log_message("Testing: What happens with empty password?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Try login with empty password
        LoginAssertions.assert_login_form_validation(login_page, USERNAME, "")

        CommonUtils.log_message("✓ Login correctly fails with empty password")

    def test_login_fails_with_both_fields_empty(self, page: Page):
        """
        Test: Login fails when both username and password are empty
        """
        CommonUtils.log_message("Testing: What happens with both fields empty?")

        login_page = LoginPage(page)
        login_page.navigate_to_login(BASE_URL)

        # Try login with both fields empty
        LoginAssertions.assert_login_form_validation(login_page, "", "")

        CommonUtils.log_message("✓ Login correctly fails with both fields empty")
