from django.http import JsonResponse
import requests
from .cdek_api import CDEKAPI
import json
from django.views.decorators.csrf import csrf_exempt

def get_cdek_cityes(request):
    city_name = request.GET.get('city')
    cdek_api = CDEKAPI()
    cityes = cdek_api.get_cityes(city_name)
    return JsonResponse(cityes, safe=False)


@csrf_exempt
def calculate_cdek_tariff(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cdek_api = CDEKAPI()
        tariff = cdek_api.calculate_tariff(data)
        return JsonResponse(tariff)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def get_city(request):
    test_api = CDEKAPI()
    try:
        response = test_api.test_cityes()
        # Извлекаем данные из ответа
        city = response.json()

        # Выводим данные в консоль для отладки
        print("City Data:", city)

        return JsonResponse(city, safe=False)
    except requests.RequestException as e:
        print("Request Error:", str(e))  # Выводим ошибку в консоль
        return JsonResponse({'error': str(e)}, status=500)
    except ValueError as e:
        print("JSON Decode Error:", str(e))  # Выводим ошибку в консоль
        return JsonResponse({'error': 'Invalid JSON response'}, status=500)
    except Exception as e:
        # Обработка любых других исключений
        print("Unexpected Error:", str(e))
        return JsonResponse({'error': 'An unexpected error occurred'}, status=500)