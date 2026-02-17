import os
import allure
import requests
from conftest import product_api
from utils.load_settings import settings
import pytest

api_url = settings['api-url']

@allure.story("Test create product 0")
@allure.title("Verify the create products API 0")
@allure.description("verify the create product API response status code and data 0")
@allure.severity("normal")
@pytest.mark.Regression  # mark the test case as regression
def test_get_products():
    api_endpoint = api_url + "/products/"
    print(f'\n{api_endpoint}')
    response = requests.get(api_endpoint)
    assert response.status_code == 200

    for product in response.json()["data"]:
        assert 'id' in product
        assert product["id"] == product.get("id")

def test_get_all_products(product_api):
    response = product_api.get_all_products()

    assert response.status_code == 200

    for product in response['data']:
        assert 'id' in product
        assert 'name' in product
        assert 'description' in product

@allure.story("Test get all products")
@allure.title("Verify the get all products API")
@allure.description("verify the get API response status code and data")
@allure.severity("normal")
@pytest.mark.Regression  # mark the test case as regression
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
@pytest.mark.Smoke  # mark the test case as smoke
def test_create_product(api_handler, product_api, created_product, generated_product_data):
    product_data = generated_product_data

    assert created_product['name'] == product_data.get("name")
    assert created_product['description'] == product_data.get("description")
    assert created_product['price'] == product_data.get("price")

@allure.story("Test delete product")
@allure.title("Verify the delete products API")
@allure.description("verify the delete product API response status code and data")
@allure.severity("normal")
@pytest.mark.Smoke  # mark the test case as smoke
def test_delete_product_by_id(product_api, created_product):
    response = product_api.delete_by_id(created_product['id'])

    assert response == 204

@allure.story("Test get env vars")
@allure.title("Verify the get env vars API")
@allure.description("verify env vars are present")
@allure.severity("normal")
@pytest.mark.Smoke  # mark the test case as smoke
def test_env_vars():
    print(os.environ.get("EMAIL"))

@allure.severity("critical")
@pytest.mark.Smoke
def test_search_product_by_name(product_api, created_product):
    response_body = product_api.search_by_name(created_product['name'])

    assert 'data' in response_body
    assert len(response_body['data']) > 0

    for product in response_body['data']:
        assert 'id' in product
        assert 'name' in product
        assert 'description' in product

    assert created_product['name'] == response_body['data'][0]['name']

@pytest.mark.Smoke
def test_verify_search_by_full_name(product_api, created_product):
    product_id = product_api.get_product_id(created_product['name'])

    assert product_id == created_product['id']
