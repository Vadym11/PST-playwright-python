import allure
import pytest
from AOM.product_api import ProductAPI
from utils.api_handler import APIHandler
from utils.test_utils import generate_new_product_data

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