from django.conf import settings
from django.http import JsonResponse
from yookassa import Configuration, Payment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Payment as PaymentModel
from .models import Order
import uuid
import json



Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


def create_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": str(order.total_price),  # Сумма заказа
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://your-site.com/payment-success"
        },
        "capture": True,
        "description": f"Order {order.id}",
    }, payment_id)


    # Сохраняем платеж в БД
    PaymentModel.objects.create(
        order=order,
        payment_id=payment.id,
        status=payment.status,
        amount=order.total_price,
    )

    return JsonResponse({"confirmation_url": payment.confirmation.confirmation_url})

@csrf_exempt
def webhook(request):
    event = json.loads(request.body)
    payment_id = event.get("object", {}).get("id")
    status = event.get("object", {}).get("status")

    try:
        payment = Payment.objects.get(payment_id=payment_id)
        payment.status = status
        payment.save()

        if status == "succeeded":
            payment.order.status = "оплачен"
            payment.order.save()

        return JsonResponse({"status": "ok"})
    except Payment.DoesNotExist:
        return JsonResponse({"error": "Payment not found"}, status=404)