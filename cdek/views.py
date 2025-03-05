from django.http import JsonResponse
from django.shortcuts import render
import requests
import time
from .cdek_api import CDEKAPI
import json
from django.views.decorators.csrf import csrf_exempt
from cache.views import cache_set, cache_get


def cities_and_pvz(request):
    """Отображает страницу с городами и ПВЗ."""
    city_code = request.GET.get('city_code')
    cities_cache_key = 'cities_data'
    pvz_cache_key = f'pvz_data_{city_code}'

    cities = cache_get(cities_cache_key)
    if cities is None:
        cdek_api = CDEKAPI()
        cities = cdek_api.get_city_list() or []
        if isinstance(cities, list) and cities and isinstance(cities[0], dict) and 'city' in cities[0]:
            cities.sort(key=lambda x: x['city'])
        cache_set(cities_cache_key, cities, 604800) # 7 дней

    delivery_points = cache_get(pvz_cache_key)
    if delivery_points is None and city_code:
        cdek_api = CDEKAPI()
        delivery_points = cdek_api.get_pvz_list(city_code)
        cache_set(pvz_cache_key, delivery_points, 259200) # 3 дня

    # Если это HTMX-запрос, отдаем только HTML для списка ПВЗ
    if request.headers.get('HX-Request'):
        return render(request, "cart/pvz_list.html", {"delivery_points": delivery_points})

    # Полная загрузка страницы
    return render(request, "cart/test_cdek.html", {"cities": cities, "delivery_points": delivery_points})

