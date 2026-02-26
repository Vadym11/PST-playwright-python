from __future__ import annotations
from playwright.sync_api import Page, Locator, expect

from lib.api_models.user import CreateUser
from lib.pages.base_page import BasePage

class AuthPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Login Page Locators
        self.__register_link: Locator = self._page.get_by_test_id("register-link")
        self.__login_header: Locator = page.get_by_role('heading', name='Login')
        self.__email_input: Locator = page.get_by_test_id('email')
        self.__password_input: Locator = page.get_by_test_id('password')
        self.__google_sign_in_button: Locator = page.get_by_role('button', name='Sign in with Google')

        # Register Page Locators
        self.__first_name_input = self._page.get_by_test_id("first-name")
        self.__last_name_input = self._page.get_by_test_id("last-name")
        self.__dob_input = self._page.get_by_test_id("dob")
        self.__phone_input = self._page.get_by_test_id("phone")
        self.__street_input = self._page.get_by_test_id("street")
        self.__city_input = self._page.get_by_test_id("city")
        self.__state_input = self._page.get_by_test_id("state")
        self.__postal_code_input = self._page.get_by_test_id("postal_code")
        self.__country_selector = self._page.get_by_test_id("country")
        self.__email_input = self._page.get_by_test_id("email")
        self.__password_input = self._page.get_by_test_id("password")
        self.__register_button = self._page.get_by_test_id("register-submit")

    # Login Page Methods
    def click_register_link(self) -> AuthPage:
        """Click the register link."""
        self.__register_link.click()

        return self

    def get_login_header(self) -> Locator:
        """Get the login header element."""
        return self.__login_header

    def assert_login_page(self) -> None:
        """Assert that the login page is displayed."""
        expect(self.__login_header).to_be_visible()
        expect(self.__google_sign_in_button).to_be_visible()
        expect(self.__email_input).to_be_visible()
        expect(self.__password_input).to_be_visible()

    # Register Page Methods
    def enter_first_name(self, first_name: str) -> None:
        """Enter the first name."""
        self.__first_name_input.wait_for(state='visible')
        self.__first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Enter the last name."""
        self.__last_name_input.fill(last_name)

    def enter_dob(self, dob: str) -> None:
        """Enter the date of birth."""
        self.__dob_input.fill(dob)

    def enter_street(self, street: str) -> None:
        """Enter the street address."""
        self.__street_input.fill(street)

    def enter_city(self, city: str) -> None:
        """Enter the city."""
        self.__city_input.fill(city)

    def enter_state(self, state: str) -> None:
        """Enter the state."""
        self.__state_input.fill(state)

    def enter_postal_code(self, postal_code: str) -> None:
        """Enter the postal code."""
        self.__postal_code_input.fill(postal_code)

    def enter_country(self, country: str) -> None:
        """Enter the country."""
        self.__country_selector.click()
        self._page.keyboard.type(country)
        self._page.keyboard.press('Enter')
        # self.__country_input.fill(country)

    def enter_email(self, email: str) -> None:
        """Enter the email address."""
        self.__email_input.fill(email)

    def enter_password(self, password: str) -> None:
        """Enter the password."""
        self.__password_input.fill(password)

    def enter_phone(self, phone: str) -> None:
        """Enter the phone number."""
        self.__phone_input.fill(phone)

    def enter_registration_details(self, user: CreateUser) -> AuthPage:
        """Enter all registration details."""
        self.enter_first_name(user.first_name)
        self.enter_last_name(user.last_name)
        self.enter_dob(user.dob)
        self.enter_phone(user.phone)
        self.enter_street(user.address.street)
        self.enter_city(user.address.city)
        self.enter_state(user.address.state)
        self.enter_postal_code(user.address.postal_code)
        self.enter_country(user.address.country)
        self.enter_email(user.email)
        self.enter_password(user.password)

        return self

    def click_register_button(self) -> AuthPage:
        """Click the register button."""
        self.__register_button.wait_for(state="visible")
        self.__register_button.click()

        return self
