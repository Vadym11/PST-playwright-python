# This is a playground for testing code snippets and experimenting with the API models.
from playwright.sync_api import Page, expect
import pytest

from lib.api_models.user import CreateUser
from utils.test_utils import generate_random_user_data_faker

user: CreateUser = generate_random_user_data_faker()

print(f'User name: {user.first_name} {user.last_name}')
print(f'User email: {user.email}')
print(f'User phone: {user.phone}')
print(f'User dob: {user.dob}')
print(f'User password: {user.password}')

@pytest.mark.mobile
def test_mobile_demo(get_device_, base_url):
    page: Page = get_device_('Pixel 7', False)
    page.goto('/')

    page.get_by_label('Toggle navigation').click()

    page.get_by_role('button', name='Categories').click()
    page.get_by_role('link', name='Power Tools').click()

    page.get_by_test_id('page-title').wait_for(state='visible')

    cordless_drill = page.get_by_role('heading', name=' Cordless Drill 20V ')

    cordless_drill.scroll_into_view_if_needed()

    cordless_drill.click()

    # FIXME: Remove this conditional testing when local testing env is updated to match the production site. 
    # This is a temporary workaround for the difference in the product specifications section.
    if base_url == 'https://www.practicesoftwaretesting.com':
        page.get_by_role('heading', name='Specifications').scroll_into_view_if_needed()

        specs = page.get_by_test_id('spec-name')

        expected_specs = [
            'Battery',
            'Chuck Size',
            'Max Torque',
            'Speed',
            'Voltage',
            'Warranty',
            'Weight',
        ]

        expect(specs).to_have_count(len(expected_specs))

        for i in range(len(specs.all())):
            spec = specs.all()[i]
            expect(spec).to_have_text(expected_specs[i])

        all_spec_texts = specs.all_text_contents()

        assert sorted(all_spec_texts) == sorted(expected_specs), f"Expected specs {expected_specs}, but got {all_spec_texts}"
    
