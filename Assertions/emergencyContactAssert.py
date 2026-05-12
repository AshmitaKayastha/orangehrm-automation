from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class emergencyContactAssert:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def verify_contact_present(self, name):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[contains(text(),'{name}')]")
            )
        )
        assert element.is_displayed(), f"Contact '{name}' is NOT displayed"

    def verify_add_button(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']")
            )
        )
        assert element.is_displayed(), "Add button is NOT displayed"

    def verify_edit_form_opened(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[contains(text(),'Emergency Contact')]")
            )
        )
        assert element.is_displayed(), "Edit form is NOT opened"

    