# Main Entry Point for OrangeHRM Automation Tests

import subprocess
import sys
from pathlib import Path


def run_tests():
    """
    Run the test suite using pytest
    """
    print("=" * 60)
    print("OrangeHRM Automation Test Suite")
    print("=" * 60)
    
    # Create reports directory
    Path("Reports").mkdir(parents=True, exist_ok=True)
    
    # Run pytest with various options
    pytest_args = [
        "pytest",
        "Test/",
        "-v",  # Verbose output
        "-s",  # Show print statements
        "--tb=short",  # Short traceback format
        f"--html=Reports/report.html",  # HTML report
        "--self-contained-html",  # Self-contained HTML report
    ]
    
    print("Running tests...")
    result = subprocess.run(pytest_args, cwd=Path(__file__).parent)
    
    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
