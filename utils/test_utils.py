import random
from typing import List
from faker import Faker
from lib.api_models.product import Product
from lib.api_models.user import CreateUser, Address
from utils.api_utils import *

fake = Faker('en_US')

def generate_new_product_data(api_handler) -> Product:
    name = fake.catch_phrase()
    description = fake.bs().title()
    # price() returns a string in Faker, so we float it
    # price = float(fake.commerce.price(min=10, max=200, decimals=2))
    price = fake.pyfloat(min_value=1, max_value=200, right_digits=2)
    is_location_offer = random.choice([0, 1])
    is_rental = random.choice([0, 1])
    co2_rating = random.choice(['A', 'B', 'C', 'D', 'E'])

    # Await the ID lookups
    category_id = random.choice(get_category_ids(api_handler))
    brand_id = random.choice(get_brand_ids(api_handler))
    product_image_id = random.choice(get_image_ids(api_handler))

    print(f"Generated Product Name: {name}")

    return Product(
        name=name,
        description=description,
        price=price,
        is_location_offer=is_location_offer,
        is_rental=is_rental,
        co2_rating=co2_rating,
        category_id=category_id,
        brand_id=brand_id,
        product_image_id=product_image_id,
    )

    # return {
    #     "name": name,
    #     "description": description,
    #     "price": price,
    #     "is_location_offer": is_location_offer,
    #     "is_rental": is_rental,
    #     "co2_rating": co2_rating,
    #     "category_id": category_id,
    #     "brand_id": brand_id,
    #     "product_image_id": product_image_id,
    # }

def generate_random_user_data_faker() -> CreateUser:
    first_name = fake.first_name().replace("'", "")
    last_name = fake.last_name().replace("'", "")
    dob = fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()
    street = fake.street_address()
    postal_code = fake.postcode()
    city = fake.city()
    state = fake.state()
    country = fake.country()[:40]  # Max length 40 chars
    phone = f"510{random.randint(10000000, 99999999)}"
    email = f"{first_name}.{last_name}@gmail.com".lower()
    password = f"{first_name}.{last_name}**12345$%"

    print(f"Generated user: {first_name} {last_name}")

    return CreateUser(
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        phone=phone,
        email=email,
        address=Address(
            street=street,
            postal_code=postal_code,
            city=city,
            state=state,
            country=country,
        ),
        password=password,
    )

def get_category_ids(api_handler) -> List[str]:
    categories = get_all_categories(api_handler)

    category_ids = []
    for category in categories:
        category_ids.append(category["id"])

    return category_ids

def get_brand_ids(api_handler) -> List[str]:
    brands = get_all_brands(api_handler)

    brand_ids = []
    for brand in brands:
        brand_ids.append(brand["id"])

    return brand_ids

def get_image_ids(api_handler) -> List[str]:
    images = get_all_images(api_handler)

    image_ids = []
    for image in images:
        image_ids.append(image["id"])

    return image_ids
