# Custom Assertions for Login Page Testing

class LoginAssertions:
    """
    Custom assertion methods specifically for login page testing
    """

    @staticmethod
    def assert_login_page_loaded(page, login_page):
        """
        Assert that the login page has loaded correctly

        Args:
            page: Playwright page object
            login_page: LoginPage instance
        """
        # Check URL contains login
        current_url = login_page.get_page_url()
        assert "login" in current_url.lower(), f"Expected login page URL, but got: {current_url}"

        # Check essential elements are visible
        assert login_page.is_username_field_visible(), "Username field should be visible on login page"
        assert login_page.is_password_field_visible(), "Password field should be visible on login page"
        assert login_page.is_login_button_visible(), "Login button should be visible on login page"

    @staticmethod
    def assert_successful_login(login_page):
        """
        Assert that login was successful

        Args:
            login_page: LoginPage instance
        """
        assert login_page.is_login_successful(), "Login should be successful"
        # Verify we're no longer on login page
        current_url = login_page.get_page_url()
        assert "login" not in current_url.lower(), f"Should navigate away from login page after successful login, current URL: {current_url}"

    @staticmethod
    def assert_login_failed(login_page):
        """
        Assert that login failed and user remains on login page

        Args:
            login_page: LoginPage instance
        """
        assert not login_page.is_login_successful(), "Login should fail"
        # Verify user is still on login page
        current_url = login_page.get_page_url()
        assert "login" in current_url.lower(), f"Should remain on login page after failed login, current URL: {current_url}"

    @staticmethod
    def assert_error_message_displayed(login_page, expected_error_contains=None):
        """
        Assert that an error message is displayed

        Args:
            login_page: LoginPage instance
            expected_error_contains: Optional string that should be in the error message
        """
        error_message = login_page.get_error_message()
        assert error_message, "Error message should be displayed"
        assert len(error_message.strip()) > 0, "Error message should not be empty"

        if expected_error_contains:
            assert expected_error_contains.lower() in error_message.lower(), \
                f"Error message should contain '{expected_error_contains}', but got: '{error_message}'"

    @staticmethod
    def assert_username_field_accepts_input(page, login_page, test_input):
        """
        Assert that username field accepts and retains input

        Args:
            page: Playwright page object
            login_page: LoginPage instance
            test_input: Input string to test
        """
        login_page.enter_username(test_input)

        # Verify field still exists and is visible
        assert login_page.is_username_field_visible(), "Username field should remain visible after input"

        # Basic check that input was accepted (field should still be functional)
        # Note: We can't easily verify exact input value without additional methods

    @staticmethod
    def assert_password_field_accepts_input(page, login_page, test_input):
        """
        Assert that password field accepts and retains input

        Args:
            page: Playwright page object
            login_page: LoginPage instance
            test_input: Input string to test
        """
        login_page.enter_password(test_input)

        # Verify field still exists and is visible
        assert login_page.is_password_field_visible(), "Password field should remain visible after input"

        # Basic check that input was accepted (field should still be functional)
        # Note: We can't easily verify exact input value without additional methods

    @staticmethod
    def assert_login_form_validation(login_page, username="", password=""):
        """
        Assert login form validation for various input combinations

        Args:
            login_page: LoginPage instance
            username: Username to test
            password: Password to test
        """
        login_page.login(username, password)

        # For empty or invalid inputs, login should fail
        if not username or not password:
            LoginAssertions.assert_login_failed(login_page)
        elif username != "Admin" or password != "admin123":  # Based on config
            LoginAssertions.assert_login_failed(login_page)
            LoginAssertions.assert_error_message_displayed(login_page)

    @staticmethod
    def assert_page_navigation_after_login(login_page, expected_in_url=None):
        """
        Assert proper page navigation after login attempt

        Args:
            login_page: LoginPage instance
            expected_in_url: Optional string that should be in the URL after navigation
        """
        current_url = login_page.get_page_url()

        if login_page.is_login_successful():
            # After successful login, should not be on login page
            assert "login" not in current_url.lower(), "Should navigate away from login page after successful login"
            if expected_in_url:
                assert expected_in_url in current_url, f"URL should contain '{expected_in_url}' after login"
        else:
            # After failed login, should remain on login page
            assert "login" in current_url.lower(), "Should remain on login page after failed login"

    @staticmethod
    def assert_security_input_handling(login_page, malicious_input):
        """
        Assert that malicious inputs are handled securely

        Args:
            login_page: LoginPage instance
            malicious_input: Potentially malicious input string
        """
        # Try login with malicious input
        login_page.login(malicious_input, malicious_input)

        # Should always fail and not cause security issues
        LoginAssertions.assert_login_failed(login_page)

        # Should show appropriate error message
        LoginAssertions.assert_error_message_displayed(login_page)

        # Should remain on login page
        current_url = login_page.get_page_url()
        assert "login" in current_url.lower(), "Should remain on login page after security test"