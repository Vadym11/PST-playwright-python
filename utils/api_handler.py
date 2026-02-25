import os
from typing import Literal
import requests
from requests import HTTPError
from utils.load_settings import settings
from dotenv import load_dotenv

load_dotenv()

class APIHandler:

    def __init__(self):
        self.base_url = os.getenv("API_URL", settings['api-url_'])
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD_")
        self.token = ''

    def authenticate_admin(self) -> None:
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

    def _get_headers(self, custom_headers=None) -> dict:
        base = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        return base | (custom_headers or {})

    def get(self, endpoint, headers=None, params=None) -> dict:
        response = requests.get(self.base_url + endpoint, headers=self._get_headers(headers), params=params)

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, data, headers=None) -> dict:
        response = requests.post( self.base_url + endpoint, json=data, headers=self._get_headers(headers))

        response.raise_for_status()

        return response.json()

    def delete(self, endpoint, params=None, headers=None) -> Literal[204] | None:
        response = requests.delete(self.base_url + endpoint, params=params, headers=self._get_headers(headers))

        try:
            response.raise_for_status()  # Raises HTTPError for 4xx/5xx
        except HTTPError as e:
            # If it's a 404, return None so delete_by_id can handle it
            if response.status_code == 404:
                return None
            # For any other error (500, 403, etc.), re-raise so the app crashes/logs it
            raise e

        if response.status_code == 204:
            return 204

        return response.json()


