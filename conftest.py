import allure
import pytest
from AOM.product_api import ProductAPI
from utils.api_handler import APIHandler
from utils.test_utils import generate_new_product_data

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