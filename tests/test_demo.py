import os

import requests
from conftest import product_api
from utils.test_utils import generate_new_product_data
from utils.load_settings import settings

api_url = settings['api-url']
product_id = ''

def test_get_products():
    api_endpoint = api_url + "/products/"
    print(api_endpoint)
    response = requests.get(api_endpoint)
    assert response.status_code == 200

    for product in response.json()["data"]:
        assert 'id' in product
        assert product["id"] == product.get("id")

def test_get_all_products(product_api):
    response = product_api.get_all_products()

    for product in response['data']:
        assert 'id' in product
        assert 'name' in product
        assert 'description' in product

def test_create_product(api_handler, product_api):
    global product_id
    product_data = generate_new_product_data(api_handler)

    response = product_api.create(product_data)

    product_id = response["id"]

    assert response['name'] == product_data.get("name")
    assert response['description'] == product_data.get("description")
    assert response['price'] == product_data.get("price")

def test_delete_product_by_id(product_api):
    global product_id

    response = product_api.delete_by_id(product_id)

    assert response == 204

def test_env_vars():
    print(os.environ.get("EMAIL"))
