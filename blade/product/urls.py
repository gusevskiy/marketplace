from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком товара
    path('product/', views.catalog_list),
    # Отдельная страница каждого товара
    path('product/<int:pk>/', views.catalog_detail),
]