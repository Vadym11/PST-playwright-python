from playwright.sync_api import Page, expect
from lib.pages.home_page import HomePage

def test_register_new_user_happy_path(page: Page, random_user_data):
    """Register a new user."""

    home_page = HomePage(page).go_to()
    sign_in_page = home_page.header.click_sign_in_link()

    (sign_in_page
     .click_register_link()
     .enter_registration_details(random_user_data)
     .click_register_button()
    # if registration is successful, it should navigate to the login page, which we assert here
     .assert_login_page())