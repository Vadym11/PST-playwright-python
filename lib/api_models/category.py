from typing import List, Optional
from pydantic import BaseModel

class BaseCategory(BaseModel):
    name: str
    slug: Optional[str] = None

class Category(BaseCategory):
    id: str

class GetCategoriesResponse(BaseCategory):
    id: str
    # Use Optional because the error showed parent_id might be missing or null
    parent_id: Optional[str] = None

class GetCategoryResponse(GetCategoriesResponse):
    # Use Optional and default to an empty list to prevent "Field required" errors
    sub_categories: Optional[List[str]] = None
