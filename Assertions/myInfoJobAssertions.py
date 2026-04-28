class MyInfoJobAssertions:
    """
    Custom assertion methods specifically for MyInfo Job page testing
    """

    @staticmethod
    def assert_job_tab_navigated(job_page):
        """Assert Job tab is visible after navigation (MI-081)"""
        assert job_page.is_job_section_visible(), "Job section should be visible after navigating to Job tab"

    @staticmethod
    def assert_all_job_fields_visible(job_page):
        """Assert all primary Job fields are visible (MI-082 to MI-088)"""
        fields = [
            ("Joined Date", job_page.is_joined_date_visible),
            ("Job Title", job_page.is_job_title_visible),
            ("Job Category", job_page.is_job_category_visible),
            ("Sub Unit", job_page.is_sub_unit_visible),
            ("Location", job_page.is_location_visible),
            ("Employment Status", job_page.is_employment_status_visible),
        ]
        
        for field_name, check_method in fields:
            assert check_method(), f"{field_name} should be visible on Job page"

    @staticmethod
    def assert_contract_fields_visible(job_page):
        """Assert Contract fields are visible (MI-089)"""
        assert job_page.is_contract_start_visible(), "Contract Start Date should be visible"
        assert job_page.is_contract_end_visible(), "Contract End Date should be visible"