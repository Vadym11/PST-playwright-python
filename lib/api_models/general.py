from typing import List, TypeVar, Generic, Optional
from pydantic import BaseModel, Field, ConfigDict

# T is a placeholder for any model (Product, Brand, etc.)
T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    # Allow Pydantic to use the alias 'from' when reading the API JSON
    model_config = ConfigDict(populate_by_name=True)

    current_page: int
    data: List[T]
    # Map the JSON key "from" to this variable
    from_item: Optional[int] = Field(alias="from", default=None)
    last_page: int
    per_page: int
    to: Optional[int] = None
    total: int

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class SuccessResponse(BaseModel):
    success: bool

class LogOutResponse(BaseModel):
    message: str
