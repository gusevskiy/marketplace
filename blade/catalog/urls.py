from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком товара
    path('catalog/', views.catalog_list),
    # Отдельная страница каждого товара
    path('catalog/<int:pk>/', views.catalog_detail),
]