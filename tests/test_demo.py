import os
import allure
import requests
from conftest import product_api
from utils.test_utils import generate_new_product_data
from utils.load_settings import settings

api_url = settings['api-url']

@allure.story("Test create product 0")
@allure.title("Verify the create products API 0")
@allure.description("verify the create product API response status code and data 0")
@allure.severity("normal")
def test_get_products():
    api_endpoint = api_url + "/products/"
    print(api_endpoint)
    response = requests.get(api_endpoint)
    assert response.status_code == 200

    for product in response.json()["data"]:
        assert 'id' in product
        assert product["id"] == product.get("id")

@allure.story("Test get all products")
@allure.title("Verify the get all products API")
@allure.description("verify the get API response status code and data")
@allure.severity("normal")
def test_get_all_products(product_api):
    response = product_api.get_all_products()

    for product in response['data']:
        assert 'id' in product
        assert 'name' in product
        assert 'description' in product

@allure.story("Test create product")
@allure.title("Verify the create products API")
@allure.description("verify the create product API response status code and data")
@allure.severity("normal")
def test_create_product(api_handler, product_api, created_product, generated_product_data):
    product_data = generated_product_data

    assert created_product['name'] == product_data.get("name")
    assert created_product['description'] == product_data.get("description")
    assert created_product['price'] == product_data.get("price")

@allure.story("Test delete product")
@allure.title("Verify the delete products API")
@allure.description("verify the delete product API response status code and data")
@allure.severity("normal")
def test_delete_product_by_id(product_api, created_product):
    created_product = created_product
    response = product_api.delete_by_id(created_product['id'])

    assert response == 204

@allure.story("Test get env vars")
@allure.title("Verify the get env vars API")
@allure.description("verify env vars are present")
@allure.severity("normal")
def test_env_vars():
    print(os.environ.get("EMAIL"))
