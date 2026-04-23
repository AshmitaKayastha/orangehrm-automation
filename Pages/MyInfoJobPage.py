from Locators.MyInfoJobLocators import MyInfoJobLocators as loc

class MyInfoJobPage:

    def __init__(self, page):
        self.page = page

    def open_my_info(self):
        self.page.click(loc.MY_INFO)

    def open_job_tab(self):
        self.page.click(loc.JOB_TAB)

    def is_job_section_visible(self):
        return self.page.locator(loc.JOB_HEADER).is_visible()


    # ---- Visibility checks ----
    def is_joined_date_visible(self):
        return self.page.locator(loc.JOINED_DATE).is_visible()

    def is_job_title_visible(self):
        return self.page.locator(loc.JOB_TITLE).is_visible()

    def is_job_category_visible(self):
        return self.page.locator(loc.JOB_CATEGORY).is_visible()

    def is_sub_unit_visible(self):
        return self.page.locator(loc.SUB_UNIT).is_visible()

    def is_location_visible(self):
        return self.page.locator(loc.LOCATION).is_visible()

    def is_employment_status_visible(self):
        return self.page.locator(loc.EMPLOYMENT_STATUS).is_visible()

    

# #    ---- Contract handling ----
#     def enable_contract_details(self):
#         self.page.locator(loc.CONTRACT_TOGGLE).click()

#     def is_contract_start_visible(self):
#         return self.page.locator(loc.CONTRACT_START).is_visible()

#     def is_contract_end_visible(self):
#         return self.page.locator(loc.CONTRACT_END).is_visible()

 
    # ── MI-089: Contract section ───────────────────────────────────────────────
 
    def enable_contract_details(self):
        """Click the toggle to reveal contract date fields."""
        self.page.locator(loc.CONTRACT_TOGGLE).click()
        # Allow the section to animate / render
        self.page.wait_for_timeout(400)
 
    def is_contract_toggle_visible(self):
        return self.page.locator(loc.CONTRACT_TOGGLE).is_visible()
 
    def is_contract_start_visible(self):
        """Label 'Contract Start Date' is visible."""
        return self.page.locator(loc.CONTRACT_START).is_visible()
 
    def is_contract_end_visible(self):
        """Label 'Contract End Date' is visible."""
        return self.page.locator(loc.CONTRACT_END).is_visible()
 
    def is_contract_start_input_visible(self):
        """The actual date input for Contract Start Date is visible."""
        return self.page.locator(loc.CONTRACT_START_INPUT).is_visible()
 
    def is_contract_end_input_visible(self):
        """The actual date input for Contract End Date is visible."""
        return self.page.locator(loc.CONTRACT_END_INPUT).is_visible()
 
    def wait_for_contract_start(self, timeout: int = 5_000):
        self.page.locator(loc.CONTRACT_START).wait_for(state="visible", timeout=timeout)
 
    def wait_for_contract_end(self, timeout: int = 5_000):
        self.page.locator(loc.CONTRACT_END).wait_for(state="visible", timeout=timeout)