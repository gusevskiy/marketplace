from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .tasks import order_created
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse


# @login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            print(cart.__dict__)
            for item in cart:
                OrderItem.objects.create(
                    product=item['product'],
                    order=order,
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            order_created.delay(order.id)
            # задать заказ в сеансе
            request.session['order_id'] = order.id
            # перенаправить к платежу
            return redirect(reverse('payment:create_payment', args=[order.id]))
            # return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
