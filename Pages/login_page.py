# Page Object Model for Login Page

from playwright.sync_api import Page, expect
from Locators.login_locators import LoginLocators
import time


class LoginPage:
    """
    Page Object Model for OrangeHRM Login Page
    """
    
    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page object
        
        Args:
            page: Playwright Page object
        """
        self.page = page
        self.locators = LoginLocators()
    
    def navigate_to_login(self, url: str):
        """
        Navigate to the login page
        
        Args:
            url: The login page URL
        """
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_load_state("domcontentloaded", timeout=60000)
    
    def enter_username(self, username: str):
        """
        Enter username in the username field
        
        Args:
            username: Username to enter
        """
        self.page.fill(self.locators.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """
        Enter password in the password field
        
        Args:
            password: Password to enter
        """
        self.page.fill(self.locators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """
        Click the login button
        """
        self.page.click(self.locators.LOGIN_BUTTON)
        time.sleep(2)  # Brief pause for page navigation
        self.page.wait_for_load_state("domcontentloaded", timeout=30000)
    
    def login(self, username: str, password: str):
        """
        Perform complete login flow
        
        Args:
            username: Username for login
            password: Password for login
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_login_successful(self) -> bool:
        """
        Verify if login was successful by checking for dashboard
        
        Returns:
            True if login successful, False otherwise
        """
        try:
            #self.page.wait_for_selector(self.locators.DASHBOARD_HEADER, timeout=5000)
            return self.page.get_by_role("heading", name="Dashboard").is_visible(timeout=5000)
            return True
        except:
            return False
    
    def get_error_message(self) -> str:
        """
        Get error message displayed on login page
        
        Returns:
            Error message text or empty string if no error
        """
        try:
            error = self.page.locator(self.locators.ALERT_MESSAGE)
            #error = self.page.locator("text=Invalid credentials")
            if error:
                return error.text_content().strip()
            return ""
        except:
            return ""
    
    def is_username_field_visible(self) -> bool:
        """
        Check if username field is visible
        
        Returns:
            True if visible, False otherwise
        """
        return self.page.is_visible(self.locators.USERNAME_INPUT)
    
    def is_password_field_visible(self) -> bool:
        """
        Check if password field is visible
        
        Returns:
            True if visible, False otherwise
        """
        return self.page.is_visible(self.locators.PASSWORD_INPUT)
    
    def is_login_button_visible(self) -> bool:
        """
        Check if login button is visible
        
        Returns:
            True if visible, False otherwise
        """
        return self.page.is_visible(self.locators.LOGIN_BUTTON)
    
    def get_page_url(self) -> str:
        """
        Get current page URL
        
        Returns:
            Current page URL
        """
        return self.page.url
