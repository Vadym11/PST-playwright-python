from pydantic import BaseModel
from .category import Category
from .brand import GetBrand
from .image import ProductImage

class BaseProduct(BaseModel):
    name: str
    description: str
    price: float  # number in JS maps to float (or int) in Python
    is_location_offer: int
    is_rental: int
    co2_rating: str

class Product(BaseProduct):
    category_id: str
    brand_id: str
    product_image_id: str

class GetProductResponse(BaseProduct):
    id: str
    is_eco_friendly: bool
    brand: GetBrand
    category: Category
    product_image: ProductImage
