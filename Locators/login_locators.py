# Locators for Login Page

class LoginLocators:
    """
    Contains all locators for the OrangeHRM Login page
    """

    # Username Input Field
    USERNAME_INPUT = ".oxd-input[name='username']"

    # Password Input Field
    PASSWORD_INPUT = ".oxd-input[type='password']"

    # Login Button
    LOGIN_BUTTON = ".oxd-button[type='submit']"

    # Invalid Credentials Alert
    INVALID_ALERT = ".oxd-alert"
    ALERT_MESSAGE = "p.oxd-text.oxd-alert-content-text"

    # Forgot Password Link
    FORGOT_PASSWORD_LINK = ".orangehrm-login-forgot"

    # Page Title (for verification)
    PAGE_TITLE = ".orangehrm-login-branding"

    # Error Message Container
    ERROR_MESSAGE = ".oxd-input-field-error-message"

    # Dashboard Header (after successful login)
    DASHBOARD_HEADER = ".oxd-topbar-header-title"
