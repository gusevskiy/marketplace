import requests
import os
from django.conf import settings
from datetime import datetime, timedelta
from .models import CDEKToken
import logging

logger = logging.getLogger(__name__)

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
            logger.debug("Используется существующий токен из базы данных.")
            return True
        else:
            logger.debug("Токен в базе данных отсутствует или устарел. Запрос на обновление.")
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
            logger.debug("Токен успешно обновлен.")
            return True
        else:
            logger.error(f"Ошибка обновления токена: {response.status_code}, {response.text}")
            return False

    def get_city_list(self, country_code='RU'):
        url = f'{self.base_url}/v2/location/cities'
        params = {'country_codes': country_code, 'size': 1000} #Увеличил размер выдачи
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_pvz_list(self, city_code):
        # Запрос к API СДЭК для получения списка ПВЗ
        # Здесь нужно добавить вашу логику для работы с API СДЭК.
        logger.debug(f"Запрос списка ПВЗ для города {city_code}")
        url = f'{self.base_url}/v2/deliverypoints'
        params = {'city_code': city_code}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Ошибка при получении списка ПВЗ"}

    def test_cityes(self):
        url = f'{self.base_url}/v2/deliverypoints'
        print(url)
        response = requests.get(url, headers=self.headers)
        print(response)
        return response