# This is a playground for testing code snippets and experimenting with the API models.

from lib.api_models.user import CreateUser
from utils.test_utils import generate_random_user_data_faker

user: CreateUser = generate_random_user_data_faker()

print(f'User name: {user.first_name} {user.last_name}')
print(f'User email: {user.email}')
print(f'User phone: {user.phone}')
print(f'User dob: {user.dob}')
print(f'User password: {user.password}')