from pydantic import BaseModel

class ProductImage(BaseModel):
    by_name: str
    by_url: str
    source_name: str
    source_url: str
    file_name: str
    title: str
    id: str
