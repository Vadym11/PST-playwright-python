import os
import requests
from utils.load_settings import settings
from dotenv import load_dotenv

load_dotenv()

class APIHandler:

    def __init__(self):
        self.base_url = os.getenv("API_URL", settings['api-url_'])
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD_")
        self.token = ''

    def authenticate_admin(self):
        print(f'{self.base_url}/users/login')
        response = requests.post(
            f'{self.base_url}/users/login',
            json={'email': self.email, 'password': self.password },
        )

        body = response.json()

        if not response.ok:
            print(response.status_code)
            raise Exception(body.get('message'))

        self.token = body.get('access_token')

        print('APIHandler: Admin authenticated successfully.')


    def get(self, endpoint, data, headers):
        response = requests.request("GET", self.base_url + endpoint, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(response.text)

        return response.json()

    def post(self, endpoint, data, headers):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        } | (headers or {})

        response = requests.request("POST", self.base_url + endpoint, data=data, headers=headers)

        if not response.ok:
            raise Exception(response.text)

        return response.json()

    def delete(self, endpoint, headers=None):

        headers = {
          'Content-Type': 'application/json',
          'Authorization': f'Bearer {self.token}'
        } | (headers or {})

        response = requests.request("DELETE", self.base_url + endpoint, params={}, headers=headers)

        if not response.ok:
            raise Exception(response.text)

        if response.status_code == 204:
            return response.status_code

        return response.json()


