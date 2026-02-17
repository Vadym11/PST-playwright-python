import json

class ProductAPI:

    def __init__(self, api_handler, **kwargs):
        self.api_handler = api_handler

    def get_all_products(self):
        products = self.api_handler.get('/products')

        return products

    def create(self, product_data):
        response = self.api_handler.post('/products', product_data)

        return response

    def delete_by_id(self, product_id):
        response = self.api_handler.delete('/products/{}'.format(product_id))

        return response

    def search_by_name(self, name):
        response = self.api_handler.get('/products/search', None, {'q': name})

        return response

    def get_product_id(self, product_name):
        response_body = self.search_by_name(product_name)

        for product in response_body['data']:
            if product['name'] == product_name:
                return product['id']

        return None

    def delete_by_name(self, product_name):
        product_id = self.get_product_id(product_name)

        if product_id is not None:
            return self.delete_by_id(product_id)
        else:
            raise Exception(f'Product with name "{product_name}" not found.')