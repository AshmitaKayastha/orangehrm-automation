# Common Utility Functions

import os
from datetime import datetime
from pathlib import Path


class CommonUtils:
    """
    Common utility functions for test automation
    """
    
    @staticmethod
    def create_screenshot_directory():
        """
        Create screenshots directory if it doesn't exist
        
        Returns:
            Path to the screenshots directory
        """
        screenshot_dir = "Reports/Screenshots"
        Path(screenshot_dir).mkdir(parents=True, exist_ok=True)
        return screenshot_dir
    
    @staticmethod
    def take_screenshot(page, test_name: str):
        """
        Take a screenshot and save with timestamp
        
        Args:
            page: Playwright page object
            test_name: Name of the test
            
        Returns:
            Path to the saved screenshot
        """
        screenshot_dir = CommonUtils.create_screenshot_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        page.screenshot(path=screenshot_path)
        return screenshot_path
    
    @staticmethod
    def log_message(message: str):
        """
        Print log message with timestamp
        
        Args:
            message: Message to log
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    @staticmethod
    def create_report_directory():
        """
        Create reports directory if it doesn't exist
        
        Returns:
            Path to the reports directory
        """
        Path("Reports").mkdir(parents=True, exist_ok=True)
        return "Reports"
