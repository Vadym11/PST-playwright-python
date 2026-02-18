import json
from typing import Optional, Any, Dict
from lib.api_models.general import PaginatedResponse
from lib.api_models.product import GetProductResponse

class ProductAPI:

    def __init__(self, api_handler, **kwargs):
        self.api_handler = api_handler

    def get_all_products(self) -> PaginatedResponse[GetProductResponse]:
        products = self.api_handler.get('/products')

        return PaginatedResponse[GetProductResponse].model_validate(products)

    def create(self, product_data: Dict[str, Any]) -> GetProductResponse:
        response = self.api_handler.post('/products', product_data)

        return GetProductResponse.model_validate(response)

    def delete_by_id(self, product_id: str) -> Any:
        response = self.api_handler.delete(f'/products/{product_id}')

        if response == 204:  # If no exception was raised, it means the deletion was successful
            return response # Return the status code (e.g., 204 for No Content)

        raise Exception(f'Product with id "{product_id}" not found.')

    def search_by_name(self, name: str) -> PaginatedResponse[GetProductResponse]:
        """
        Searches products and returns a validated PaginatedResponse
        containing GetProductResponse objects.
        """
        # Assuming api_handler returns the JSON dict
        response = self.api_handler.get('/products/search', params={'q': name})

        # This one line validates the pagination AND every product in the 'data' list
        return PaginatedResponse[GetProductResponse].model_validate(response)

    def get_product_id(self, product_name: str) -> Optional[str]:
        """Finds the ID of a product by its name using the paginated response."""
        paginated_data = self.search_by_name(product_name)

        # Accessing .data gives you the list of validated GetProductResponse objects
        for product in paginated_data.data:
            if product.name == product_name:
                return product.id

        return None

    def delete_by_name(self, product_name) -> Any:
        product_id = self.get_product_id(product_name)

        if product_id is not None:
            return self.delete_by_id(product_id)

        raise Exception(f'Product with name "{product_name}" not found.')