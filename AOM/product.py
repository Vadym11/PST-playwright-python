import json

class ProductAPI:

    def __init__(self, api_handler, **kwargs):
        self.api_handler = api_handler

    def get_all_products(self):
        products = self.api_handler.get('/products', {}, {})

        return products

    def create(self, product_data,):
        response = self.api_handler.post('/products', json.dumps(product_data), {})

        return response

    def delete_by_id(self, product_id):
        response = self.api_handler.delete('/products/{}'.format(product_id))

        return response