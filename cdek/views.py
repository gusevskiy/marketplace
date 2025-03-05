from django.http import JsonResponse
from django.shortcuts import render
import requests
import time
from .cdek_api import CDEKAPI
import json
from django.views.decorators.csrf import csrf_exempt


def cities_and_pvz(request):
    """Отображает страницу с городами и ПВЗ."""
    cdek_api = CDEKAPI()
    cities = cdek_api.get_city_list() or []
    
    if isinstance(cities, list) and cities and isinstance(cities[0], dict) and 'city' in cities[0]:
        cities.sort(key=lambda x: x['city'])
    
    start1 = time.perf_counter()
    city_code = request.GET.get('city_code')
    print(f"Запрос города занял {time.perf_counter() - start1:.2f} сек")
    start2 = time.perf_counter()
    delivery_points = cdek_api.get_pvz_list(city_code) if city_code else []
    print(f"Запрос ПВЗ занял {time.perf_counter() - start2:.2f} сек")

    # print(delivery_points)

    # Если это HTMX-запрос, отдаем только HTML для списка ПВЗ
    if request.headers.get('HX-Request'):
        return render(request, "cart/pvz_list.html", {"delivery_points": delivery_points})

    # Полная загрузка страницы
    return render(request, "cart/test_cdek.html", {"cities": cities, "delivery_points": delivery_points})

