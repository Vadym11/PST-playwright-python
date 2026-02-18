import re

import allure
import pytest
from playwright.sync_api import Page, expect

@allure.story("Verify Home page")
@allure.title("Verify Home page loads")
@allure.description("Verify Home page fully loads and displays the correct content")
@allure.severity("critical")
@pytest.mark.Smoke  # mark the test case as smoke
def test_main_page(page: Page):
    page.goto("http://localhost:8080")
    expect(page.get_by_test_id('nav-home')).to_be_visible()
    expect(page.get_by_test_id('nav-home')).to_have_text('Home')

    png_bytes = page.screenshot()
    allure.attach(png_bytes, name="full-page", attachment_type=allure.attachment_type.PNG)


@allure.story("Verify login")
@allure.title("Verify login functionality")
@allure.description("Verify user can login successfully")
@allure.severity("critical")
@pytest.mark.Smoke  # mark the test case as smoke
def test_login_success(page: Page):
    page.goto("http://localhost:8080")

    page.get_by_test_id('nav-sign-in').click()

    page.wait_for_timeout(1000)  # wait for 5 seconds to allow the login page to load

    expect(page.get_by_role('heading', name='Login')).to_be_visible()
    expect(page.get_by_test_id('login-form')).to_be_visible()

    page.get_by_test_id('email').fill('customer@practicesoftwaretesting.com')
    page.get_by_test_id('password').fill('welcome01')

    page.get_by_test_id('login-submit').click()

    expect(page.get_by_role('heading', name='My account')).to_be_visible()
    png_bytes = page.screenshot()
    allure.attach(png_bytes, name="full-page", attachment_type=allure.attachment_type.PNG)


