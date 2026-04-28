import re
from playwright.sync_api import Page, expect
from Locators.contact_details_locators import ContactDetailsLocators
from config import BASE_URL, TIMEOUT


class ContactDetailsPage:
    """
    Page Object Model for OrangeHRM – Employee Contact Details page.
    URL pattern: /web/index.php/pim/contactDetails/empNumber/{emp_number}
    """

    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactDetailsLocators()
        self.timeout = TIMEOUT

    # ──────────────────────────────────────────────────────────────────────────
    # Navigation
    # ──────────────────────────────────────────────────────────────────────────

    def navigate_to_contact_details(self, emp_number: int = 7) -> None:
        """Navigate directly to the Contact Details page for the given employee."""
        url = BASE_URL.replace(
            "/auth/login",
            f"/pim/contactDetails/empNumber/{emp_number}"
        )
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    # ──────────────────────────────────────────────────────────────────────────
    # Assertions / State Checks
    # ──────────────────────────────────────────────────────────────────────────

    def is_page_loaded(self) -> bool:
        """Return True when the Contact Details form is visible."""
        try:
            self.page.wait_for_selector(
                self.locators.BTN_CONTACT_DETAILS_SAVE,
                timeout=self.timeout
            )
            return True
        except Exception:
            return False

    def get_page_header_text(self) -> str:
        return self.page.locator(self.locators.PAGE_HEADER).inner_text()

    # ──────────────────────────────────────────────────────────────────────────
    # Getters – read current field values
    # ──────────────────────────────────────────────────────────────────────────

    def get_street1(self) -> str:
        return self.page.locator(self.locators.INPUT_STREET1).input_value()

    def get_street2(self) -> str:
        return self.page.locator(self.locators.INPUT_STREET2).input_value()

    def get_city(self) -> str:
        return self.page.locator(self.locators.INPUT_CITY).input_value()

    def get_state(self) -> str:
        return self.page.locator(self.locators.INPUT_STATE).input_value()

    def get_zip(self) -> str:
        return self.page.locator(self.locators.INPUT_ZIP).input_value()

    def get_country(self) -> str:
        return self.page.locator(self.locators.DROPDOWN_COUNTRY_INPUT).inner_text()

    def get_home_telephone(self) -> str:
        return self.page.locator(self.locators.INPUT_HOME_TELEPHONE).input_value()

    def get_work_telephone(self) -> str:
        return self.page.locator(self.locators.INPUT_WORK_TELEPHONE).input_value()

    def get_mobile(self) -> str:
        return self.page.locator(self.locators.INPUT_MOBILE).input_value()

    def get_work_email(self) -> str:
        return self.page.locator(self.locators.INPUT_WORK_EMAIL).input_value()

    def get_other_email(self) -> str:
        return self.page.locator(self.locators.INPUT_OTHER_EMAIL).input_value()

    # ──────────────────────────────────────────────────────────────────────────
    # Setters – fill individual fields
    # ──────────────────────────────────────────────────────────────────────────

    def fill_street1(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_STREET1)
        field.clear()
        field.fill(value)

    def fill_street2(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_STREET2)
        field.clear()
        field.fill(value)

    def fill_city(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_CITY)
        field.clear()
        field.fill(value)

    def fill_state(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_STATE)
        field.clear()
        field.fill(value)

    def fill_zip(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_ZIP)
        field.clear()
        field.fill(value)

    def select_country(self, country: str):
        dropdown = self.page.locator(self.locators.DROPDOWN_COUNTRY).first
        dropdown.click()

        options = self.page.locator("//div[@role='listbox']//span")
        options.filter(has_text=country).first.click()

    def fill_home_telephone(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_HOME_TELEPHONE)
        field.clear()
        field.fill(value)

    def fill_work_telephone(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_WORK_TELEPHONE)
        field.clear()
        field.fill(value)

    def fill_mobile(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_MOBILE)
        field.clear()
        field.fill(value)

    def fill_work_email(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_WORK_EMAIL)
        field.clear()
        field.fill(value)

    def fill_other_email(self, value: str) -> None:
        field = self.page.locator(self.locators.INPUT_OTHER_EMAIL)
        field.clear()
        field.fill(value)

    # ──────────────────────────────────────────────────────────────────────────
    # Composite Actions
    # ──────────────────────────────────────────────────────────────────────────

    def fill_contact_details(
        self,
        street1: str = "",
        street2: str = "",
        city: str = "",
        state: str = "",
        zip_code: str = "",
        country: str = "",
        home_telephone: str = "",
        work_telephone: str = "",
        mobile: str = "",
        work_email: str = "",
        other_email: str = "",
    ) -> None:
        """Fill all Contact Details form fields in one call."""
        if street1:
            self.fill_street1(street1)
        if street2:
            self.fill_street2(street2)
        if city:
            self.fill_city(city)
        if state:
            self.fill_state(state)
        if zip_code:
            self.fill_zip(zip_code)
        if country:
            self.select_country(country)
        if home_telephone:
            self.fill_home_telephone(home_telephone)
        if work_telephone:
            self.fill_work_telephone(work_telephone)
        if mobile:
            self.fill_mobile(mobile)
        if work_email:
            self.fill_work_email(work_email)
        if other_email:
            self.fill_other_email(other_email)

    def click_contact_details_save(self) -> None:
        """Click the Save button for the Contact Details section."""
        self.page.locator(self.locators.BTN_CONTACT_DETAILS_SAVE).click()

    def save_contact_details(
        self,
        street1: str = "",
        street2: str = "",
        city: str = "",
        state: str = "",
        zip_code: str = "",
        country: str = "",
        home_telephone: str = "",
        work_telephone: str = "",
        mobile: str = "",
        work_email: str = "",
        other_email: str = "",
    ) -> None:
        """Fill fields then save – convenience wrapper."""
        self.fill_contact_details(
            street1=street1,
            street2=street2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            home_telephone=home_telephone,
            work_telephone=work_telephone,
            mobile=mobile,
            work_email=work_email,
            other_email=other_email,
        )
        self.click_contact_details_save()

    # ──────────────────────────────────────────────────────────────────────────
    # Toast Helpers
    # ──────────────────────────────────────────────────────────────────────────

    def get_success_toast_message(self) -> str:
        """Wait for and return the success toast message text."""
        self.page.wait_for_selector(self.locators.TOAST_SUCCESS, timeout=self.timeout)
        return self.page.locator(self.locators.TOAST_SUCCESS).inner_text()

    def get_error_toast_message(self) -> str:
        """Wait for and return the error toast message text."""
        self.page.wait_for_selector(self.locators.TOAST_ERROR, timeout=self.timeout)
        return self.page.locator(self.locators.TOAST_ERROR).inner_text()

    def get_validation_messages(self) -> list[str]:
        """Return all inline field validation error messages."""
        self.page.wait_for_selector(self.locators.VALIDATION_MESSAGE, timeout=self.timeout)
        msgs = self.page.locator(self.locators.VALIDATION_MESSAGE)
        return [msgs.nth(i).inner_text() for i in range(msgs.count())]

    # ──────────────────────────────────────────────────────────────────────────
    # Emergency Contacts
    # ──────────────────────────────────────────────────────────────────────────

    def click_add_emergency_contact(self) -> None:
        self.page.locator(self.locators.BTN_ADD_EMERGENCY_CONTACT).click()
        # Wait for the modal/inline form to appear
        self.page.wait_for_selector(self.locators.INPUT_EC_NAME, timeout=self.timeout)

    def fill_emergency_contact_form(
        self,
        name: str,
        relationship: str,
        home_phone: str = "",
        mobile: str = "",
        work_phone: str = "",
    ) -> None:
        self.page.locator(self.locators.INPUT_EC_NAME).fill(name)
        self.page.locator(self.locators.INPUT_EC_RELATIONSHIP).fill(relationship)
        if home_phone:
            self.page.locator(self.locators.INPUT_EC_HOME_PHONE).fill(home_phone)
        if mobile:
            self.page.locator(self.locators.INPUT_EC_MOBILE).fill(mobile)
        if work_phone:
            self.page.locator(self.locators.INPUT_EC_WORK_PHONE).fill(work_phone)

    def save_emergency_contact(self) -> None:
        self.page.locator(self.locators.BTN_EC_SAVE).click()

    def cancel_emergency_contact(self) -> None:
        self.page.locator(self.locators.BTN_EC_CANCEL).click()

    def add_emergency_contact(
        self,
        name: str,
        relationship: str,
        home_phone: str = "",
        mobile: str = "",
        work_phone: str = "",
    ) -> None:
        """Open form, fill it, and save – all in one call."""
        self.click_add_emergency_contact()
        self.fill_emergency_contact_form(name, relationship, home_phone, mobile, work_phone)
        self.save_emergency_contact()

    def get_emergency_contact_rows(self):
        """Return all emergency contact table row locators."""
        return self.page.locator(self.locators.EC_TABLE_ROWS)

    def get_emergency_contact_count(self) -> int:
        return self.get_emergency_contact_rows().count()

    def get_first_emergency_contact_name(self) -> str:
        return self.page.locator(self.locators.EC_TABLE_FIRST_ROW_NAME).inner_text()

    def click_edit_emergency_contact(self, row_index: int = 0) -> None:
        row = self.get_emergency_contact_rows().nth(row_index)
        row.locator(self.locators.BTN_EC_ROW_EDIT).click()
        self.page.wait_for_selector(self.locators.INPUT_EC_NAME, timeout=self.timeout)

    def click_delete_emergency_contact(self, row_index: int = 0) -> None:
        row = self.get_emergency_contact_rows().nth(row_index)
        row.locator(self.locators.BTN_EC_ROW_DELETE).click()

    def confirm_delete_emergency_contact(self) -> None:
        self.page.locator(self.locators.BTN_CONFIRM_DELETE).click()

    def delete_emergency_contact(self, row_index: int = 0) -> None:
        """Click delete on the given row and confirm the dialog."""
        self.click_delete_emergency_contact(row_index)
        self.page.wait_for_selector(self.locators.BTN_CONFIRM_DELETE, timeout=self.timeout)
        self.confirm_delete_emergency_contact()