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

    # ---- Field Visibility checks ----
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

    # ---- MI-089: Contract section handling ----
    # def enable_contract_details(self):
    #     """Scrolls to the toggle and clicks it."""
    #     toggle = self.page.locator(loc.CONTRACT_TOGGLE)
    #     toggle.scroll_into_view_if_needed() # Add this line
    #     toggle.click()
    #     # Wait for the fields to become visible after the animation
    #     self.page.locator(loc.CONTRACT_START).wait_for(state="visible")

    # def is_contract_start_visible(self):
    #     return self.page.locator(loc.CONTRACT_START).is_visible()

    # def is_contract_end_visible(self):
    #     return self.page.locator(loc.CONTRACT_END).is_visible()