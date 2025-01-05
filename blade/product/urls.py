from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Главная страница
    path('', views.product_list, name="product_list"),
    # Страница со списком товара
    # path('product/', views.catalog_list),
    # Отдельная страница каждого товара
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
]



if settings.DEBUG:  # Для разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)