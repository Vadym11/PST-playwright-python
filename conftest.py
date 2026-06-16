import os
import allure
import pytest
from playwright_stealth import Stealth
from AOM.product_api import ProductAPI
from utils.api_handler import APIHandler
from utils.test_utils import generate_new_product_data, generate_random_user_data_faker

# to bypass bot detection on CircleCI
@pytest.fixture
def page(page):
    Stealth().apply_stealth_sync(page)
    return page

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # "viewport": {"width": 1280, "height": 720},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

@pytest.fixture(scope="function")
def context(context):
    # Set a global timeout for all actions (60 seconds)
    context.set_default_timeout(60000)
    return context

@allure.title("Basic API handler")
@pytest.fixture(scope='module')
def api_handler():
    api_handler = APIHandler()
    api_handler.authenticate_admin()
    return api_handler

@allure.title("Product API fixture")
@pytest.fixture(scope='module')
def product_api(api_handler):
    product_api = ProductAPI(api_handler)
    return product_api

@allure.title("Generate product data and create product fixture")
@pytest.fixture()
def created_product(product_api, generated_product_data):
    created_product = product_api.create(generated_product_data)

    return created_product

@allure.title("Generate product data fixture")
@pytest.fixture()
def generated_product_data(api_handler):
    product_data = generate_new_product_data(api_handler)

    return product_data

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright):
    # Change the default 'data-testid' to 'data-test'
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="module")
def random_user_data():
    random_user_data = generate_random_user_data_faker()

    return random_user_data
# TODO: this is used to add custom command line options to pytest.
# For example, you can run tests with a specific environment like this:
def pytest_addoption(parser):
    parser.addoption("--env", default="staging")

# TODO: this is used to access the custom command line options in your tests.
@pytest.fixture
def env(request):
    return request.config.getoption("--env")

# may be removed later
@pytest.fixture()
def page_iPhone_13(playwright, browser):
    iPhone_13 = playwright.devices["iPhone 13"]
    ctx = browser.new_context(**iPhone_13)
    page = ctx.new_page()
    yield page
    ctx.close()

# may be removed later
@pytest.fixture()
def get_device(playwright, browser):
    """
    Uses built in browser fixture.
    """    
    device_used = []
    def _make_page(device_name):
        device = playwright.devices[device_name]
        ctx = browser.new_context(**device)
        page = ctx.new_page()
        device_used.append((ctx, page))
        return page
    yield _make_page
    for ctx, page in device_used:
        page.close()
        ctx.close()

@pytest.fixture()
def get_device_(playwright, base_url):
    """Launches a new browser context for each device and returns a page object. Closes the context after the test.
    Args:
        playwright: The Playwright instance
        base_url: The base URL for the browser context
    Returns:
        A function that takes a device name and returns a page object.
    """    
    device_cxt = []
    def _make_page(device_name, is_headless=True):
        device = playwright.devices[device_name]
        ios_devices = ['iPhone', 'iPad']
        browser_type = playwright.webkit if any(d in device_name for d in ios_devices) else playwright.chromium
        browser = browser_type.launch(headless=is_headless)
        ctx = browser.new_context(**device, base_url=base_url)
        page = ctx.new_page()
        device_cxt.append((browser, ctx))
        return page
    yield _make_page
    for browser, ctx in device_cxt:
        ctx.close()
        browser.close()

# to be picked up by pytest-playwright plugin, it has to be named exactly as base_url
@pytest.fixture(scope="session")
def base_url(request):
    """
    Checks for a target environment variable first.
    If it doesn't exist, falls back to the pytest.ini 'base_url'.
    """
    # look for your custom environment variable
    env_url = os.getenv("MY_APP_URL")
    if env_url:
        print('\nDefaulting to MY_APP_URL environment variable value: ' + env_url)
        return env_url

    # fallback to pytest.ini base_url value configuration
    # 'pytest-base-url' plugin stores ini config under 'base_url'
    ini_url = request.config.getini("base_url")
    if ini_url:
        print('\nDefaulting to pytest.ini base_url value: ' + ini_url)
        return ini_url

    # fallback to hard-coded value if pytest.ini is empty
    return "http://localhost:8000"