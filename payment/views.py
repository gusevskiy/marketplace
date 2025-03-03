from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from yookassa import Configuration, Payment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from .models import Payment as PaymentModel
from django.urls import reverse
from .models import Order
import uuid
import json

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


@login_required
def create_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment_id = str(uuid.uuid4())

    try:
        payment = Payment.create(
            {
                "amount": {
                    "value": str(order.get_total_cost()),  # Сумма заказа
                    "currency": "RUB"
                },
                "confirmation": {
                    "type":
                    "redirect",
                    "return_url":
                    request.build_absolute_uri(
                        reverse("product:product_list")),
                },
                "capture": True,
                "description": f"Order {order.id}",
            },
            payment_id)

        # Сохраняем платеж в БД
        PaymentModel.objects.create(
            order=order,
            payment_id=payment.id,
            status=payment.status,
            amount=order.get_total_cost(),
        )
        print(f"Создан платеж {payment.id}")  # Добавь лог для проверки
        PaymentModel.objects.values_list("payment_id", flat=True)

    except Exception as e:
        return JsonResponse({"error", str(e)}, status=500)

    return redirect(payment.confirmation.confirmation_url)
    # return JsonResponse({"confirmation_url": payment.confirmation.confirmation_url})


@require_POST
@csrf_exempt
def webhook(request):
    event = json.loads(request.body)
    payment_id = event.get("object", {}).get("id")
    status = event.get("object", {}).get("status")
    print("Request method:", request.method)
    print("Request body:", request.body)

    try:
        payment = PaymentModel.objects.get(payment_id=payment_id)
        payment.status = status
        payment.save()

        if status == "succeeded":
            payment.order.status = "оплачен"
            payment.order.save()

        elif status == "canceled":  # Статус отмены платежа
            payment.order.status = "отменен"
            payment.order.save()

        return JsonResponse({"status": "ok"})
    except PaymentModel.DoesNotExist:
        return JsonResponse({"error": "Payment not found"}, status=404)


def payment_success(request):
    return render(request, "payment/success.html")


def payment_cancel(request):
    # Шаблон для отмены оплаты
    return render(request, "payment/cancel.html")
