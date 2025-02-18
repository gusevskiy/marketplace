from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('pay/<int:order_id>/', views.create_payment, name='create_payment'),
    path("webhook/yookassa/", views.webhook, name="yookassa_webhook"),
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
]
