import pytest
from playwright.sync_api import Page
from Pages.contact_details_page import ContactDetailsPage
from config import USERNAME, PASSWORD, BASE_URL, TIMEOUT


@pytest.fixture(scope="function")
def logged_in_page(page: Page) -> Page:
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator("input[name='username']").fill(USERNAME)
    page.locator("input[name='password']").fill(PASSWORD)
    page.locator("button[type='submit']").click()
    page.wait_for_url("**/dashboard/**", timeout=TIMEOUT)
    return page


@pytest.fixture(scope="function")
def contact_details(logged_in_page: Page) -> ContactDetailsPage:
    cdp = ContactDetailsPage(logged_in_page)
    cdp.navigate_to_contact_details(emp_number=7)
    assert cdp.is_page_loaded(), "Contact Details page did not load in time."
    return cdp


class TestContactDetailsCompleteFlow:

    def test_tc001_fill_all_fields_and_save_successfully(self, contact_details: ContactDetailsPage):

        contact_details.fill_street1("123 Automation Avenue")
        contact_details.fill_street2("Suite 200")
        contact_details.fill_city("Toronto")
        contact_details.fill_state("Ontario")
        contact_details.fill_zip("M5V 3A8")
        contact_details.select_country("Canada")
        contact_details.fill_home_telephone("4161112222")
        contact_details.fill_work_telephone("4163334444")
        contact_details.fill_mobile("4165556666")
        contact_details.fill_work_email("qa.engineer@example.com")
        contact_details.fill_other_email("personal@example.com")

        contact_details.click_contact_details_save()

        toast = contact_details.get_success_toast_message()
        assert "Successfully" in toast, f"Unexpected toast message: '{toast}'"