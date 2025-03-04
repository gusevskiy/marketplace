
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Главная страница
    path('', views.product_list, name="product_list"),
    # Страница со списком товара
    path('category/<slug:category_slug>', views.product_list,
         name="product_list_by_category"),
    # Отдельная страница каждого товара
    path('product/<int:id>/<slug:slug>/',
         views.product_detail, name="product_detail"),
]



