import requests
import os
from django.conf import settings
from datetime import datetime, timedelta

class CDEKAPI:
    def __init__(self):
        self.token = settings.CDEK_API_TOKEN
        self.base_url = settings.CDEK_API_URL
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        # self.get_token()

    def refresh_token(self):
        url = f'{self.base_url}/oauth/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': settings.CDEK_CLIENT_ID, #Добавить в .env CLIENT_ID
            'client_secret': settings.CDEK_CLIENT_SECRET #Добавить в .env CLIENT_SECRET
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token_data = response.json()
            self.token = token_data['access_token']
            self.headers['Authorization'] = f'Bearer {self.token}'
            self.token_expiration = datetime.now() + timedelta(seconds=token_data['expires_in']) # Обновляем время жизни токена.
            settings.CDEK_API_TOKEN = self.token #Обновляем токен в настройках
            return True
        else:
            return False

    def get_cityes(self, city_name):
        url = f'{self.base_url}/location/cities'
        params = {'city': city_name}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()


    def calculate_tariff(self, data):
        url = f'{self.base_url}/calculator/tariff'
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()


    def test_cityes(self):
        url = f'{self.base_url}/v2/deliverypoints'
        print(url)
        response = requests.get(url, headers=self.headers)
        print(response)
        return response