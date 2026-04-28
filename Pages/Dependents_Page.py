
from Locators.Dependents_Locators import Dependents_Locators as dep_loc

class Dependents_Page:

    def __init__(self, page):
        self.page = page

    def open_dependents_tab(self):
        self.page.click(dep_loc.DEPENDENTS_TAB)

    # ---- Visibility checks ----
    def is_assigned_dependents_header_visible(self):
        return self.page.locator(dep_loc.DEPENDENTS_HEADER).is_visible()

    def is_assigned_dependents_add_button_visible(self):
        return self.page.locator(dep_loc.ADD_DEPENDENT_BUTTON).is_visible()   

    def is_attachments_header_visible(self):
        return self.page.locator(dep_loc.ATTACHMENTS_HEADER).is_visible()
    
    def is_attachments_add_button_visible(self):
        return self.page.locator(dep_loc.ADD_ATTACHMENT_BUTTON).is_visible()

    def test_add_dependent(self):
        # Code to test adding a dependent
        pass

    def test_view_dependents(self):
        # Code to test viewing dependents
        pass

    def test_update_dependent_info(self):
        # Code to test updating dependent information
        pass

    def test_remove_dependent(self):
        # Code to test removing a dependent
        pass