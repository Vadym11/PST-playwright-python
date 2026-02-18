from typing import Optional

from pydantic import BaseModel

class Brand(BaseModel):
    id: str
    name: str
    # API is sending Brand without a slug, so make it optional
    slug: Optional[str] = None

class GetBrand(Brand):
    id: str
