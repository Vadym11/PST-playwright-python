from pydantic import BaseModel

class Address(BaseModel):
    street: str
    postal_code: str
    city: str
    state: str
    country: str

class BaseUser(BaseModel):
    first_name: str
    last_name: str
    phone: str
    dob: str
    email: str
    address: Address

class CreateUser(BaseUser):
    password: str