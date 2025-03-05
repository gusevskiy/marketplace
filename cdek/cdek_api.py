import requests
import os
from django.conf import settings
from datetime import datetime, timedelta
from .models import CDEKToken

class CDEKAPI:
    def __init__(self):
        self.base_url = settings.CDEK_API_URL
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.get_token()

    def get_token(self):
        token_obj = CDEKToken.objects.first()
        if token_obj and token_obj.expires_at > datetime.now():
            self.token = token_obj.access_token
            self.headers['Authorization'] = f'Bearer {self.token}'
            return True
        else:
            return self.refresh_token()

    def refresh_token(self):
        url = f'{self.base_url}/v2/oauth/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': settings.CDEK_CLIENT_ID,
            'client_secret': settings.CDEK_CLIENT_SECRET
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token_data = response.json()
            self.token = token_data['access_token']
            self.headers['Authorization'] = f'Bearer {self.token}'
            # время токена в секундах, прибавляем их к текущему и получаем врямя истечения
            self.token_expiration = datetime.now() + timedelta(seconds=token_data['expires_in'])
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