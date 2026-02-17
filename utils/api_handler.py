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

    def _get_headers(self, custom_headers=None):
        base = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        return base | (custom_headers or {})

    def get(self, endpoint, headers=None, params=None):
        response = requests.get(self.base_url + endpoint, headers=self._get_headers(headers), params=params)

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, data, headers=None):
        response = requests.post( self.base_url + endpoint, json=data, headers=self._get_headers(headers))

        response.raise_for_status()

        return response.json()

    def delete(self, endpoint, params=None, headers=None):
        response = requests.delete(self.base_url + endpoint, params=params, headers=self._get_headers(headers))

        response.raise_for_status()

        if response.status_code == 204:
            return response.status_code

        return response.json()


