from django.urls import path
from . import views

app_name = 'cdek'

urlpatterns = [
    path('city/', views.get_city, name='city'),

    path('cityes/', views.get_cdek_cityes, name='cdek_cityes'),
    path('tariff/', views.calculate_cdek_tariff, name='cdek_tariff'),
]