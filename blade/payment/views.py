from django.conf import settings
from django.http import JsonResponse
from yookassa import Configuration, Payment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from .models import Payment as PaymentModel
from .models import Order
import uuid
import json



Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY



@login_required
def create_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment_id = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": str(order.get_total_cost()),  # Сумма заказа
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://g79cud29d6bu.share.zrok.io/payment/success/"
        },
        "capture": True,
        "description": f"Order {order.id}",
    }, payment_id)


    # Сохраняем платеж в БД
    PaymentModel.objects.create(
        order=order,
        payment_id=payment.id,
        status=payment.status,
        amount=order.get_total_cost(),
    )

    return redirect(payment.confirmation.confirmation_url)
    # return JsonResponse({"confirmation_url": payment.confirmation.confirmation_url})

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
    

def payment_success(request):
    return render(request, "payment/success.html")
