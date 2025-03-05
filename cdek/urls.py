from django.urls import path
from . import views

app_name = 'cdek'

urlpatterns = [
    path('test-cdek/', views.cities_and_pvz, name='test_cdek'),
]
